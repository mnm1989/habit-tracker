from datetime import date
from habit import Habit
import storage


class HabitManager:
    def __init__(self, file_path=None):
        if file_path is not None:
            storage.DATA_FILE = file_path
        self.habits = [Habit.from_dict(h) if isinstance(h, dict) else h for h in storage.load_habits()]

    def add_habit(self, name, periodicity):
        if any(h.name.lower() == name.lower() for h in self.habits):
            return False

        new_habit = Habit(name, periodicity)
        self.habits.append(new_habit)
        storage.save_habits([h.__dict__ for h in self.habits])
        return True

    def list_habits(self):
        return self.habits

    def checkoff(self, name):
        today = date.today().isoformat()
        for h in self.habits:
            if h.name.lower() == name.lower():
                h.checkoff(today)
                storage.save_habits([h.__dict__ for h in self.habits])
                return True
        return False