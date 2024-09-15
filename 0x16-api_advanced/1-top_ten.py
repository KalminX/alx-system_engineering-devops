#!/usr/bin/python3
import requests
import json

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    subscribers = requests.get(url).json()
    print(json.dumps(subscribers['data']['subscribers'], indent=4))


number_of_subscribers("PYTHON")