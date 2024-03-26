#!/usr/bin/python3
"""Using REST API to access todo lists of employees"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    employeeId = argv[1]
    mainUrl = "https://jsonplaceholder.typicode.com/users"
    url = mainUrl + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dictionary = {employeeId: []}
    for task in tasks:
        dictionary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
            })
        with open('{}.json'.format(employeeId), 'w') as filename:
            json.dump(dictionary, filename)