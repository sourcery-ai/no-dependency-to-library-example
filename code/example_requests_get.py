import requests


def get_astronomy_picture():
    result = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    print(result)


get_astronomy_picture()
