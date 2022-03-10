"""Logging Configuration"""
__docformat__ = "numpy"
import logging
from logging.handlers import TimedRotatingFileHandler
import os
import re
from pathlib import Path
import sys
import time
import uuid
from math import floor, ceil
import requests

import schedule
import git
import boto3
from botocore.exceptions import ClientError

import gamestonk_terminal.config_terminal as cfg
from gamestonk_terminal import feature_flags as gtff

logger = logging.getLogger(__name__)
LOGFORMAT = "%(asctime)s|%(name)s|%(funcName)s|%(lineno)s|%(message)s"
LOGPREFIXFORMAT = "%(levelname)s|%(appName)s|%(version)s|%(loggingId)s|%(sessionId)s|"
DATEFORMAT = "%Y-%m-%dT%H:%M:%S%z"
BUCKET = "gst-restrictions"
FOLDER_NAME = "gst-app/logs"
URL = "https://knaqi3sud7.execute-api.eu-west-3.amazonaws.com/log_api/logs"


def library_loggers(verbosity: int = 0) -> None:
    """Setup library logging

    Parameters
    ----------
    verbosity : int, optional
        Log level verbosity, by default 0
    """

    logging.getLogger("requests").setLevel(verbosity)
    logging.getLogger("urllib3").setLevel(verbosity)


def get_log_dir() -> Path:
    file_path = Path(__file__)
    logger.debug("Parent dir: %s", file_path.parent.parent.absolute())
    log_dir = file_path.parent.parent.absolute().joinpath("logs")
    logger.debug("Future logdir: %s", log_dir)

    if not os.path.isdir(log_dir.absolute()):
        logger.debug("Logdir does not exist. Creating.")
        os.mkdir(log_dir.absolute())

    log_id = log_dir.absolute().joinpath(".logid")

    if not os.path.isfile(log_id.absolute()):
        logger.debug("Log ID does not exist: %s", log_id.absolute())
        cfg.LOGGING_ID = f"{uuid.uuid4()}"
        with open(log_id.absolute(), "a") as a_file:
            a_file.write(f"{cfg.LOGGING_ID}\n")
    else:
        logger.debug("Log ID exists: %s", log_id.absolute())
        with open(log_id.absolute()) as a_file:
            cfg.LOGGING_ID = a_file.readline().rstrip()

    logger.debug("Log id: %s", cfg.LOGGING_ID)

    uuid_log_dir = log_dir.absolute().joinpath(cfg.LOGGING_ID)

    logger.debug("Current_log dir: %s", uuid_log_dir)

    if not os.path.isdir(uuid_log_dir.absolute()):
        logger.debug(
            "UUID_log dir does not exist: %s. Creating.", uuid_log_dir.absolute()
        )
        os.mkdir(uuid_log_dir.absolute())
    return uuid_log_dir


def setup_file_logger(app_name: str, session_id: str) -> None:
    """Setup File Logger"""

    uuid_log_dir = get_log_dir()

    upload_archive_logs_s3(directory_str=uuid_log_dir, log_filter=r"gst_")

    start_time = int(time.time())
    cfg.LOGGING_FILE = uuid_log_dir.absolute().joinpath(f"gst_{start_time}")  # type: ignore

    logger.debug("Current_log file: %s", cfg.LOGGING_FILE)

    handler = TimedRotatingFileHandler(cfg.LOGGING_FILE)
    handler.suffix += ".log"
    formatter = CustomFormatterWithExceptions(
        app_name, uuid_log_dir.stem, session_id, fmt=LOGFORMAT, datefmt=DATEFORMAT
    )
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)


