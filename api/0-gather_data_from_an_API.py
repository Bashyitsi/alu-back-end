#!/usr/bin/python3

import requests
import sys


def get_employee_todo_progress(employee_id):
    # Make a GET request to the API endpoint to retrieve employee details
    employee_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )

    # Check if the request was successful (status code 200)
    if employee_response.status_code == 200:
        employee_data = employee_response.json()  # Convert the response to JSON

        # Fetch the employee name
        emp_name = employee_data["name"]

        # Make a GET request to retrieve the TODO list for the employee
        todos_response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        )

        # Check if the request was successful (status code 200)
        if todos_response.status_code == 200:
            todos = todos_response.json()  # Convert the response to JSON

            # Filter the completed tasks for the employee
            comp_tasks = [todo["title"] for todo in todos if todo["completed"]]

            # Display the employee TODO list progress
            print(
                f"Employee {emp_name} is done with tasks"
                f"({len(comp_tasks)}/{len(todos)}):"
            )
            for task in comp_tasks:
                print(f"\t{task.expandtabs(4)}")  # Use expandtabs() for consistent tabulation
        else:
            print(f"Error: Failed  for employee" f" {employee_id}")
    else:
        print(f"Error: Failed  for employee" f"{employee_id}")


if __name__ == "__main__":
    # Check if the employee ID is provided as a command line argument
    if len(sys.argv) < 2:
        print("Please provide an employee ID as a command line argument")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
