#!/usr/bin/python3
"""
 a recursive function that queries the Reddit API
 parses the title of all hot articles
 and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, counts={}):
    if after == "STOP":
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'My User Agent 1.0'}
    if after:
        url += f'&after={after}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            for word in word_list:
                if word.lower() in title.lower().split():
                    if word.lower() in counts:
                        counts[word.lower()] += 1
                    else:
                        counts[word.lower()] = 1
        after = data['data']['after']
        count_words(subreddit, word_list, hot_list, after, counts)
    elif response.status_code == 404:
        print(None)
