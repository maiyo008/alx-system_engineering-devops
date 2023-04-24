#!/usr/bin/python3
"""Spreadsheet Column Printer

This script allows the user to print to the console all columns in the
spreadsheet. It is assumed that the first row of the spreadsheet is the
location of the columns.

This tool accepts comma separated value files (.csv) as well as excel
(.xls, .xlsx) files.

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the script
"""
import csv
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
            "{}/todos?userID={}".format(base_url, employee_id))
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

        """ exporting to a csv file"""
        with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todo_list:
                csvwriter.writerow([
                    employee_id,
                    employee_username,
                    task.get("completed"),
                    task.get("title")
                ])
    except requests.exceptions.HTTPError as error:
        print("Error: {}".format(error))
