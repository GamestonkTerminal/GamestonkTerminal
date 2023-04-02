# IMPORTATION STANDARD

import os

import pandas as pd

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.core.session.current_user import PreferencesModel, copy_user
from openbb_terminal.economy.quantitative_analysis import qa_controller

# pylint: disable=E1101
# pylint: disable=W0603
# pylint: disable=E1111
# pylint: disable=C0302

MOCK_CPI = pd.DataFrame.from_dict(
    {
        "date": {
            0: "1947-01-01",
            1: "1947-02-01",
            2: "1947-03-01",
            3: "1947-04-01",
        },
        "CPI": {
            0: 21.48,
            1: 21.62,
            2: 22.0,
            3: 22.0,
        },
    }
)

MOCK_OBJ = {}
MOCK_OBJ["united_states_CPI"] = MOCK_CPI


@pytest.mark.parametrize(
    "queue, expected",
    [
        (["load", "help"], ["help"]),
        (["quit", "help"], ["help"]),
    ],
)
def test_menu_with_queue(expected, mocker, queue):
    path_controller = "openbb_terminal.economy.quantitative_analysis.qa_controller"

    # MOCK SWITCH
    mocker.patch(
        target=f"{path_controller}.QaController.switch",
        return_value=["quit"],
    )
    result_menu = qa_controller.QaController(
        all_economy_data=MOCK_OBJ,
        queue=queue,
    ).menu()

    assert result_menu == expected


def test_menu_without_queue_completion(mocker):
    # ENABLE AUTO-COMPLETION : HELPER_FUNCS.MENU
    preferences = PreferencesModel(USE_PROMPT_TOOLKIT=True)
    mock_current_user = copy_user(preferences=preferences)
    mocker.patch(
        target="openbb_terminal.core.session.current_user.__current_user",
        new=mock_current_user,
    )

    mocker.patch(
        target="openbb_terminal.parent_classes.session",
    )
    mocker.patch(
        target="openbb_terminal.parent_classes.session.prompt",
        return_value="quit",
    )

    # DISABLE AUTO-COMPLETION : CONTROLLER.COMPLETER
    mocker.patch(
        target="openbb_terminal.economy.economy_controller.session",
    )
    mocker.patch(
        target="openbb_terminal.economy.economy_controller.session.prompt",
        return_value="quit",
    )

    result_menu = qa_controller.QaController(
        all_economy_data=MOCK_OBJ,
        queue=None,
    ).menu()

    assert result_menu == ["help"]


@pytest.mark.parametrize(
    "mock_input",
    ["help", "homee help", "home help", "mock"],
)
def test_menu_without_queue_sys_exit(mock_input, mocker):
    path_controller = "openbb_terminal.economy.quantitative_analysis.qa_controller"

    # DISABLE AUTO-COMPLETION
    preferences = PreferencesModel(USE_PROMPT_TOOLKIT=True)
    mock_current_user = copy_user(preferences=preferences)
    mocker.patch(
        target="openbb_terminal.core.session.current_user.__current_user",
        new=mock_current_user,
    )
    mocker.patch(
        target=f"{path_controller}.session",
        return_value=None,
    )

    # MOCK USER INPUT
    mocker.patch("builtins.input", return_value=mock_input)

    # MOCK SWITCH
    class SystemExitSideEffect:
        def __init__(self):
            self.first_call = True

        def __call__(self, *args, **kwargs):
            if self.first_call:
                self.first_call = False
                raise SystemExit()
            return ["quit"]

    mock_switch = mocker.Mock(side_effect=SystemExitSideEffect())
    mocker.patch(
        target=f"{path_controller}.QaController.switch",
        new=mock_switch,
    )

    result_menu = qa_controller.QaController(
        all_economy_data=MOCK_OBJ,
        queue=None,
    ).menu()

    assert result_menu == ["help"]


@pytest.mark.record_verify_screen
def test_print_help():
    controller = qa_controller.QaController(all_economy_data=MOCK_OBJ, queue=None)
    controller.print_help()


@pytest.mark.parametrize(
    "an_input, expected_queue",
    [
        ("", []),
        ("/help", ["home", "help"]),
        ("help/help", ["help", "help"]),
        ("q", ["quit"]),
        ("h", []),
        (
            "r",
            [
                "quit",
                "quit",
                "reset",
                "economy",
            ],
        ),
    ],
)
def test_switch(an_input, expected_queue):
    controller = qa_controller.QaController(all_economy_data=MOCK_OBJ, queue=None)
    queue = controller.switch(an_input=an_input)

    assert queue == expected_queue


@pytest.mark.vcr(record_mode="none")
def test_call_cls(mocker):
    mocker.patch("os.system")

    controller = qa_controller.QaController(all_economy_data=MOCK_OBJ, queue=None)
    controller.call_cls([])

    assert controller.queue == []
    os.system.assert_called_once_with("cls||clear")


@pytest.mark.parametrize(
    "func, queue, expected_queue",
    [
        (
            "call_exit",
            [],
            ["quit", "quit", "quit"],
        ),
        ("call_exit", ["help"], ["quit", "quit", "quit", "help"]),
        ("call_home", [], ["quit", "quit"]),
        ("call_help", [], []),
        ("call_quit", [], ["quit"]),
        ("call_quit", ["help"], ["quit", "help"]),
        (
            "call_reset",
            [],
            [
                "quit",
                "quit",
                "reset",
                "economy",
            ],
        ),
        (
            "call_reset",
            ["help"],
            [
                "quit",
                "quit",
                "reset",
                "economy",
                "help",
            ],
        ),
    ],
)
def test_call_func_expect_queue(expected_queue, func, queue):
    controller = qa_controller.QaController(all_economy_data=MOCK_OBJ, queue=queue)
    result = getattr(controller, func)([])

    assert result is None
    assert controller.queue == expected_queue
