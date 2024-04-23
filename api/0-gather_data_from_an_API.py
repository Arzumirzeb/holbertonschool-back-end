#!/usr/bin/python3

"""Script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress"""


import requests
from sys import argv


def fetch_employee_todo_progress(employee_id):
    user_response = requests.get(f"https://jsonplaceholder.\
            typicode.com/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data['name']

    todos_response = requests.get(f"https://jsonplaceholder.\
            typicode.com/todos?userId={employee_id}")
    todos_data = todos_response.json()

    completed_tasks = []
    for task in todos_data:
        if task['completed']:
            completed_tasks.append(task)
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    print(f"Employee {employee_name} is done with tasks\
            ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")

    employee_id = argv[1]
    fetch_employee_todo_progress(employee_id)
