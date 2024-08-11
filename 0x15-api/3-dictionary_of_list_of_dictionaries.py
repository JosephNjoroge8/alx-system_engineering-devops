#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    
    users_url = f"{base_url}/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    all_data = {}
    for user in users_data:
        user_id = str(user.get('id'))
        username = user.get('username')
        
        todos_url = f"{base_url}/todos?userId={user_id}"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
        
        user_tasks = []
        for todo in todos_data:
            user_tasks.append({
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            })
        
        all_data[user_id] = user_tasks

    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_data, json_file) 
