#!/usr/bin/python3
"""

Script is used to gather data from REST API. Once we have the data,
we export it to a JSON file, to record all users and the tasks 
assigned to them
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    filename = "todo_all_employees.json"
    try:
        """Get user information"""
        user_response = requests.get("{}/users".format(base_url))
        user_response.raise_for_status()
        user_info = user_response.json()

        """Getting tasks for every user"""
        for user in user_info:
            todo_response = requests.get(
                "{}/todos?userId={}".format(base_url, user.get("id"))
            )
            todo_response.raise_for_status()
            todo_list = todo_response.json()

            """exporting to a JSON file"""
            data = {}
            data[user.get("id")] = []
            for task in todo_list:
                data[user.get("id")].append({
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
            with open(filename, "a") as outfile:
                json.dump(data, outfile)
    except requests.exceptions.HTTPError as error:
        print("Error: {}".format(error))