#!/usr/bin/python3
"""This script to gather data from REST API."""
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

        """Get todo list"""
        todo_response = requests.get(
                             "{}/todos?userId={}".format(
                                base_url, employee_id
                                ))
        todo_response.raise_for_status()
        todo_list = todo_response.json()

        """Extract completed tasks"""
        completed_tasks = [task for task in todo_list if task.get("completed")]
        num_completed_tasks = len(completed_tasks)
        total_num_tasks = len(todo_list)

        print("Employee {} is done with tasks({}/{}):".format(
                         employee_name, num_completed_tasks, total_num_tasks))
        for task in completed_tasks:
            print("\t {}".format(task['title']))
    except requests.exceptions.HTTPError as error:
        print("Error: {}".format(error))
