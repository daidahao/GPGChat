#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def readinfo(data):
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
        return False
    return mail.strip(), salt.strip()

def writeinfo(mail, salt, filepath):
    f = open(filepath, 'w')
    f.write('mail=' + mail + '\n' + 'salt=' + salt)
    f.close()
