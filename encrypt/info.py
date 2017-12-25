#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64


def readinfo(filepath):
    mail = ''
    salt = ''
    try:
        reader = open(filepath, 'r')
        while True:
            line = reader.readline()
            if len(line) == 0:
                break
            if line.startswith('mail='):
                mail = line[5:].strip()
            if line.startswith('salt='):
                salt = line[5:].strip()
                salt = base64.urlsafe_b64decode(salt)
        reader.close()
    except FileNotFoundError as e:
        return False
    return mail, salt


def writeinfo(mail, salt, filepath):
    salt = base64.urlsafe_b64encode(salt).decode()
    f = open(filepath, 'w')
    f.write('mail=' + mail + '\n' + 'salt=' + salt)
    f.close()
