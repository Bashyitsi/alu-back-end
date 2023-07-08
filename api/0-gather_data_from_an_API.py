#!/usr/bin/python3
""" Calls an API in order to get completed tasks """
import requests
import sys


if __name__ == '__main__':
    userId = sys.argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/users/1/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users'
    todo = requests.get(url_todo, params={'userId': userId})
    user = requests.get(url_user, params={'id': userId})

    todo_dict_list = todo.json()
    user_dict_list = user.json()

    completed_tasks = []
    total_tasks = len(todo_dict_list)
    employee = user_dict_list[0].get('name')

    for task in todo_dict_list:
        if task['completed']:
            completed_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
