# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:32:53 2024
@author: segal
"""
# an encription program:
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
# look at those characters:
#print(chars)
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars : {chars}")
#print(f"key : {key}")

# get user input to encript:
plainTxt = input("Enter a msg to encript: ")

CipherTxt = ""

for letter in plainTxt:
    index = chars.index(letter)
    CipherTxt += key[index]

print(f" OG MSG : {plainTxt}")

print(f" Encripted MSG : {CipherTxt}")

# Next decript the msg:
CipherTxt = input("Enter a msg to decript: ")

plainTxt = ""

for letter in CipherTxt:
    index = key.index(letter)
    plainTxt += chars[index]

print(f" encripted MSG : {CipherTxt}")

print(f" og MSG : {plainTxt}")