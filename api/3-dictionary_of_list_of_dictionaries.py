#!/usr/bin/python3
"""Exports all employees' TODO list information to a JSON file."""

import json
import requests

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        )
        todos = requests.get(todos_url).json()

        user_tasks = []
        for task in todos:
            user_tasks.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        all_tasks[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
