
# The underscores in __init__ and other special methods signal to Python that these methods serve a predefined purpose
# and should be automatically triggered in certain situations (like object creation). 
# They’re part of Python's object-oriented programming magic!

class Task:
    def __init__(self, name):
        self.name = name
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "Done" if self.done else "Not Done"
        return f"{self.name} - {status}"
    
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)
        print(f"Task added: {task_name}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks created yet!")
        else: 
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        
    def mark_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_done()
            print(f"Task {task_index + 1} marked as done.")
        else:
            print("Invalid task number.")
        
    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Deleted task: {removed_task.name}")
        else:
            print("Invalid task number.")
    

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
    
        if choice == "1":
            task_name = input("Enter the task: ")
            todo_list.add_task(task_name)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            task_number = int(input("Enter task number to mark as done: ")) - 1
            todo_list.mark_done(task_number)
        elif choice == "4":
            todo_list.view_tasks()
            task_number = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(task_number)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()