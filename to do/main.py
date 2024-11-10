def main():
    tasks = []

    while True:
        print("\n=== To-Do List Application ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            if not tasks:
                print("No tasks available.")
            else:
                print("Your Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        
        elif choice == '2':
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added!")
        
        elif choice == '3':
            if not tasks:
                print("No tasks to delete.")
            else:
                try:
                    task_index = int(input("Enter the task number to delete: ")) - 1
                    if 0 <= task_index < len(tasks):
                        deleted_task = tasks.pop(task_index)
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