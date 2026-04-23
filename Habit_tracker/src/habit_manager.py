from typing import List
from habit import Habit
from storage import load_habits, save_habits


class HabitManager:
    """
    Manages creation, storage, and retrieval of habits.
    """

    def __init__(self, file_path: str):
        """
        Initialize the habit manager.

        :param file_path: Path to the JSON storage file
        """
        self.file_path: str = file_path
        self.habits: List[Habit] = load_habits(file_path)

    def add_habit(self, name: str, periodicity: str) -> Habit:
        """
        Create and store a new habit.

        :param name: Name of the habit
        :param periodicity: Habit frequency
        :return: The created Habit object
        """
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        save_habits(self.file_path, self.habits)
        return habit

    def get_habits(self) -> List[Habit]:
        """
        Retrieve all stored habits.

        :return: List of habits
        """
        return self.habits

