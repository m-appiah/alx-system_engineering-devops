#!/usr/bin/python3
"""shebang line"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    """
    headers = {'User-Agent': 'custom'}
    response = requests.get(
            f'https://www.reddit.com/r/{subreddit}/about.json',
            headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
