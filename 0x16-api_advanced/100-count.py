#!/usr/bin/python3
"""recursive function that queries the Reddit API, parses the
title of all hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces. Javascript
should count as javascript, but java should not
"""
import requests
from collections import Counter
import re


def count_words(subreddit, word_list, counts=None, after=None):
    """recursive function that queries the Reddit API,"""
    if counts is None:
        counts = Counter(map(str.lower, word_list))
    headers = {'User-Agent': 'custom'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()['data']

    for post in data['children']:
        title = post['data']['title'].lower()
        words = re.findall(r'\b\w+\b', title)
        counts.update(word for word in words if word in counts)

    if data['after'] is None:
        for word, count in counts.most_common():
            print(f'{word}: {count}')
    else:
        count_words(subreddit, word_list, counts, data['after'])
