#!/usr/bin/python3
'''gather information from the an api'''

import json
import requests
import sys


def api_get_name():
    """function to make the format and print the info"""

    id_user = sys.argv[1]
    users = "https://jsonplaceholder.typicode.com/users/"
    url = "{}{}".format(users, id_user)
    response = requests.get(url)
    get1 = response.content
    dict_get = json.loads(get1)

    url1 = "{}{}/todos".format(users, id_user)
    response = requests.get(url1)
    dict_get1 = response.json()
    num_of_task = 0
    tasks = 0
    for i in dict_get1:
        tasks += 1
        if i["completed"]:
            num_of_task += 1

    print(
        "Employee {} is done with tasks({}/{}):"
        .format(dict_get['name'], num_of_task, tasks))
    for i in dict_get1:
        if i["completed"]:
            print("     {}".format(i['title']))


if __name__ == '__main__':
    api_get_name()
