from datetime import datetime, timedelta

def calculate_streak(checkoffs, periodicity):
    if not checkoffs:
        return 0

    dates = sorted(datetime.strptime(d, "%Y-%m-%d") for d in checkoffs)
    streak = 1

    for i in range(len(dates)-1, 0, -1):
        delta = dates[i] - dates[i-1]

        if periodicity == "daily" and delta == timedelta(days=1):
            streak += 1
        elif periodicity == "weekly" and delta == timedelta(days=7):
            streak += 1
        else:
            break

    return streak
