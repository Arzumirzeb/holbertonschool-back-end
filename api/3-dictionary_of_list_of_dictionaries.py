#!/usr/bin/python3

"""Dictionary of list of dictionaries"""

import json
import requests


def fetch_employee_todo_progress():
    all_tasks = {}

    user_url = "https://jsonplaceholder.typicode.com/users/"
    user = requests.get(user_url)
    user_data = user.json()

    for user in user_data:
        user_id = user['id']
        employee_name = user['username']
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                    .format(user_id)
        todos = requests.get(todos_url)
        todos_data = todos.json()

        datas = []
        for task in todos_data:
            data = {
                    "username": employee_name,
                    "task": task['title'],
                    "completed": task['completed']
                    }
            datas.append(data)
        all_tasks[user_id] = datas

    json_file = "todo_all_employees.json"
    with open(json_file, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    fetch_employee_todo_progress()
