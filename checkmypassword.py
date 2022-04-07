import requests
import hashlib
import sys

#  password = input('Please enter your password to check: \n')


def request_api(query_hash):
    # print(query_hash)
    # API of have I been pawned.
    url = 'https://api.pwnedpasswords.com/range/' + f'{query_hash}'
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error from API: {response.status_code}, Please check the hash format or API URL')

    return response


def read_response(hashes, rest_chars):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == rest_chars:
            return count
    return 0


def hash_password(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_chars = sha1password[:5]
    rest_chars = sha1password[5:]
    # print(first_5_chars, rest_chars)
    response = request_api(first_5_chars)
    # print(response)
    return read_response(response, rest_chars)


def main(args):
    for password in args:
        count = hash_password(password)
        if count:
            print(f'{password} was found {count} times, please change the password..')

        else:
            print(f'{password} was not found, please go ahead.')

    return 'Done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
