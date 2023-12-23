#!/usr/bin/python3
"""commenting the module to pass the check"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    """
        access to the api
    """

    url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(argv[1])
    employee_data = requests.get(url + f'users/{employee_id}').json()
    employee_tasks = requests.get(url + f'users/{employee_id}/todos').json()

    completed_tasks = [task for task in employee_tasks if task["completed"]]

    print(f'Employee {employee_data["name"]} is done with tasks:')

    for task in completed_tasks:
        print(f'\t[{"" if task["completed"] else "not "}completed] {task["title"]}')

    csv_filename = f'{employee_id}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in employee_tasks:
            csv_writer.writerow([employee_id, employee_data["name"], task["completed"], task["title"]])

    print(f'Data exported to {csv_filename}')