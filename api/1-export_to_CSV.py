#!/usr/bin/python3
""" Call API and store data in CSV """
import csv
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    todo = requests.get(url_todo, params={'userId': employee_id})
    user = requests.get(url_user, params={'id': employee_id})

    todo_dict_list = todo.json()
    user_dict_list = user.json()

    employee = user_dict_list[0].get('username')

    with open("{}.csv".format(employee_id), "a+") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_dict_list:
            status = task['completed']
            title = task['title']
            csvwriter.writerow(["{}".format(employee_id),
                                "{}".format(employee),
                                "{}".format(status),
                                "{}".format(title)])
