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
    i = 1
    main_url = "https://jsonplaceholder.typicode.com/users"
    data = requests.get(main_url).json()
    list_tasks = []
    dictionary = {}
    json_filename = "todo_all_employees.json"
    for a_dic in data:
        tasks_url = "https://jsonplaceholder.typicode.com/todos"
        tasks = requests.get(tasks_url).json()
        username = a_dic["username"]
        for task in tasks:
            user_id = task["userId"]
            if user_id == i:
                dic_tasks = {
                        "username": username,
                        "completed": task["completed"],
                        "task": task["title"]
                        }
                list_tasks.append(dic_tasks)
                dictionary[str(i)] = list_tasks
        i += 1

    with open(json_filename, "w") as f:
        json.dump(dictionary, f)


if __name__ == "__main__":
    get_employee()
