#!/usr/bin/python3
"""commenting the module to pass the check"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """function to acces the api"""
    base_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = f"{base_url}/{employee_id}/todos"

    try:
        employee_response = requests.get(f"{base_url}/{employee_id}")
        employee_data = employee_response.json()

        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task["completed"]]

        print(f"Employee {employee_data['name']} is done with tasks
              ({len(completed_tasks)}/{len(todos_data)}): ")
        print(f"{employee_data['name']}:", len(completed_tasks),
              len(todos_data))

        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
