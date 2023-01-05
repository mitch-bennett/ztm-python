"""
passwordchecker

usage:
CLI to enter multiple passwords and check if they've been hacked
combat hackers using dict lookups

resources:
https://pypi.org/project/requests/
https://passwordsgenerator.net/sha1-hash-generator/
https://haveibeenpwned.com/Passwords

goal:
use pwned API to build own checker
learn about hashing - never store plain text!
k-anonymity: receive info about identity but not know actual identity
run SHA1 algo, only send first 5 chars, then check rest of hash locally

to do:
read passwords from text file instead of command line
"""

import requests
import hashlib
import sys


def request_api_data(query_char):
    # CBFDA is first 5 of SHA1 hash 'hello'
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fething: {res.status_code}, check the api and try again"
        )
    return res


# def read_res(response):
#     print(response.text)


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        # print(h, count) # list all matching tails and number of leaks
        if h == hash_to_check:
            return count
    return 0  # if no matches


def pwned_api_check(password):
    # # see what buildup of hash code does
    # # encode in utf-8 (unicode objects must be encoded before hashing), then generate hash object
    # # hash object is converted to hexidecimal output (string object of double length)
    # print(password.encode("utf-8"))
    # print(hashlib.sha1(password.encode("utf-8")))
    # print(hashlib.sha1(password.encode("utf-8")).hexdigest().upper())

    # Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(f"head: {first5_char}, tail: {tail}")
    # print(response)
    # return read_res(response)
    return get_password_leaks_count(response, tail)


def main(args):
    # add "with open(text file) as f: --loop through each line and grab pwd"
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f"{password} was found {count} times... you should probably change your password"
            )
        else:
            print(f"{password} was NOT found. Carry on!")
    return "done!"


if __name__ == "__main__":
    main(sys.argv[1:])

# request_api_data("123")
# pwned_api_check("123")
