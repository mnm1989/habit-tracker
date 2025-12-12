from habit import Habit

def test_create_habit():
    habit = Habit("Read", "daily")

    assert habit.name == "Read"
    assert habit.periodicity == "daily"
    assert habit.checkoffs == []
    assert habit.created_at is not None
