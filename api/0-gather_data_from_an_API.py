#!/usr/bin/python3
'''gather information from the an api'''

import requests
import json
import sys


def api_get_name():
    """function to make the format and print the info"""

    id_user = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{id_user}"
    response = requests.get(url)
    get1 = response.content
    dict_get = json.loads(get1)

    url1 = f"https://jsonplaceholder.typicode.com/users/{id_user}/todos"
    response = requests.get(url1)
    dict_get1 = response.json()
    num_of_task = 0
    tasks = 0
    for i in dict_get1:
        tasks += 1
        if i["completed"]:
            num_of_task += 1

    print(
        f"Employee {dict_get['name']} is done with tasks({num_of_task}/{tasks}):")
    for i in dict_get1:
        if i["completed"]:
            print(f"     {i['title']}")


if __name__ == '__main__':
    api_get_name()
