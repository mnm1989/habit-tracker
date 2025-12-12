
from datetime import datetime

class Habit:
    def __init__(
        self,
        name,
        periodicity,
        created_at=None,
        checkoffs=None
    ):
        self.name = name
        self.periodicity = periodicity
        self.created_at = created_at or datetime.now().isoformat(timespec="seconds")
        self.checkoffs = checkoffs or []

    def checkoff(self, date_str):
        if date_str not in self.checkoffs:
            self.checkoffs.append(date_str)
