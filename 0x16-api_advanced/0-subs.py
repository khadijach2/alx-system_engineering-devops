#!/usr/bin/python3
"""Module that consumes the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers (not
    active users, total subscribers) for a given subreddit.

    If not a valid subreddit, return 0.
    Invalid subreddits may return a redirect to search results. Ensure that
    you are not following redirects.

    Args:
        subreddit (str): subreddit

    Returns:
        int: number of subscribers
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
        return results.get("subscribers")