class CustomFormatterWithExceptions(logging.Formatter):
    """Custom Logging Formatter that includes formatting of Exceptions"""

    def __init__(
        self,
        app_name: str,
        logging_id: str,
        session_id: str,
        fmt=None,
        datefmt=None,
        style="%",
        validate=True,
    ) -> None:
        super().__init__(fmt=fmt, datefmt=datefmt, style=style, validate=validate)
        self.logPrefixDict = {
            "loggingId": logging_id,
            "sessionId": session_id,
            "version": cfg.LOGGING_VERSION,
            "appName": app_name,
        }

    def formatException(self, ei) -> str:
        """Exception formatting handler

        Parameters
        ----------
        ei : logging._SysExcInfoType
            Exception to be logged

        Returns
        -------
        str
            Formatted exception
        """
        result = super().formatException(ei)
        return repr(result)

    def format(self, record: logging.LogRecord) -> str:
        """Log formatter

        Parameters
        ----------
        record : logging.LogRecord
            Logging record

        Returns
        -------
        str
            Formatted_log message
        """
        if hasattr(record, "func_name_override"):
            record.funcName = record.func_name_override  # type: ignore
            record.lineno = 0

        if hasattr(record, "user_id"):
            self.logPrefixDict["loggingId"] = record.user_id  # type: ignore

        if hasattr(record, "session_id"):
            self.logPrefixDict["sessionId"] = record.session_id  # type: ignore

        s = super().format(record)
        if record.levelname:
            self.logPrefixDict["levelname"] = record.levelname[0]
        else:
            self.logPrefixDict["levelname"] = "U"

        if record.exc_text:
            self.logPrefixDict["levelname"] = "X"
            logPrefix = LOGPREFIXFORMAT % self.logPrefixDict
            s = (
                s.replace("\n", " - ")
                .replace("\t", " ")
                .replace("\r", "")
                .replace("'", "`")
                .replace('"', "`")
            )

        else:
            logPrefix = LOGPREFIXFORMAT % self.logPrefixDict
        return f"{logPrefix}{s}"


def get_commit_hash() -> None:
    """Get Commit Short Hash"""

    file_path = Path(__file__)
    git_dir = file_path.parent.parent.absolute().joinpath(".git")

    if os.path.isdir(git_dir.absolute()):
        repo = git.Repo(search_parent_directories=True)
        sha = repo.head.object.hexsha
        short_sha = repo.git.rev_parse(sha, short=8)
        cfg.LOGGING_VERSION = f"sha:{short_sha}"


def setup_logging(app_name: str) -> None:
    """Setup Logging"""

    START_TIME = int(time.time())
    LOGGING_ID = cfg.LOGGING_ID if cfg.LOGGING_ID else ""

    verbosity_terminal = floor(cfg.LOGGING_VERBOSITY / 10) * 10
    verbosity_libraries = ceil(cfg.LOGGING_VERBOSITY / 10) * 10
    logging.basicConfig(
        level=verbosity_terminal, format=LOGFORMAT, datefmt=DATEFORMAT, handlers=[]
    )

    get_commit_hash()

    for a_handler in cfg.LOGGING_HANDLERS.split(","):
        if a_handler == "stdout":
            handler = logging.StreamHandler(sys.stdout)
            formatter = CustomFormatterWithExceptions(
                app_name, LOGGING_ID, str(START_TIME), fmt=LOGFORMAT, datefmt=DATEFORMAT
            )
            handler.setFormatter(formatter)
            logging.getLogger().addHandler(handler)
        elif a_handler == "stderr":
            handler = logging.StreamHandler(sys.stderr)
            formatter = CustomFormatterWithExceptions(
                app_name, LOGGING_ID, str(START_TIME), fmt=LOGFORMAT, datefmt=DATEFORMAT
            )
            handler.setFormatter(formatter)
            logging.getLogger().addHandler(handler)
        elif a_handler == "noop":
            handler = logging.NullHandler()  # type: ignore
            formatter = CustomFormatterWithExceptions(
                app_name, LOGGING_ID, str(START_TIME), fmt=LOGFORMAT, datefmt=DATEFORMAT
            )
            handler.setFormatter(formatter)
            logging.getLogger().addHandler(handler)
        elif a_handler == "file":
            setup_file_logger(app_name, str(START_TIME))
        else:
            logger.debug("Unknown loghandler")

    library_loggers(verbosity_libraries)

    logger.info("Logging configuration finished")
    logger.info("Logging set to %s", cfg.LOGGING_HANDLERS)
    logger.info("Verbosity set to %s", verbosity_libraries)
    logger.info(
        "FORMAT: %s%s", LOGPREFIXFORMAT.replace("|", "-"), LOGFORMAT.replace("|", "-")
    )


