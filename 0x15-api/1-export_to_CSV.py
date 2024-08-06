#!/usr/bin/python3
"""
This module fetches tasks for a given user from a placeholder API
and writes them to a CSV file.

Usage: python3 script_name.py USER_ID
"""

import requests
import csv
import sys

def main():
    """
    Main function to fetch tasks and write them to a CSV file.
    """
    user_id = sys.argv[1]
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

    file_name = 'USER_ID.csv'
    
    with open(file_name, mode='w', newline='') as f:
        f_writer = csv.writer(
            f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL
        )
        for task in user_tasks:
            f_writer.writerow([
                user_id, USERNAME, task['completed'], task['title']
            ])

if __name__ == '__main__':
    main()
