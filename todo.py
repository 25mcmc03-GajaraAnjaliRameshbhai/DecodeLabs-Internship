# ==========================
# DecodeLabs Project 1
# To-Do List Manager
# ==========================

tasks = []


def add_task():
    title = input("\nEnter task: ").strip()

    if title == "":
        print("Task cannot be empty.")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== YOUR TASKS ==========")

    for i, task in enumerate(tasks, start=1):

        status = "✔" if task["completed"] else "✘"

        print(f"{i}. {task['title']} [{status}]")

    print("===============================")


def complete_task():

    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        num = int(input("\nEnter task number to mark complete: "))

        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Enter a valid number.")


def delete_task():

    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:

        num = int(input("\nEnter task number to delete: "))

        if 1 <= num <= len(tasks):

            removed = tasks.pop(num - 1)

            print(f"Deleted: {removed['title']}")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Enter a valid number.")


def search_task():

    keyword = input("\nEnter keyword: ").lower()

    found = False

    for i, task in enumerate(tasks, start=1):

        if keyword in task["title"].lower():

            status = "✔" if task["completed"] else "✘"

            print(f"{i}. {task['title']} [{status}]")

            found = True

    if not found:
        print("No matching task found.")


def statistics():

    total = len(tasks)

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    pending = total - completed

    print("\n===== TASK SUMMARY =====")
    print("Total Tasks     :", total)
    print("Completed Tasks :", completed)
    print("Pending Tasks   :", pending)


while True:

    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Task Summary")
    print("7. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        search_task()

    elif choice == "6":
        statistics()

    elif choice == "7":
        print("\nThank you for using To-Do List.")
        break

    else:
        print("Invalid choice.")
