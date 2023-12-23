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
    user_task = requests.get(url + f'/users/{user_id}/todos').json()

    completed_tasks = [task for task in user_task if task["completed"]]

    print(f'Employee {user_data["name"]} is done with ', end='')
    print(f'tasks({len(completed_tasks)}/{len(user_task)}):')

    for task in completed_tasks:
        print('\t' + task["title"])

    # Export data to CSV
    csv_filename = f'{user_id}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in user_task:
            csv_writer.writerow([user_id, user_data["name"], task["completed"], task["title"]])

    print(f'Data exported to {csv_filename}')
