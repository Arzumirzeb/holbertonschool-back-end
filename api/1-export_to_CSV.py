#!/usr/bin/python3

"""Export to CSV"""


import requests
import csv
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
