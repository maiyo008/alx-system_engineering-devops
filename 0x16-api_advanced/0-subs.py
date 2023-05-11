#!/usr/bin/python3
""" How many subs? """
import requests


def number_of_subscribers(subreddit):
    """
    A function that querries the redit api
    and returns number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
