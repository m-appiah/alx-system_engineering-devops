#!/usr/bin/python3
"""unction that queries the Reddit API and returns the number of subscribers
e"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    """
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    response = requests.get(
            'https://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
