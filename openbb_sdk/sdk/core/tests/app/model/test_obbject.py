"""Tests for the OBBject class."""
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
from openbb_core.app.model.obbject import Chart, OBBject, OpenBBError
from openbb_provider.abstract.data import Data


def test_OBBject():
    """Smoke test."""
    co = OBBject()
    assert isinstance(co, OBBject)


def test_fields():
    """Smoke test."""
    fields = OBBject.__fields__.keys()

    assert "results" in fields
    assert "provider" in fields
    assert "warnings" in fields
    assert "chart" in fields


def test_to_dataframe_no_results():
    """Test helper."""
    co = OBBject()
    with pytest.raises(Exception):
        co.to_dataframe()


@pytest.mark.parametrize(
    "results, expected_df",
    [
        # Test case 1: Normal results with "date" column
        (
            [{"date": "2023-07-30", "value": 10}, {"date": "2023-07-31", "value": 20}],
            pd.DataFrame(
                [
                    {"date": "2023-07-30", "value": 10},
                    {"date": "2023-07-31", "value": 20},
                ],
            ),
        ),
        # Test case 2: Normal results without "date" column
        (
            [{"value": 10}, {"value": 20}],
            pd.DataFrame({"value": [10, 20]}, index=pd.RangeIndex(start=0, stop=2)),
        ),
        # Test case 3: List of Data
        (
            [
                Data(x=0, y=2),
                Data(x=1, y=3),
                Data(x=2, y=0),
                Data(x=3, y=1),
                Data(x=4, y=6),
            ],
            pd.DataFrame({"x": [0, 1, 2, 3, 4], "y": [2, 3, 0, 1, 6]}),
        ),
        # Test case 4: List of dict
        (
            [
                {"x": 1, "y": 2},
                {"x": 1, "y": 3},
                {"x": 2, "y": 0},
                {"x": 3, "y": 1},
                {"x": 4, "y": 6},
            ],
            pd.DataFrame({"x": [1, 1, 2, 3, 4], "y": [2, 3, 0, 1, 6]}),
        ),
        # Test case 5: List of Lists
        (
            [[0, 1], [1, 3], [2, 0], [3, 1], [4, 6]],
            pd.DataFrame([[0, 1], [1, 3], [2, 0], [3, 1], [4, 6]]),
        ),
        # Test case 6: List of Tuples
        (
            [(3, 2), (1, 3), (2, 0), (3, 1), (4, 6)],
            pd.DataFrame([(3, 2), (1, 3), (2, 0), (3, 1), (4, 6)]),
        ),
        # Test case 7: List of Strings
        (
            ["YOLO2", "YOLO3", "YOLO0", "YOLO1", "YOLO6"],
            pd.DataFrame(["YOLO2", "YOLO3", "YOLO0", "YOLO1", "YOLO6"]),
        ),
        # Test case 7: List of Numbers
        (
            [1, 0.42, 12321298, 129387129387192837, 0.000000123],
            pd.DataFrame([1, 0.42, 12321298, 129387129387192837, 0.000000123]),
        ),
        # Test case 7: Dict of Dicts
        (
            {
                "0": {"x": 0, "y": 2},
                "1": {"x": 1, "y": 3},
                "2": {"x": 2, "y": 0},
                "3": {"x": 3, "y": 1},
                "4": {"x": 4, "y": 6},
            },
            pd.DataFrame(
                {
                    "0": {"x": 0, "y": 2},
                    "1": {"x": 1, "y": 3},
                    "2": {"x": 2, "y": 0},
                    "3": {"x": 3, "y": 1},
                    "4": {"x": 4, "y": 6},
                },
            ),
        ),
        # Test case 8: Dict of Lists
        (
            {"0": [0, 2], "1": [1, 3], "2": [2, 0], "3": [3, 1], "4": [4, 6]},
            pd.DataFrame(
                {"0": [0, 2], "1": [1, 3], "2": [2, 0], "3": [3, 1], "4": [4, 6]}
            ),
        ),
        # Test case 9: List of dict of data
        (
            [
                {
                    "df1": [
                        Data(date="1956-01-01", another_date="2023-09-01", value=0.0),
                        Data(date="1956-02-01", another_date="2023-09-01", value=0.0),
                        Data(date="1956-03-01", another_date="2023-09-01", value=0.0),
                    ],
                    "df2": [
                        Data(date="1955-03-01", another_date="2023-09-01", value=0.0),
                        Data(date="1955-04-01", another_date="2023-09-01", value=0.0),
                        Data(date="1955-05-01", another_date="2023-09-01", value=0.0),
                    ],
                }
            ],
            pd.concat(
                {
                    "df1": pd.DataFrame(
                        {
                            "date": [
                                pd.to_datetime("1956-01-01"),
                                pd.to_datetime("1956-02-01"),
                                pd.to_datetime("1956-03-01"),
                            ],
                            "another_date": [
                                "2023-09-01",
                                "2023-09-01",
                                "2023-09-01",
                            ],
                            "value": [0.0, 0.0, 0.0],
                        }
                    ).set_index("date"),
                    "df2": pd.DataFrame(
                        {
                            "date": [
                                pd.to_datetime("1955-03-01"),
                                pd.to_datetime("1955-04-01"),
                                pd.to_datetime("1955-05-01"),
                            ],
                            "another_date": [
                                "2023-09-01",
                                "2023-09-01",
                                "2023-09-01",
                            ],
                            "value": [0.0, 0.0, 0.0],
                        }
                    ).set_index("date"),
                },
                axis=1,
            ),
        ),
        # Test case 10: Empty results
        ([], OpenBBError("Results not found.")),
        # Test case 11: Results as None, should raise OpenBBError
        (None, OpenBBError("Results not found.")),
    ],
)
def test_to_dataframe(results, expected_df):
    """Test helper."""
    # Arrange
    co = OBBject(results=results)

    # Act and Assert
    if isinstance(expected_df, pd.DataFrame):
        result = co.to_dataframe()
        assert result.equals(expected_df)
    else:
        with pytest.raises(expected_df.__class__) as exc_info:
            co.to_dataframe()

        assert str(exc_info.value) == str(expected_df)


