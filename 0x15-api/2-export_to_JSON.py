#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username')

    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    json_data = {employee_id: []}
    for todo in todos_data:
        json_data[employee_id].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        })

    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file) 
