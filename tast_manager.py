from datetime import datetime
import json

tasks = []



def load_task_manager():
    global tasks
    try:
        with open("task_manager.json", "r") as f:
            tasks = json.load(f)
        print("Task manager loaded successfully.")
    except FileNotFoundError:
        tasks = []
        
def save_task_manager():
    with open("task_manager.json", "w") as f:
        json.dump(tasks, f)
    print("Task manager saved successfully!")
    
def add_task():
    task_name = input("Which task would you like to add? ")
    task_description = input("Additional information: ")
    due_date = input("When is this task due? (YYYY-MM-DD) ")
    task_status = "pending"
    tasks.append({'Title': task_name,
                  'Description': task_description,
                  'Due Date': due_date,
                  "Status": task_status
        })
    
def view_tasks():
    if not tasks:
        print("No tasks currently stored.")
        return
    
    tasks.sort(key=lambda task: datetime.strptime(task["Due Date"], "%Y-%m-%d"))
    
    print("=== Tasks ===")
    
    for index, task in enumerate(tasks, start = 1):
        today = datetime.today().date()
        task_due = datetime.strptime(task["Due Date"], "%Y-%m-%d").date()
        if task_due < today and task['Status'] == "pending":
            status_display = 'OVERDUE'
        else:
            status_display = task['Status']
        print(f"""{index}.{task['Title']}
Description: {task['Description']}
Due Date: {task['Due Date']}
Status: {status_display}
""")

def complete_task():
    if not tasks:
        print("No tasks currently stored.")
        return
    
    view_tasks()
    try:
         choice = int(input("Which task would you like to complete? "))
         index = choice - 1
         
         if 0 <= index < len(tasks):
             tasks[index]['Status'] = 'completed'
             print(f"Task Complete: {tasks[index]['Title']} {tasks[index]['Status']}.")
       
         else:
            print("Invalid selection. Please try again")
             
    except ValueError:
        print("Please select a valid number.")
        
def remove_task():
    if not tasks:
        print("No tasks currently stored.")
        return
    
    view_tasks()
    try:
         choice = int(input("Which task would you like to remove? "))
         index = choice - 1
         
         if 0<= index < len(tasks):
             removed = tasks.pop(index)
             print(f"{removed['Title']} removed.")
         else:
             print("Invalid selection. Please try again")
          
    except ValueError:
        print("Please select a valid number.")    
        
        
def task_manager():
    while True:
        print("""
              === Main Menu ===
              1. Add Task
              2. View Tasks
              3. Complete Task
              4. Remove Task
              5.Exit
              """)
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print('Goodbye!')
            break
        else:
            print('Invalid. Please try again.')
            
            
load_task_manager()

task_manager()

save_task_manager()

        