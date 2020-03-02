'''
    Example of how to use the standard library to perform
    an HTTP GET request.
'''
from urllib.request import urlopen

with urlopen("https://www.google.com") as internet:
    res = internet.read()

print(res)

