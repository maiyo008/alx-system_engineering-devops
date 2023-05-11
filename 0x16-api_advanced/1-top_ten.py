#!/usr/bin/python3
""" Top ten """
import requests


def top_ten(subreddit):
    """"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": 'Mozilla/5.0'}
    params = {'limit': 10}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
        )
    if response.status_code == 200:
        data = response.json()['data']
        for post in data['children']:
            print(post['data']['title'])
    else:
        print(None)
