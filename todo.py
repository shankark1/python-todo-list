tasks = []

def show_menu():
    print("\nTo-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(str(i) + ".", task)

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(str(i) + ".", task)

            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(removed, "removed.")
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid choice.")