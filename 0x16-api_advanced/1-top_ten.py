#!/usr/bin/python3
"""shebang line"""

import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit
    """
    headers = {'User-Agent': 'custom'}
    response = requests.get(
            f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10',
            headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    data = response.json()['data']['children']
    for post in data:
        print(post['data']['title'])
