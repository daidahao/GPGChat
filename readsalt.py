#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def read(data):
    mail = ''
    salt = ''
    try:
        reader = open(data, 'r')
        while True:
            line = reader.readline()
            if len(line) == 0:
                break
            if line.startswith('mail='):
                mail=line[5:]
            if line.startswith('salt='):
                salt=line[5:]
        reader.close()
    except FileNotFoundError as e:
        print(e)
    return mail.strip(), salt.strip()

def write(mail, salt, filepath):
    f = open(filepath, 'w')
    f.write('mail=' + mail + '\n' + 'salt=' + salt)
    f.close()
