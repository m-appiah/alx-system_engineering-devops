#!/usr/bin/python3
"""Using REST API to access todo lists of employees"""

import requests
from sys import argv


if __name__ == '__main__':
    employeeId = argv[1]
    mainUrl = "https://jsonplaceholder.typicode.com/users"
    url = mainUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    completed = 0
    completed_tasks = []

    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):".format(
        employeeName, completed, len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
