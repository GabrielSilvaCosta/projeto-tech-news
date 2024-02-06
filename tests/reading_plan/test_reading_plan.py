from tech_news.analyzer.reading_plan import ReadingPlanService


def test_reading_plan_group_news():
    result = ReadingPlanService.group_news_for_available_time(10)
    assert result["readable"] == []
    assert result["unreadable"] == [
        ("Notícia 1", 1),
    ]

    result = ReadingPlanService.group_news_for_available_time(5)
    assert result["readable"] == [
        {"unfilled_time": 4, "chosen_news": [("Notícia 1", 1)]},
    ]
    assert result["unreadable"] == [
        ("Notícia 2", 2),
    ]

    result = ReadingPlanService.group_news_for_available_time(3)
    assert result["readable"] == [
        {"unfilled_time": 2, "chosen_news": [("Notícia 1", 1)]},
        {"unfilled_time": 1, "chosen_news": [("Notícia 2", 2)]},
    ]
    assert result["unreadable"] == [
        ("Notícia 3", 3),
    ]

    result = ReadingPlanService.group_news_for_available_time(1)
    assert result["readable"] == [
        {"unfilled_time": 0, "chosen_news": [("Notícia 1", 1)]},
        {"unfilled_time": 0, "chosen_news": [("Notícia 2", 2)]},
        {"unfilled_time": 0, "chosen_news": [("Notícia 3", 3)]},
    ]
    assert result["unreadable"] == []
