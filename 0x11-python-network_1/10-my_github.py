#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
   the header of the response.
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    result = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(result.json().get('id'))
