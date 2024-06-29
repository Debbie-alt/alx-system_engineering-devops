#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the top ten hot posts for a given subreddit.
If an invalid subreddit is given, the function should return None.
"""

import requests
from sys import argv


def top_ten(subreddit):
    """
    Returns the top ten posts for a given subreddit
    """
    user = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    response = requests.get(url, headers=user, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get('data', {}).get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Please provide a subreddit name.")
