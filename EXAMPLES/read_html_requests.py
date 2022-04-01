#!/usr/bin/env python
import requests

response = requests.get(
    "https://www.python.org",
    # proxies={'https': {'www.freddiemac.gov:1010'},
    # auth=('myname', 'l0lz'),
    # cookies = {'c1': 'spam', 'c2': 'ham'}
    # ...
)  # <1>
if response.status_code == requests.codes.OK:
    for header, value in sorted(response.headers.items()): # <2>
        print("{:20.20s} {}".format(header, value))
    print()

    print(response.text[:200])   # <3>
    print('...')
    print(response.text[-200:])   # <4>
