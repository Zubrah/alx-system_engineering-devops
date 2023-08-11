#!/usr/bin/python3
'''
module 0-subs
query Reddit API and retun the number of subscribers
'''
import requests


def number_of_subscribers(subreddit):
    '''
    return number of subscribers on the Reddit API
    '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "linux"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        return 0
    sub = r.json().get('data').get('subscribers')
    return sub