#!/usr/bin/python3
"""this is the final task
we need to create a dict with every user
"""

import json
import requests


def get_user():
    base_url = "https://jsonplaceholder.typicode.com/users/"

    dict_user = requests.get(base_url).json()

    final_dict = {}

    for i in dict_user:
        dict_todos = requests.get("{}{}/todos"
                                  .format(base_url, str(i["id"]))).json()
        list_task = []
        for j in dict_todos:
            listing = {"username": i["username"],
                       "task": j["title"], "completed": j["completed"]}
            list_task.append(listing)
        final_dict[str(i["id"])] = list_task

    with open("todo_all_employees.json", mode="w") as f:
        f.write(json.dumps(final_dict))


if __name__ == "__main__":
    get_user()
