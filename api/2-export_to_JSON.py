#!/usr/bin/python3
'''api to convert to csv'''

import json
import requests
import sys


def api_get_name():
    """function to make the format and print the info"""

    EMPLOYEE_NAME = ""
    id_user = int(sys.argv[1])
    users = "https://jsonplaceholder.typicode.com/users"
    todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        id_user)
    response = requests.get(users).json()

    for i in response:
        if i["id"] == id_user:
            EMPLOYEE_NAME = i['username']

    TASK_CSV = []
    response1 = requests.get(todos).json()
    for j in response1:
        listing = {
            "task": j["title"],
            "completed": j["completed"],
            "username": EMPLOYEE_NAME}
        TASK_CSV.append(listing)

    final_dict = {str(id_user): TASK_CSV}

    namefile = "{}.json".format(id_user)
    with open(namefile, "w", newline='') as f:
        f.write(json.dumps(final_dict))


if __name__ == '__main__':
    api_get_name()
