FILENAME = "tasks.txt"
def load_tasks():
    """Load tasks from the file."""
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    """Save tasks to the file."""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")
def display_menu():
    print("\nTask Management Application")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
def create_task(tasks):
    task = input("\nEnter the task to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")
def view_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("\nNo tasks found!")
def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_num - 1] = new_task
                save_tasks(tasks)
                print("Task updated successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
def main():
    tasks = load_tasks()  # Load tasks from the file when the program starts
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")        
        if choice == "1":
            create_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nExiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()
