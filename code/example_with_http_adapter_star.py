from requests.adapters import *


def print_adapter():
    adapter = HTTPAdapter()
    print(adapter)


print_adapter()
