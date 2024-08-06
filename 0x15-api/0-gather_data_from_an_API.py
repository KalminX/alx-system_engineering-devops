#!/usr/bin/python3
import requests
import json, pprint
import sys

def main():
    user_id = sys.argv[1]
    USER_URL = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    TASK_URL = f'https://jsonplaceholder.typicode.com/todos/'
    user_json = requests.get(USER_URL).json()
    todo_json = requests.get(TASK_URL).json()
    # print(todo_json)
    EMPLOYEE_NAME = user_json['name']
    TASKS_DONE = []
    for task in todo_json:
        if task['completed'] == True and task['userId'] == int(user_id):
            title = task['title']
            TASKS_DONE.append(f'\t {title}')
    TASKS_STRING = '\n'.join(TASKS_DONE)
    head = f'Employee {EMPLOYEE_NAME} is done with tasks({len(TASKS_DONE)}/20):\n{TASKS_STRING}'
    print(head)
    
    # Concantenate the list into a string '\n'
    
    
    pass


if __name__=='__main__':
    main()
