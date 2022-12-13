#!/usr/bin/python3
'''gather information from the an api'''

import requests
import sys


def api_get_name():
    """function to make the format and print the info"""

    EMPLOYEE_NAME = ""
    id_user = int(sys.argv[1])
    users = "https://jsonplaceholder.typicode.com/users?id="
    todos = "https://jsonplaceholder.typicode.com/todos?userId="
    response = requests.get(users+sys.argv[1]).json()
    for i in response:
        if i["id"] == id_user:
            EMPLOYEE_NAME = i['name']
    TASK_TITLE = []

    response1 = requests.get(todos+sys.argv[1]).json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    for elem in response1:
        if elem["userId"] == id_user:
            TOTAL_NUMBER_OF_TASKS += 1
            if elem["completed"]:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(elem['title'])

    print(
        'Employee {} is done with tasks({}/{}):'
        .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for i in TASK_TITLE:
        print('\t {}'.format(i))


if __name__ == '__main__':
    api_get_name()