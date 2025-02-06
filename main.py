from task_manager import TaskManager

if __name__ == "__main__":
   
    manager = TaskManager()

    
    user1 = manager.get_user("Sandra")

    while True:
        print("\n1. Create New Task")
        print("2. View All Tasks")
        print("3. Mark Completion Status")
        print("4. Delete Task")
        print("5. View Task Details")
        print("6. Filter Tasks")
        print("7. Exit App")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            user = manager.get_user(username)  
            title = input("Enter task title: ")
            time = input("Enter task time (e.g., '9 pm' or '7 am'): ")
            user.add_task(title, time)
            print(f"Task '{title}' added successfully for user '{username}'!")

        elif choice == "2":
            username = input("Enter username: ")
            user = manager.get_user(username)
            print(f"\nAll tasks for {user.username}:")
            user.display_tasks()

        elif choice == "3":
            username = input("Enter username: ")
            user = manager.get_user(username)
            title = input("Enter task title to mark as complete/incomplete: ")
            task = user.get_task(title)
            if task:
                status = input("Enter 'complete' to mark as completed or 'incomplete' to mark as incomplete: ")
                if status.lower() == "complete":
                    task.mark_complete()
                    print(f"Task '{title}' marked as completed.")
                elif status.lower() == "incomplete":
                    task.mark_incomplete()
                    print(f"Task '{title}' marked as incomplete.")
                else:
                    print("Invalid status.")
            else:
                print("Task not found!")

        elif choice == "4":
            username = input("Enter username: ")
            user = manager.get_user(username)
            title = input("Enter task title to delete: ")
            user.remove_task(title)
            print(f"Task '{title}' removed successfully for user '{username}'!")

        elif choice == "5":
            username = input("Enter username: ")
            user = manager.get_user(username)
            title = input("Enter task title to view details: ")
            task = user.get_task(title)
            if task:
                task.display()
            else:
                print("Task not found!")

        elif choice == "6":
            username = input("Enter username: ")
            user = manager.get_user(username)
            completed = input("Enter 'yes' to filter completed tasks, 'no' for incomplete tasks: ")
            if completed.lower() == "yes":
             filtered_tasks = user.filter_tasks()
            else:
                filtered_tasks = user.filter_tasks(False)
                
            if filtered_tasks:
                print("\nFiltered tasks:")
                for task in filtered_tasks:
                    task.display()
            else:
                print("No tasks found!")

        elif choice == "7":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

