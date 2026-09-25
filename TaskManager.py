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
    input = input("Add a task: ")
    tasks.append(input)
    print("Task Added")
def view_tasks():
    for index, task in enumerate(tasks):
        print(f"{index}. {task}/n")
def delete_task(delete_task):
    for task in tasks:
        if delete_task == task:
            tasks.remove(task)
def search_task(certain_task)-> str:
    for task in tasks:
        if certain_task in task:
            return task
    return "Task not found"
tasks = []
while option != 9:
    menu()
