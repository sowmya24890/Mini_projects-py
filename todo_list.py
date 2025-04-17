# todo_list.py

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Save and Exit")

def load_tasks(filename):
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if not tasks:
                print("No tasks to show.")
            else:
                print("\nYour Tasks:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
        elif choice == "2":
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == "3":
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
            try:
                task_no = int(input("Enter task number to remove: "))
                if 1 <= task_no <= len(tasks):
                    tasks.pop(task_no - 1)
                    print("Task removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")
        elif choice == "4":
            save_tasks(tasks, filename)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()