@pytest.mark.parametrize(
    "results, expected",
    [
        # Test case 1: Normal results with "date" column
        (
            [{"date": "2023-07-30", "value": 10}, {"date": "2023-07-31", "value": 20}],
            {
                "date": [pd.to_datetime("2023-07-30"), pd.to_datetime("2023-07-31")],
                "value": [10, 20],
            },
        ),
        # Test case 2: Normal results without "date" column
        (
            [{"value": 10}, {"value": 20}],
            {
                "value": [10, 20],
            },
        ),
        # Test case 3: Empty results
        ([], OpenBBError("Results not found.")),
    ],
)
def test_to_dict(results, expected):
    """Test helper."""
    # Arrange
    if results:
        results = [Data(**d) for d in results]
    co = OBBject(results=results)

    # Act and Assert
    if isinstance(expected, Exception):
        with pytest.raises(expected.__class__) as exc_info:
            co.to_dict()

        assert str(exc_info.value) == str(expected)
    else:
        result = co.to_dict()
        result.pop("index", None)

        assert result == expected


@patch("openbb_core.app.model.obbject.OBBject.to_dataframe")
@patch("openbb_core.app.model.obbject.ChartingService")
def test_to_chart_with_new_chart(
    mock_charting_service,
    mock_to_dataframe,
):
    """Test helper."""

    def get_mock_dataframe():
        data = {
            "col1": [1, 2, 3],
            "col2": ["a", "b", "c"],
            "col3": [True, False, True],
        }

        return pd.DataFrame(data)

    # Arrange
    mock_instance = OBBject()
    mock_charting_service_instance = mock_charting_service.return_value
    mock_charting_service_instance.to_chart.return_value = Chart(
        content={"content": "some_new_content"}, fig={"fig": "some_mock_fig"}
    )
    mock_to_dataframe.return_value = get_mock_dataframe()

    # Act
    result = mock_instance.to_chart()

    # Assert
    assert result == {"fig": "some_mock_fig"}
    assert mock_instance.chart.content == {"content": "some_new_content"}

    # Ensure self.to_dataframe() was called
    mock_to_dataframe.assert_called_once()

    # Ensure ChartingService was called with the correct parameters
    mock_charting_service_instance.to_chart.assert_called_once()


def test_show_chart_exists():
    """Test helper."""
    mock_instance = OBBject()
    # Arrange
    mock_instance.chart = MagicMock(spec=Chart)
    mock_instance.chart.fig = MagicMock()
    mock_instance.chart.fig.show.return_value = MagicMock()

    # Act
    mock_instance.show()

    # Assert
    mock_instance.chart.fig.show.assert_called_once()


def test_show_chart_no_chart():
    """Test helper."""
    mock_instance = OBBject()

    # Act and Assert
    with pytest.raises(OpenBBError, match="Chart not found."):
        mock_instance.show()


def test_show_chart_no_fig():
    """Test helper."""
    mock_instance = OBBject()
    # Arrange
    mock_instance.chart = Chart()

    # Act and Assert
    with pytest.raises(OpenBBError, match="Chart not found."):
        mock_instance.show()
