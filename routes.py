from flask import Blueprint, jsonify, request
import sqlite3

# Create a Blueprint for tasks
tasks_bp = Blueprint('tasks', __name__)

def get_db_connection():
    conn = sqlite3.connect("todo.db")
    conn.row_factory = sqlite3.Row
    return conn

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return jsonify([dict(row) for row in tasks])

@tasks_bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    conn = get_db_connection()
    conn.execute("INSERT INTO tasks (name, done) VALUES (?, ?)", (data['name'], 0))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task added!"}), 201

@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET done = ? WHERE id = ?", (data['done'], task_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task updated!"})

@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task deleted!"})