import pytest

try:
    from bots.stocks.disc.toplosers import losers_command
except ImportError:
    pytest.skip(allow_module_level=True)


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("period1", "MOCK_PERIOD_1"),
            ("period2", "MOCK_PERIOD_2"),
            ("date", "MOCK_DATE"),
        ],
    }


@pytest.mark.bots
@pytest.mark.vcr
def test_losers_command(recorder):
    value = losers_command()
    value["imagefile"] = str(type(value["imagefile"]))

    recorder.capture(value)


@pytest.mark.bots
@pytest.mark.vcr
def test_losers_command_invalid():
    with pytest.raises(Exception):
        losers_command(-5)
