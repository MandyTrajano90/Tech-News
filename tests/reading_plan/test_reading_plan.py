from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest


def test_reading_plan_group_news(mocker):
    mocker.patch(
        'tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy',
        return_value=[
            {
                "title": "Notícia 1",
                "reading_time": 4,
            },
            {
                "title": "Notícia 2",
                "reading_time": 3,
            },
            {
                "title": "Notícia 3",
                "reading_time": 10,
            },
            {
                "title": "Notícia 4",
                "reading_time": 15,
            },
        ]
    )
 # Test invalid parameter
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-1)

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    # Test valid parameter
    result = ReadingPlanService.group_news_for_available_time(10)

    # Expected result
    expected_result = {
        "readable": [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    ("Notícia 1", 4),
                    ("Notícia 2", 3),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    ("Notícia 3", 10),
                ],
            },
        ],
        "unreadable": [
            ("Notícia 4", 15),
        ],
    }

    # Assert the result is as expected
    assert result == expected_result

    # Test another valid parameter with different grouping
    result = ReadingPlanService.group_news_for_available_time(7)

    # Expected result
    expected_result = {
        "readable": [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    ("Notícia 1", 4),
                ],
            },
            {
                "unfilled_time": 4,
                "chosen_news": [
                    ("Notícia 2", 3),
                ],
            },
        ],
        "unreadable": [
            ("Notícia 3", 10),
            ("Notícia 4", 15),
        ],
    }

    # Assert the result is as expected
    assert result == expected_result

    # Test all news unreadable scenario
    result = ReadingPlanService.group_news_for_available_time(2)

    # Expected result
    expected_result = {
        "readable": [],
        "unreadable": [
            ("Notícia 1", 4),
            ("Notícia 2", 3),
            ("Notícia 3", 10),
            ("Notícia 4", 15),
        ],
    }

    # Assert the result is as expected
    assert result == expected_result