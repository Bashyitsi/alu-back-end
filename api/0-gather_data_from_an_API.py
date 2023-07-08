#!/usr/bin/python3

import sys
import requests

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    user_url = f'{base_url}/users/{employee_id}'

    # Fetch user information
    response = requests.get(user_url)
    user_data = response.json()
    employee_name = user_data['name']

    # Fetch TODO list for the employee
    response = requests.get(todos_url)
    todos_data = response.json()

    # Calculate the number of completed tasks
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todos_data)

    # Display the employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_num_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide an employee ID.")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
