from todo_operations import add_task, delete_task, view_tasks
from utils import clear_screen, read_input

def main():
    tasks = []

    while True:
        clear_screen()
        print("=== To-Do List Application ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = read_input("Select an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        
        elif choice == '2':
            task = read_input("Enter the task: ")
            add_task(tasks, task)
            print("Task added!")
        
        elif choice == '3':
            if not tasks:
                print("No tasks to delete.")
            else:
                try:
                    task_index = int(read_input("Enter the task number to delete: ")) - 1
                    deleted_task = delete_task(tasks, task_index)
                    if deleted_task:
                        print(f"Task '{deleted_task}' deleted!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        
        else:
            print("Invalid option! Please select a valid option.")

if __name__ == "__main__":
    main()