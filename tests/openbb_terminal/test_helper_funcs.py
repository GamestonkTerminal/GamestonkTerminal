# IMPORTATION STANDARD
from pathlib import Path

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.helper_funcs import (
    export_data,
    check_start_less_than_end,
    update_news_from_tweet_to_be_displayed,
)

# pylint: disable=E1101
# pylint: disable=W0603
# pylint: disable=E1111
# pylint: disable=W0621
# pylint: disable=W0613
# pylint: disable=R0912


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [
            ("User-Agent", None),
            ("Authorization", "MOCK_AUTHORIZATION"),
        ],
    }


@pytest.fixture
def mock_compose_export_path(monkeypatch, tmp_path):
    # files in tmp_dir will remain (in separate folders) for 3 sequential runs of pytest
    def mock_return(func_name, *args, **kwargs):
        return tmp_path / f"20220829_235959_{func_name}"

    monkeypatch.setattr("openbb_terminal.helper_funcs.compose_export_path", mock_return)


@pytest.mark.parametrize(
    "export_type, dir_path, func_name, df",
    [
        (
            "csv",
            "C:/openbb_terminal/common/behavioural_analysis",
            "queries",
            pd.DataFrame(),
        ),
        (
            "json",
            "C:/openbb_terminal/common/behavioural_analysis",
            "queries",
            pd.DataFrame(),
        ),
        (
            "xlsx",
            "C:/openbb_terminal/common/behavioural_analysis",
            "queries",
            pd.DataFrame(),
        ),
        (
            "png",
            "C:/openbb_terminal/common/behavioural_analysis",
            "queries",
            pd.DataFrame(),
        ),
        (
            "jpg",
            "C:/openbb_terminal/common/behavioural_analysis",
            "queries",
            pd.DataFrame(),
        ),
        (
            "pdf",
            "C:/openbb_terminal/common/behavioural_analysis",
            "queries",
            pd.DataFrame(),
        ),
        (
            "svg",
            "C:/openbb_terminal/common/behavioural_analysis",
            "queries",
            pd.DataFrame(),
        ),
    ],
)
def test_export_data_filetypes(
    mock_compose_export_path, export_type, dir_path, func_name, df, tmp_path
):
    export_data(export_type, dir_path, func_name, df)

    assert Path(tmp_path / f"20220829_235959_{func_name}.{export_type}").exists()
    # TODO add assertions to check the validity of the files?


@pytest.mark.parametrize(
    "export_type, dir_path, func_name, data",
    [
        (
            # Dict instead of DataFrame
            "csv",
            "C:/openbb_terminal/common/behavioural_analysis",
            "queries",
            dict({"test": "dict"}),
        ),
    ],
)
def test_export_data_invalid_data(
    mock_compose_export_path, export_type, dir_path, func_name, data
):
    with pytest.raises(AttributeError):
        assert export_data(export_type, dir_path, func_name, data)


def test_start_less_than_end():
    assert check_start_less_than_end("2022-01-01", "2022-01-02") is False
    assert check_start_less_than_end("2022-01-02", "2022-01-01") is True
    assert check_start_less_than_end("2022-01-01", "2022-01-01") is True
    assert check_start_less_than_end(None, "2022-01-01") is False
    assert check_start_less_than_end("2022-01-02", None) is False
    assert check_start_less_than_end(None, None) is False


@pytest.mark.vcr
def test_update_news_from_tweet_to_be_displayed(mocker, recorder):
    mocker.patch(
        target="openbb_terminal.helper_funcs.LAST_TWEET_NEWS_UPDATE_CHECK_TIME",
        new=None,
    )
    mocker.patch(
        target="openbb_terminal.helper_funcs.obbff.TOOLBAR_TWEET_NEWS_SECONDS_BETWEEN_UPDATES",
        new=300,
    )
    mocker.patch(
        target="openbb_terminal.helper_funcs.obbff.TOOLBAR_TWEET_NEWS_NUM_LAST_TWEETS_TO_READ",
        new=3,
    )
    mocker.patch(
        target="openbb_terminal.helper_funcs.obbff.TOOLBAR_TWEET_NEWS_KEYWORDS",
        new="BREAKING,JUST IN",
    )
    NEWS_TWEET = update_news_from_tweet_to_be_displayed()
    recorder.capture(NEWS_TWEET)
