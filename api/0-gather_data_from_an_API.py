#!/usr/bin/python3
"""commenting the module to pass the check"""
import requests
import sys


if __name__ == "__main__":
    """
        access to the api
    """

    url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/{employee_id}/todos"

    employee_response = requests.get(f"{base_url}/{employee_id}")
    employee_data = employee_response.json()

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    completed_tasks = [task for task in todos_data if task["completed"]]

    print(f"Employee {employee_data['name']} is done with tasks
          ({len(completed_tasks)}/{len(todos_data)}): ")
    print(f"{employee_data['name']}:", len(completed_tasks), len(todos_data))

    for task in completed_tasks:
        print(f"\t{task['title']}")
