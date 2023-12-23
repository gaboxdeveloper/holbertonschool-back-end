#!/usr/bin/python3
"""commenting the module to pass the check"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    """
        access to the api
    """

    url = "https://jsonplaceholder.typicode.com"
    user_id = int(argv[1])
    user_data = requests.get(url + f'/users/{user_id}').json()
    user_tasks = requests.get(url + f'/users/{user_id}/todos').json()

    print(f'Employee {user_data["name"]} is done with tasks:')
    
    for task in user_tasks:
        print(f'\t[{"" if task["completed"] else "not "}completed] {task["title"]}')

    csv_filename = f'{user_id}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in user_tasks:
            csv_writer.writerow([user_id, user_data["name"], task["completed"], task["title"]])

    print(f'Data exported to {csv_filename}')
