import hashlib

from requests import get
#from hashlib sha1

def request_api_data (query_data):

    ulr = 'https://api.pwnedpasswords.com/range/' + query_data
    respond = get(ulr)
    print('Data received')
    if respond.status_code != 200:
        raise RuntimeError ('Wrong query data. Hash function failed')
    print('Data processing')
    return respond
def pwned_api_check(passwor):
    pass

print('Data sending ......')
request_api_data('CBDFA')
