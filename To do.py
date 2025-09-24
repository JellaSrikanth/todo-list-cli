FILE_NAME = "todo.txt"   # file to store tasks
# function to load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            tasks = f.read().splitlines()   # split by line into list
    except FileNotFoundError:
        tasks = []   # if file not found start with empty list
    return tasks
# function to save tasks into file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            if tasks:   # if list not empty
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
            else:
                print("No tasks yet.")
        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task != "":
                tasks.append(task)
                save_tasks(tasks)
                print("Task added.")
        elif choice == "3":
            if tasks:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
                try:
                    num = int(input("Enter task number to remove: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        save_tasks(tasks)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Enter a valid number.")
            else:
                print("No tasks to remove.")
        elif choice == "4":
            print("Exiting... tasks saved.")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice, try again.")
if __name__ == "__main__":
    main()
