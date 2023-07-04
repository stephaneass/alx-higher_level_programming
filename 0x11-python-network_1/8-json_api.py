#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
   the header of the response.
"""


if __name__ == "__main__":
    from requests import post
    from sys import argv

    param = argv[1] if len(argv) > 1 else ""
    result = post('http://0.0.0.0:5000/search_user', data={'q': param})
    try:
        response = result.json()
        if response == {}:
            print('No result')
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print('Not a valid JSON')
