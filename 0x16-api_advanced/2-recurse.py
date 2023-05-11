#!/usr/bin/python3
""" Recurse it"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    a recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
    """
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
        )
    if response.status_code != 200:
        return None
    data = response.json()['data']
    posts = data['children']
    for post in posts:
        hot_list.append(post['data']['title'])
    after = data['after']
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list
