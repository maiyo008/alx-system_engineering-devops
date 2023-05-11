#!/usr/bin/python3
""" Count it """

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    if after is not None:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()['data']
        posts = data['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title\
                and not any(char.isalpha()\
                for char in title.split(word.lower())[0][-1:]):
                    counts[word] = counts.get(word, 0) + title.count(word.lower())
        after = data['after']
        if after is not None:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))
    elif response.status_code == 404:
        print("Subreddit '{}' not found.".format(subreddit))
    else:
        print("An error occurred.")
