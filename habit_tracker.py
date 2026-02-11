import json
from datetime import datetime, timedelta

DATA_FILE = "habits.json"



def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}



def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)



def add_habit(data):
    name = input("Enter habit name: ").strip()

    if name in data:
        print("Habit already exists.")
    else:
        data[name] = {
            "last_completed": None,
            "streak": 0,
            "longest_streak": 0
        }
        save_data(data)
        print("Habit added successfully!")



def complete_habit(data):
    name = input("Enter habit name to mark complete: ").strip()

    if name not in data:
        print("Habit not found.")
        return

    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    last_completed = data[name]["last_completed"]

    if last_completed is None:
        data[name]["streak"] = 1

    else:
        last_completed_date = datetime.strptime(last_completed, "%Y-%m-%d").date()

        if last_completed_date == today:
            print("Already marked completed today.")
            return

        elif last_completed_date == yesterday:
            data[name]["streak"] += 1

        else:
            data[name]["streak"] = 1


    if data[name]["streak"] > data[name]["longest_streak"]:
        data[name]["longest_streak"] = data[name]["streak"]

    data[name]["last_completed"] = str(today)

    save_data(data)
    print("Habit marked as completed!")



def view_habits(data):
    if not data:
        print("No habits added yet.")
        return

    for name, details in data.items():
        print("\n--------------------")
        print(f"Habit: {name}")
        print(f"Current Streak: {details['streak']}")
        print(f"Longest Streak: {details['longest_streak']}")



def main():
    data = load_data()

    while True:
        print("\n===== Habit Tracker =====")
        print("1. Add Habit")
        print("2. Mark Habit as Completed Today")
        print("3. View Habits")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_habit(data)
        elif choice == "2":
            complete_habit(data)
        elif choice == "3":
            view_habits(data)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
