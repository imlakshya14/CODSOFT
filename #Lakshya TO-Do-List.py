#TO-Do-List

tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("\n--- To-Do List ---")
        for idx, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx + 1}. [{status}] {task['task']}")
        print("------------------")
        # Function to mark a task as completed
def mark_completed():
    view_tasks()    
    task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def remove_task():
    view_tasks()
    task_index = int(input("Enter the number of the task to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Invalid task number.")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
