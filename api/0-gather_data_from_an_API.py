#!/usr/bin/python3
"""
Program to gather data from an api
"""
import json
import requests
import sys


def get_todo_info():
    """Function to get the info from the api"""
    user_id = sys.argv[1]
    r = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                     .format(user_id))
    user = json.loads(r.text)
    user_name = user[0].get('name')

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(user_id))
    todos = json.loads(r.text)
    comp_tasks = 0
    comp_titles = []
    total_tasks = 0
    for task in todos:
        total_tasks += 1
        if task['completed'] is True:
            comp_tasks += 1
            comp_titles.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, comp_tasks, total_tasks))
    for title in comp_titles:
        print("\t {}".format(title))


if __name__ == "__main__":
    get_todo_info()
