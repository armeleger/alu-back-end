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
