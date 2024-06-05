#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
from sys import argv
import requests


def get_employee():
    """returns information about his/her TODO list progress"""
    employee_id = argv[1]
    main_url = (
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(employee_id)
            )
    employee_name = requests.get(main_url).json().get('name')
    tasks_url = (
            "https://jsonplaceholder.typicode.com/users/{}/todos"
            .format(employee_id)
            )
    tasks = requests.get(tasks_url).json()
    done_tasks = 0
    list_dtasks = []
    for task in tasks:
        if task["completed"]:
            done_tasks += 1
            list_dtasks.append(task)

    print("Employee {} is done with tasks({}/{})"
          .format(employee_name, done_tasks, len(tasks)))

    for task in list_dtasks:
        print("\t {}".format(task["title"]))


if __name__ == "__main__":
    get_employee()
