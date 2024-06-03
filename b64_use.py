#!/usr/bin/env python3

# Python 3.9.5

# b64_use.py

import base64

def b64_encode(string):
    bts = base64.b64encode(bytes(string, 'utf-8'))  # converts string to bytes
    return bts.decode('utf-8')                      # convert bytes to string

def b64_decode(encoded_string):
    return base64.b64decode(encoded_string)

if __name__ == '__main__':
    string = "username:password"
    encoded_string = b64_encode(string)
    decoded_string = b64_decode(encoded_string)
    print(encoded_string)
    print(decoded_string)
