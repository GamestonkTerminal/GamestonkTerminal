import pytest

try:
    from bots.economy.futures_coms import futures_coms_command
except ImportError:
    pytest.skip(allow_module_level=True)


@pytest.mark.bots
@pytest.mark.vcr
def test_futures_coms_command(mocker, recorder):
    mocker.patch("bots.helpers.uuid_get", return_value="1")
    value = futures_coms_command()

    recorder.capture(value)
