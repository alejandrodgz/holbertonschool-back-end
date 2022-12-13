#!/usr/bin/python3
'''api to convert to csv'''

import csv
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
        listing = [j["userId"], EMPLOYEE_NAME, j["completed"], j['title']]
        TASK_CSV.append(listing)

    namefile = "{}.csv".format(id_user)
    with open(namefile, "w", newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(TASK_CSV)


if __name__ == '__main__':
    api_get_name()
