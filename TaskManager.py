def menu() -> int:
    option = 0
    print("====== TASK MANAGER ====== \n " \
    "1. Add Task \n"\
    "2. View Tasks \n"\
    "3. Search Tasks \n"\
    "4. Complete Task \n" \
    "5. Delete Task \n"\
    "6. View Priority Queue \n" \
    "7. Sort Tasks \n" \
    "8. Find Task \n"\
    "9. Exit \n")
    try:
        option = int(input("Please select an option: "))
    except ValueError:
        print("Please input a number!")
    return option 
def add_task():
    added_task = str(input("Add a task: "))
    tasks.append(added_task)
    print("Task Added")
def view_tasks():
    for index, task in enumerate(tasks):
        print(f"{index}. {task}")
def delete_task(delete_task):
    for index,task in enumerate(tasks):
        if index == delete_task:
            tasks.remove(task)
def search_task(certain_task)-> str:
    upper_certain_task = certain_task.upper()
    for task in tasks:
        if certain_task in task:
            return task
    return "Task not found"
def tasks_to_caps():
    upper_tasks = []
    for task in tasks:
        upper_tasks.append(task.upper())
    return upper_tasks
tasks = []
option = menu()
while option != 9:
    if option == 1:
        add_task()
    if option == 2:
        view_tasks()
    if option == 3:
        print(search_task(input("Search task: ")))
    if option == 4:
        deleted_task = input("Completed task number: ")
        delete_task(deleted_task)
    option = menu()
