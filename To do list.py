# TO-DO LIST APPLICATION

tasks = []

def show_menu():
    print("\n" + "=" * 50)
    print("           TO-DO LIST APPLICATION")
    print("=" * 50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
    print("=" * 50)

while True:
    show_menu()

    choice = input("Enter your choice (1-6): ")

    # Add Task
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append({"task": task, "status": "Pending"})
        print("✅ Task added successfully!")

    # View Tasks
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\n----- YOUR TASKS -----")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']} [{task['status']}]")

    # Update Task
    elif choice == "3":
        if not tasks:
            print("No tasks available to update.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")

            try:
                task_no = int(input("Enter task number to update: "))
                new_task = input("Enter updated task: ")

                tasks[task_no - 1]["task"] = new_task
                print("✅ Task updated successfully!")

            except:
                print("Invalid task number.")

    # Delete Task
    elif choice == "4":
        if not tasks:
            print("No tasks available to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")

            try:
                task_no = int(input("Enter task number to delete: "))
                removed = tasks.pop(task_no - 1)
                print(f"🗑️ Task '{removed['task']}' deleted successfully!")

            except:
                print("Invalid task number.")

    # Mark Completed
    elif choice == "5":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']} [{task['status']}]")

            try:
                task_no = int(input("Enter task number to mark completed: "))
                tasks[task_no - 1]["status"] = "Completed"
                print("✅ Task marked as completed!")

            except:
                print("Invalid task number.")

    # Exit
    elif choice == "6":
        print("\nThank you for using To-Do List Application!")
        break

    else:
        print("❌ Invalid choice. Please try again.")