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
    employee_name = user_data['username']

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                .format(employee_id)
    todos = requests.get(todos_url)
    todos_data = todos.json()

    csv_file = "{}.csv".format(employee_id)
    with open(csv_file, 'w') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            csv_writer.writerow([employee_id, employee_name,
                                task['completed'], task['title']])


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")

    employee_id = argv[1]
    fetch_employee_todo_progress(employee_id)
