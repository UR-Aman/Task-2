# todo.py

def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.")
    else:
        print("\n📝 Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter the task to add: ").strip()
    if task:
        tasks.append(task)
        print("✅ Task added.")
    else:
        print("⚠️ Empty task cannot be added.")

def remove_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            task_no = int(input("Enter the task number to remove: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"🗑️ Removed task: {removed}")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print("👋 Exiting To-Do List. Bye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
