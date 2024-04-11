#!/usr/bin/python3
"""unction that queries the Reddit API and returns the number of subscribers
e"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    """
    headers = {'User-Agent': 'Chrome'}
    response = requests.get(
            'https://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
