from requests.adapters import HTTPAdapter


def print_adapter():
    adapter = HTTPAdapter()
    print(adapter)


print_adapter()
