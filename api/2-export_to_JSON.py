#!/usr/bin/python3

"""Export to JSON"""

import json
import requests
from sys import argv


def fetch_employee_todo_progress(employee_id):
    user_url = "https://jsonplaceholder.typicode.com/users/{}"\
               .format(employee_id)
    user = requests.get(user_url)
    user_data = user.json()
    employee_name = user_data['username']

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                .format(employee_id)
    todos = requests.get(todos_url)
    todos_data = todos.json()

    datas = []
    for task in todos_data:
        data = {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name
                }
        datas.append(data)

    tasks = {employee_id: datas}

    json_file = "{}.json".format(employee_id)
    with open(json_file, 'w') as jsonfile:
        json.dump(tasks, jsonfile)


if __name__ == "__main__":
    if len(argv) != 2:
        exit()

    employee_id = argv[1]
    fetch_employee_todo_progress(employee_id)
