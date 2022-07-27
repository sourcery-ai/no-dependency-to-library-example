# Based on:
# https://requests.readthedocs.io/en/latest/user/advanced/#prepared-requests

from requests import *

s = Session()

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
req = Request("GET", url)
prepped = req.prepare()
resp = s.send(prepped)

print(resp.status_code)
