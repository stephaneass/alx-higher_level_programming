#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
   the header of the response.
"""


if __name__ == "__main__":
    from requests import get

    result = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type: {}".format(result.text.__class__))
    print("\t- content: {}".format(result.text))
