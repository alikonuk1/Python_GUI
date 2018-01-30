#!/bin/python3
import random

chars = 'qwertyuıopasdfghjklizxcvbnm1234567890!?.,-+()=/'

length = input('Password length?')
length = int(length)

for p in range(3):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)
