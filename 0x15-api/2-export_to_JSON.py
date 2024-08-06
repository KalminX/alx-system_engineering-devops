#!/usr/bin/python3
"""
Module to fetch and save tasks of a user in a JSON file.

This script fetches tasks for a specific user from the
JSONPlaceholder API and saves them to a JSON file.

Usage:
    python script_name.py USER_ID

Arguments:
    USER_ID - The ID of the user whose tasks are to be fetched.
"""

import json
import requests
import sys


def main():
    """Main function to fetch and save user tasks."""
    user_id = sys.argv[1]
    tasks_dict = {}
    tasks_dict[user_id] = []

    TASK_URL = 'https://jsonplaceholder.typicode.com/todos/'
    USER_URL = (
        f'https://jsonplaceholder.typicode.com/users/{user_id}'
    )

    todo_json = requests.get(TASK_URL).json()
    user_json = requests.get(USER_URL).json()

    USER_ID = int(user_id)
    USERNAME = user_json['username']
    user_tasks = [
        task for task in todo_json if task['userId'] == USER_ID
    ]

    for task in user_tasks:
        task_dict = {
            "task": task['title'],
            "completed": task['completed'],
            "username": USERNAME
        }
        tasks_dict[user_id].append(task_dict)

    filename = f'{user_id}.json'
    with open(filename, mode='w') as f:
        json.dump(tasks_dict, f)


if __name__ == '__main__':
    main()
