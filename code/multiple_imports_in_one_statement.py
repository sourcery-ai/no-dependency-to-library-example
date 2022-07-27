import json, requests as r


def get_astronomy_picture():
    result = r.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    print(result)


get_astronomy_picture()
