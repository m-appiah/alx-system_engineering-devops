#!/usr/bin/python3
"""Using REST API to export data in the CSV format of employees"""

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
    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(
                employeeId, username, task.get(
                    'completed'), task.get('title')))
