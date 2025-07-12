#!/usr/bin/python3
import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Get all users
    users = requests.get(users_url).json()

    # Get all todos
    todos = requests.get(todos_url).json()

    # Create dictionary to store data
    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Filter todos for the current user
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user_id
        ]

        all_data[user_id] = user_tasks

    # Export to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)
"""Script to use a REST API, returns information about
all tasks from all employees and export in JSON"""
import json
import requests


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{API_URL}/users").json()

    dict_users_tasks = {}
    for user in users:
        tasks = requests.get(f"{API_URL}/users/{user['id']}/todos").json()

        dict_users_tasks[user["id"]] = []
        for task in tasks:
            task_dict = {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            dict_users_tasks[user["id"]].append(task_dict)

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict_users_tasks, file)

