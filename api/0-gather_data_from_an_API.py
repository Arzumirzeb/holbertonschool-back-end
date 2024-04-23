#!/usr/bin/python3

"""Script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress"""


import requests
from sys import argv


def fetch_employee_todo_progress(employee_id):
    user_url = "https://jsonplaceholder.typicode.com/users/{}"\
               .format(employee_id)
    user = requests.get(user_url)
    user_data = user.json()
    employee_name = user_data['name']

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                .format(employee_id)
    todos = requests.get(todos_url)
    todos_data = todos.json()

    completed_tasks = []
    for task in todos_data:
        if task['completed']:
            completed_tasks.append(task)
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")

    employee_id = argv[1]
    fetch_employee_todo_progress(employee_id)
