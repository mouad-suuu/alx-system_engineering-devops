#!/usr/bin/python3
"""
 a recursive function that queries the Reddit API
 and returns a list containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if after == "STOP":
        if len(hot_list) == 0:
            return None
        return hot_list
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'My User Agent 1.0'}
    if after:
        url += f'&after={after}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        return recurse(subreddit, hot_list, after)
    elif response.status_code == 404:
        return None
