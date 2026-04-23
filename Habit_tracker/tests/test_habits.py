import pytest
import storage
from habit_manager import HabitManager


@pytest.fixture
def clean_storage(tmp_path, monkeypatch):
    test_file = tmp_path / "test_habits.json"
    monkeypatch.setattr(storage, "DATA_FILE", str(test_file))
    return test_file


def test_add_habit(clean_storage):
    manager = HabitManager()
    result = manager.add_habit("Reading", "daily")
    assert result is True
    assert len(manager.list_habits()) == 1


def test_duplicate_habit(clean_storage):
    manager = HabitManager()
    manager.add_habit("Reading", "daily")
    result = manager.add_habit("Reading", "daily")
    assert result is False


def test_checkoff(clean_storage):
    manager = HabitManager()
    manager.add_habit("Gym", "daily")
    result = manager.checkoff("Gym")
    assert result is True
    habit = manager.list_habits()[0]
    assert len(habit.checkoffs) == 1
