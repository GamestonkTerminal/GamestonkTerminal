# IMPORT STANDARD
import logging
import sys

# IMPORT THIRD-PARTY
# IMPORT INTERNAL
from openbb_sdk_core.logs.formatters.formatter_with_exceptions import (
    FormatterWithExceptions,
)
from openbb_sdk_core.logs.handlers.path_tracking_file_handler import (
    PathTrackingFileHandler,
)
from openbb_sdk_core.logs.handlers.posthog_handler import PosthogHandler
from openbb_sdk_core.logs.models.logging_settings import LoggingSettings


class HandlersManager:
    def __init__(self, settings: LoggingSettings):
        self.is_initialized = True

        self._handlers = settings.handler_list
        self._settings = settings

        for handler_type in self._handlers:
            if handler_type == "stdout":
                self._add_stdout_handler()
            elif handler_type == "stderr":
                self._add_stderr_handler()
            elif handler_type == "noop":
                self._add_noop_handler()
            elif handler_type == "file":
                self._add_file_handler()
            elif handler_type == "posthog":
                self._add_posthog_handler()
            else:
                logging.getLogger().debug("Unknown log handler.")

    def _add_posthog_handler(self):
        handler = PosthogHandler(settings=self._settings)
        formatter = FormatterWithExceptions(settings=self._settings)
        handler.setFormatter(formatter)
        logging.getLogger().addHandler(handler)

    def _add_stdout_handler(self):
        handler = logging.StreamHandler(sys.stdout)
        formatter = FormatterWithExceptions(settings=self._settings)
        handler.setFormatter(formatter)
        logging.getLogger().addHandler(handler)

    def _add_stderr_handler(self):
        handler = logging.StreamHandler(sys.stderr)
        formatter = FormatterWithExceptions(settings=self._settings)
        handler.setFormatter(formatter)
        logging.getLogger().addHandler(handler)

    def _add_noop_handler(self):
        handler = logging.NullHandler()
        formatter = FormatterWithExceptions(settings=self._settings)
        handler.setFormatter(formatter)
        logging.getLogger().addHandler(handler)

    def _add_file_handler(self):
        handler = PathTrackingFileHandler(settings=self._settings)
        formatter = FormatterWithExceptions(settings=self._settings)
        handler.setFormatter(formatter)
        logging.getLogger().addHandler(handler)

    def update_handlers(self, settings: LoggingSettings):
        logger = logging.getLogger()
        for hdlr in logger.handlers:
            if isinstance(hdlr, (PathTrackingFileHandler, PosthogHandler)):
                hdlr.settings = settings
                hdlr.formatter.settings = settings
