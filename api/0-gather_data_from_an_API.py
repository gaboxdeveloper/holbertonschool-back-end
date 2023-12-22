#!/usr/bin/python3
"""commenting the module to pass the check"""
import requests
from sys import argv


if __name__ == "__main__":
    """
        access to the api
    """

    url = "https://jsonplaceholder.typicode.com"
    employee_id = int(argv[1])
    todos_url = f"{url}/{employee_id}/todos"

    employee_data = requests.get(f"{url}/users/{employee_id}").json()
    todos_data = requests.get(f"{url}/users/{employee_id}/todos").json()

    completed_tasks = [task for task in todos_data if task["completed"]]

    print(f"Employee {employee_data['name']} is done with tasks ({len(completed_tasks)}/{len(todos_data)}): ")
    print(f"{employee_data['name']}:", len(completed_tasks), len(todos_data))

    for task in completed_tasks:
        print(f"\t{task['title']}")
