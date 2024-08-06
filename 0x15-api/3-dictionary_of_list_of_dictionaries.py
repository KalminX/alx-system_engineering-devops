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
    tasks_dict = {}

    TASK_URL = 'https://jsonplaceholder.typicode.com/todos/'
    USERS_URL = f'https://jsonplaceholder.typicode.com/users/'
    todo_json = requests.get(TASK_URL).json()
    users_json = requests.get(USERS_URL).json()

    for user in users_json:
        user_id = user['id']
        tasks_dict[user_id] = []
        user_tasks = [
            task for task in todo_json if task['userId'] == user_id
        ]
        for task in user_tasks:
            task_dict = {
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            }
            tasks_dict[user_id].append(task_dict)

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(tasks_dict, f)


if __name__ == '__main__':
    main()
