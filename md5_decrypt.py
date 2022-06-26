#!/usr/bin/env python3

# Python 3.9.9

# md5_decrypt.py

# Dependency
import hashlib

password_hash:str = '0992a2d18de838d8380c50e4b9dbfe9f'
password_list:list = ['123456', 'password', 'ilove2code', '...']

for password in password_list:
  md5_password = hashlib.md5(password.encode()).hexdigest()
  if password_hash == md5_password:
    print("There is a match:", password)
    break
  else:
    print("There is no match.")
