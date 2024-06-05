#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
from sys import argv


def get_employee():
    """returns information about his/her TODO list progress"""
    employee_id = argv[1]
    main_url = (
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(employee_id)
            )
    username = requests.get(main_url).json().get('username')
    tasks_url = (
            "https://jsonplaceholder.typicode.com/users/{}/todos"
            .format(employee_id)
            )
    tasks = requests.get(tasks_url).json()
    done_tasks = 0
    list_tasks = []
    json_filename = "{}.json".format(employee_id)
    for task in tasks:
        dic_tasks = {
                "task": task.get("title"),
                "completed": task["completed"],
                "username": username
                }
        list_tasks.append(dic_tasks)

    dic = {employee_id: list_tasks}
    with open(json_filename, "w") as f:
        json.dump(dic, f)


if __name__ == "__main__":
    get_employee()
