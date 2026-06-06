import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

tasks = load_tasks()

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)

    elif choice == "2":
        for i, t in enumerate(tasks, start=1):
            status = "✓" if t["done"] else "✗"
            print(f"{i}. {t['task']} [{status}]")

    elif choice == "3":
        num = int(input("Task number: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            save_tasks(tasks)
        else:
            print("Invalid task number!")

    elif choice == "4":
        num = int(input("Task number: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            save_tasks(tasks)
        else:
            print("Invalid task number!")

    elif choice == "5":
        break

    else:
        print("Invalid choice!")