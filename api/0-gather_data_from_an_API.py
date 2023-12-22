#!/usr/bin/python3
"""commenting the module to pass the check"""
import requests
from sys import argv


if __name__ == "__main__":
    """
        access to the api
    """

    url = "https://jsonplaceholder.typicode.com"
    user_id = int(argv[1])

    user_data = requests.get(url + f'/users/{user_id}').json()
    todos_data = requests.get(url + f'/users/{user_id}/todos').json()

    completed_tasks = [task for task in todos_data if task["completed"]]

    print(f'Employee {user_data["name"]} is done with ', end='')
    print(f'tasks({len(completed_tasks)}/{len(todos_data)}):')

    for task in completed_tasks:
        print('    ' + task["title"])
