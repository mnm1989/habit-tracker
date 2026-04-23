from datetime import datetime
from typing import List


class Habit:
    """
    Represents a habit that can be tracked over time.
    """

    def __init__(self, name: str, periodicity: str):
        """
        Initialize a new habit.

        :param name: Name of the habit
        :param periodicity: Habit frequency (e.g. daily, weekly)
        """
        self.name: str = name
        self.periodicity: str = periodicity
        self.created_at: str = datetime.now().isoformat(timespec="seconds")
        self.checkoffs: List[str] = []

    def checkoff(self, date_str: str) -> None:
        """
        Mark the habit as completed on a given date.

        :param date_str: Date string (YYYY-MM-DD)
        """
        if date_str not in self.checkoffs:
            self.checkoffs.append(date_str)
class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now().isoformat(timespec="seconds")
        self.checkoffs = []

    def checkoff(self, date_str):
        if date_str not in self.checkoffs:
            self.checkoffs.append(date_str)

    @classmethod
    def from_dict(cls, data):
        habit = cls(data["name"], data["periodicity"])
        habit.created_at = data["created_at"]
        habit.checkoffs = data["checkoffs"]
        return habit