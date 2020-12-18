from requests import get
from hashlib import sha1
import sys

def request_api_data(query_data):
    ulr = 'https://api.pwnedpasswords.com/range/' + query_data
    print('Data sending ......')
    respond = get(ulr)
    print('Data received')
    if respond.status_code != 200:
        raise RuntimeError('Wrong query data. Hash function failed')
    print('Data processing')
    return respond


def pwned_api_check(passwor):
    # below coade hash my password
    hashed = sha1(passwor.encode('utf-8')).hexdigest().upper()

    print('Data Processing .......')

    # since we donr want to send our password's hash to the api we divide it to 2 section
    first_five, rest = hashed[:5], hashed[5:]
    #print(first_five)
    #print(rest)
    # send first six letters to get all the hash valuese and pwned count
    result = request_api_data(first_five).text.splitlines()  # by .text we convert the result to texts by .splitlines

    hash = (line.split(':') for line in result)
    for h, c in hash:
        if h == rest:
            return c

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} has been pwned {count} times. Better use another one')
        else:
            print(f'{password} password is safe')


main(sys.argv[1:])

