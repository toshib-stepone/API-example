import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, description):
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"Added: {description}")


def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked done: {tasks[index]['description']}")
    else:
        print("Invalid task number.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks):
        status = "x" if task["done"] else " "
        print(f"[{status}] {i}: {task['description']}")


def main():
    tasks = load_tasks()
    while True:
        print("\n1. List tasks\n2. Add task\n3. Complete task\n4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            desc = input("Task description: ").strip()
            add_task(tasks, desc)
        elif choice == "3":
            list_tasks(tasks)
            try:
                idx = int(input("Task number to complete: "))
                complete_task(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()