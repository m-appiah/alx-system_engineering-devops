#!/usr/bin/python3
""" Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    """

    headers = {'User-Agent': 'custom'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    if after:
        url += f'?after={after}'
        response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None
    data = response.json()['data']
    hot_list.extend([post['data']['title'] for post in data['children']])

    if data['after'] is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, data['after'])
