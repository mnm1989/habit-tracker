import json
from typing import List
from habit import Habit


def load_habits(file_path: str) -> List[Habit]:
    """
    Load habits from a JSON file.

    :param file_path: Path to the JSON storage file
    :return: List of Habit objects
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Habit.from_dict(item) for item in data]
    except FileNotFoundError:
        return []


def save_habits(file_path: str, habits: List[Habit]) -> None:
    """
    Save habits to a JSON file.

    :param file_path: Path to the JSON storage file
    :param habits: List of Habit objects
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump([habit.to_dict() for habit in habits], file, indent=4)


