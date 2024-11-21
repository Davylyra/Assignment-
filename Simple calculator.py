# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 01:08:39 2023

@author: DAVIDICA
"""

print('\nWelcome to Davcacus \n')
a = input('Enter the first number:  ')
b = input('Enter the second number:  ')
print('\nPlease choose the operation sign you want\na.➕ Add\nb.➖ Subtract\nc.✖ Multiply\nd.➗ Divide')
u = input()


if u == ("a"):
    print(int(a)+int(b))

if u == ('b'):
    print(int(a)-int(b))


if u == ("c"):
    print(int(a)* int(b))


if u == ("d"):
    print(int(a)/ int(b))
    

