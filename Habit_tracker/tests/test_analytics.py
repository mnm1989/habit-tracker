from analytics import calculate_streak


def test_daily_streak():
    checkoffs = [
        "2026-04-20",
        "2026-04-21",
        "2026-04-22"
    ]
    result = calculate_streak(checkoffs, "daily")
    assert result == 3


def test_weekly_streak():
    checkoffs = [
        "2026-04-01",
        "2026-04-08",
        "2026-04-15"
    ]
    result = calculate_streak(checkoffs, "weekly")
    assert result == 3