#!/usr/bin/python3
"""

The script gathers data from REST API. It takes in <employee_id>
as a parameter, and returns the data for the specific employee.
From the data received we export it to a JSON file.

The JSON file stores all the tasks owned by <this> employee.
"""
import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_api <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    try:
        """Get user information"""
        user_response = requests.get(
            "{}/users?id={}".format(base_url, employee_id))
        user_response.raise_for_status()
        user_info = user_response.json()[0]
        employee_name = user_info.get("name")
        employee_username = user_info.get("username")

        """Get todo list"""
        todo_response = requests.get(
            "{}/todos?userId={}".format(base_url, employee_id))
        todo_response.raise_for_status()
        todo_list = todo_response.json()

        """Extract completed tasks"""
        completed_tasks = [task for task in todo_list if task.get("completed")]
        num_completed_tasks = len(completed_tasks)
        total_num_tasks = len(todo_list)

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, num_completed_tasks, total_num_tasks))
        for task in completed_tasks:
            print(f"\t {task['title']}")

        """ exporting to a json file"""
        data = {}
        data[employee_id] = []
        for task in todo_list:
            data[employee_id].append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_username
            })
        filename = "{}.json".format(employee_id)
        with open(filename, "w") as outfile:
            json.dump(data, outfile)
    except requests.exceptions.HTTPError as error:
        print("Error: {}".format(error))
