#!/usr/bin/python3
"""
Module to fetch and display completed tasks of an
employee from a JSONPlaceholder API.

This module uses the `requests` library to fetch user
and task data from JSONPlaceholder.
It then filters and displays the completed
tasks for a specified user.

Usage:
    python script_name.py <user_id>
"""

import requests
import sys


def main():
    """
    Main function to fetch and display completed
    tasks for a user.

    The user ID is taken from the command line arguments.
    It fetches user and task data from JSONPlaceholder,
    filters the completed tasks
    for the specified user, and prints them.
    """
    user_id = sys.argv[1]
    USER_URL = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    TASK_URL = 'https://jsonplaceholder.typicode.com/todos/'

    user_json = requests.get(USER_URL).json()
    todo_json = requests.get(TASK_URL).json()

    tasks_done = []
    EMPLOYEE_NAME = user_json['name']

    for task in todo_json:
        if task['completed'] and task['userId'] == int(user_id):
            TASK_TITLE = task['title']
            tasks_done.append(f'\t {TASK_TITLE}')

    NUMBER_OF_DONE_TASKS = len(tasks_done)
    TOTAL_NUMBER_OF_TASKS = 20
    tasks_string = '\n'.join(tasks_done)
    output = f'Employee {EMPLOYEE_NAME} is done with '
    output += f'\n{tasks_string}tasks'
    output += f'({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):'
    print(output)


if __name__ == '__main__':
    main()
