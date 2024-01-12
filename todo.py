def print_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_task(tasks):
    task = input("Enter task to add: ")
    tasks.append(task)

def remove_task(tasks):
    print_tasks(tasks)
    index = int(input("Enter the index of the task to remove: ")) - 1
    if index >= 0 and index < len(tasks):
        tasks.pop(index)
    else:
        print("Invalid index.")

def display_tasks(tasks):
    print_tasks(tasks)

def main():
    tasks = ["Wake-up Early", "Do Brush", "Eat Breakfast", "Going College"]

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Quit")

        option = input("Enter the number of your option: ")

        if option == "1":
            add_task(tasks)
        elif option == "2":
            remove_task(tasks)
        elif option == "3":
            display_tasks(tasks)
        elif option == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()