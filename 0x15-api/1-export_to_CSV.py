#!/usr/bin/python3
"""Using REST API to export data in the CSV format of employees"""

import csv
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
    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(
                employeeId, employeeName, task.get(
                    'completed'), task.get('title')))
