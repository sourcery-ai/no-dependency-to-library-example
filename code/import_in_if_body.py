def placeholder(nr):
    if nr == 42:
        import requests
        result = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
        print(result)

placeholder(5)