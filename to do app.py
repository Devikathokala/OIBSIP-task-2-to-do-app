# Define a dictionary to store tasks
tasks = []

def print_menu():
    print("\n---- To-Do List App ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    print("\n---- Tasks ----")
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{idx}. {task['task']} - {status}")

def mark_completed():
    view_tasks()
    task_number = int(input("Enter task number to mark as completed: "))
    tasks[task_number - 1]["completed"] = True
    print("Task marked as completed!")

def delete_task():
    view_tasks()
    task_number = int(input("Enter task number to delete: "))
    del tasks[task_number - 1]
    print("Task deleted!")

# Main program loop
while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
