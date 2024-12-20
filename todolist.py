
# The underscores in __init__ and other special methods signal to Python that these methods serve a predefined purpose
# and should be automatically triggered in certain situations (like object creation). 
# They’re part of Python's object-oriented programming magic!

import sqlite3

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
    def __init__(self, db_name="todo.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
        """)
        self.conn.commit()

    def add_task(self, task_name):
        self.cursor.execute("INSERT INTO tasks (name, done) VALUES (?, ?)", (task_name, 0))
        self.conn.commit()
        print(f"Task added: {task_name}")

    def view_tasks(self):
        self.cursor.execute("SELECT id, name, done FROM tasks")
        tasks = self.cursor.fetchall()
        if not tasks:
            print("No tasks created yet!")
        else:
            for task_id, name, done in tasks:
                status = "Done" if done else "Not Done"
                print(f"{task_id}. {name} - {status}")
        
    def mark_done(self, task_id):
        self.cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
        self.conn.commit()
        print(f"Task {task_id} marked as done.")
        
    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
        print(f"Deleted task with ID: {task_id}")
    
    def close_connection(self):
        self.conn.close()

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("\nChoose an option: ")
    
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