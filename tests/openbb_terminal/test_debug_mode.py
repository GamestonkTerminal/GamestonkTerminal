import logging

import pytest

from openbb_terminal.config_terminal import change_debug_mode
from openbb_terminal.decorators import log_start_end

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def function_that_fails():
    raise ValueError("Failure")


def test_debug_false():
    change_debug_mode(False)
    function_that_fails()


def test_debug_true():
    change_debug_mode(True)
    with pytest.raises(ValueError):
        function_that_fails()
