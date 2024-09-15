#!/usr/bin/python3
import requests
import json
import sys


def number_of_subscribers(subreddit):
    """
        A function that returns the number of subscribers in a subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    try:
        subscribers = requests.get(url).json()
        return subscribers['data']['subscribers']
    except:
        return 0