def upload_file_to_s3(
    file: Path, bucket: str = None, object_name: str = None, folder_name: str = None
) -> None:
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file.name

    # If folder_name was specified, upload in the folder
    if folder_name is not None:
        object_name = f"{folder_name}/{object_name}"

    if not object_name.endswith(".log"):
        object_name += ".log"

    # Upload the file
    if (
        bucket is not None
        and cfg.AWS_ACCESS_KEY != "REPLACE_ME"
        and cfg.AWS_ACCESS_KEY_ID != "REPLACE_ME"
    ):
        try:
            s3_client = boto3.client(
                service_name="s3",
                aws_access_key_id=cfg.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=cfg.AWS_ACCESS_KEY,
            )
            s3_client.upload_file(str(file), bucket, object_name)
        except ClientError as e:
            logger.exception(str(e))
    else:
        files = None
        try:
            with open(file, "rb") as f:
                files = {"file": f.read()}
        except Exception as e:
            logger.exception("Could not open file: %s", str(e))

        if files is not None and files:
            json = requests.put(url=URL, json={"object_key": object_name}).json()
            r = requests.post(json["url"], data=json["fields"], files=files)

            if r.status_code in [403, 401, 400]:
                logger.error("%s could not be uploaded", str(file))
            elif r.status_code == 204:
                logger.info("Log uploaded")
            else:
                logger.error(
                    "Unexpected status_code: %s when uploading: %s",
                    str(r.status_code),
                    str(file),
                )
        else:
            logger.error("Uploading payload empty")


def contains_goodbye(file: Path) -> bool:
    with open(file, "rb") as f:
        try:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b"\n":
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
            logger.exception("Could not find last line")
            return False
        last_line = f.readline().decode()
    return "print_goodbye" in last_line


def upload_archive_logs_s3(
    directory_str=None,
    log_filter=r"gst_\d{10}\.20[2-3][0-9]-[0-2][0-9]-[0-3][0-9]_[0-2][0-9]\.log",
    bucket=None,
    folder_name=FOLDER_NAME,
) -> None:
    if gtff.ALLOW_LOG_COLLECTION:
        if directory_str is None:
            directory = get_log_dir()
        else:
            directory = Path(directory_str)
        archive = directory / "archive"

        if not archive.exists():
            # Create a new directory because it does not exist
            archive.mkdir()
            logger.debug("The new archive directory is created!")

        log_files = {}

        for file in directory.iterdir():

            one_day_old = (
                file.name[4:14].isdigit()
                and (int(time.time()) - int(file.name[4:14])) / 86400 > 1
            )  # 86400 seconds in one day

            regexp = re.compile(log_filter)
            if regexp.search(str(file)) and (
                file.suffix == ".log" or one_day_old or contains_goodbye(file)
            ):
                log_files[str(file)] = file, (archive / file.name)

        for log_file, archived_file in log_files.values():
            logger.info("Uploading logs")
            upload_file_to_s3(
                file=log_file,
                bucket=bucket,
                folder_name=f"{folder_name}/{cfg.LOGGING_ID}",
            )
            try:
                log_file.rename(archived_file)
            except Exception as e:
                logger.exception("Cannot archive file: %s", str(e))
    else:
        logger.info("Logs not allowed to be collected")


def periodically_upload_logs() -> None:
    schedule.every(65).minutes.do(upload_archive_logs_s3)
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait a minute
