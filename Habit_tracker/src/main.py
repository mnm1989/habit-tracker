from habit_manager import HabitManager
import analytics

manager = HabitManager("habits.json")

def show_menu():
    print("\n=== Habit Tracker ===")
    print("1) Add habit")
    print("2) List habits")
    print("3) Check off a habit")
    print("4) Show analytics")
    print("5) Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Habit name: ")
            per = input("Periodicity (daily/weekly): ")
            if manager.add_habit(name, per):
                print("Habit added!")
            else:
                print("Habit already exists.")

        elif choice == "2":
            habits = manager.list_habits()
            for h in habits:
                print(f"- {h.name} ({h.periodicity}), created {h.created_at}, checkoffs: {len(h.checkoffs)}")

        elif choice == "3":
            name = input("Habit name to check off: ")
            if manager.checkoff(name):
                print("Marked!")
            else:
                print("Habit not found.")

        elif choice == "4":
            habits = manager.list_habits()
            for h in habits:
                streak = analytics.calculate_streak(h.checkoffs, h.periodicity)
                print(f"{h.name}: streak = {streak}")

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
