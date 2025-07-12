#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    tasks = [{
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": user.get("username")
    } for task in todos]

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump({user_id: tasks}, jsonfile)
