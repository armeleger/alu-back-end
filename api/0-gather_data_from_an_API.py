#!/usr/bin/python3

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    
    try:

        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name', 'Unknown')

        todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
        todos_response.raise_for_status()
        todos_data = todos_response.json()
        
        total_tasks = len(todos_data)
        completed_tasks = [todo for todo in todos_data if todo.get('completed', False)]
        done_tasks = len(completed_tasks)
        
        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        
        for task in completed_tasks:
            task_title = task.get('title', 'No title')
            print(f"\t {task_title}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyError as e:
        print(f"Error parsing data: missing key {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>", file=sys.stderr)
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer", file=sys.stderr)
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)