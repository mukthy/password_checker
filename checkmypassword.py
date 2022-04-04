import requests
import hashlib


password = input('Please enter your password to check: \n')

def request_api(query_hash):
    # print(query_hash)
    url = 'https://api.pwnedpasswords.com/range/' + f'{query_hash}'
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error from API: {response.status_code}, Please check the hash format or API URL')

    return response


def read_response(hashes, rest_chars):
    #print(hashes.text)
    if rest_chars in hashes.text:
        print('Found')
    else:
        print('Not Found')


def hash_password(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_chars = sha1password[:5]
    rest_chars = sha1password[5:]
    print(first_5_chars, rest_chars)
    response = request_api(first_5_chars)
    print(response)
    return read_response(response, rest_chars)


hash_password(password)
