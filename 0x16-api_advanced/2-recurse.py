#!/usr/bin/python3
"""
Using reddit's API
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']

            for post in posts:
                hot_list.append(post['data']['title'])
            if after:
                recurse(subreddit, hot_list, after)
            else:
                return hot_list if hot_list else None
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
