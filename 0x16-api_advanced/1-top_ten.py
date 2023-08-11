#!/usr/bin/python3
'''
Module 1-top_ten
print titles of the first top 10 hot posts listed for a subreddit
'''
import requests


def top_ten(subreddit):
    '''
    top ten posts of a subreddit
    '''
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {"User-Agent": "linux"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        print(None)
        return
    t_10 = r.json().get('data')
    t_10 = t_10.get('children')
    for t in t_10:
        print(t.get('data').get('title'))