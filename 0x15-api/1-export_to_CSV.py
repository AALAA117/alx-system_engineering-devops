#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
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
    list_dtasks = []
    csv_filename = "{}.csv".format(employee_id)
    for task in tasks:
        if task["completed"]:
            done_tasks += 1
            list_dtasks.append(task)

    with open(csv_filename, "w") as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(employee_id, username,
                            task["completed"], task["title"])
                    )


if __name__ == "__main__":
    get_employee()
