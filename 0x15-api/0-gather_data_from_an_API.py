#!/usr/bin/python3
'''
A script that gathers employee name completed
tasks and total number of tasks from an API
'''
import requests
import sys

def get_employee_todo_progress(employee_id):
    # API endpoint for fetching user's TODO list
    api_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            todos = response.json()

            # Filter completed tasks
            completed_tasks = [todo['title'] for todo in todos if todo['completed']]

            # Display progress information
            print(f"Employee {todos[0]['userId']} {todos[0]['title']} is done with tasks"
                  f"({len(completed_tasks)}/{len(todos)}):")

            # Display titles of completed tasks
            for task in completed_tasks:
                print(f"\t{task}")

        else:
            # Display an error message if the request was not successful
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")

    except requests.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if the script is provided with an employee ID as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line argument
    employee_id = int(sys.argv[1])

    # Call the function with the provided employee ID
    get_employee_todo_progress(employee_id)

