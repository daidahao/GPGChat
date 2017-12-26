#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

class Info:
    def __init__(self):
        self.mail = None
        self.salt = None
        self.password = None
        self.server = None
        self.name = None

    def read(self, filepath):
        try:
            reader = open(filepath, 'r')
            while True:
                line = reader.readline()
                if len(line) == 0:
                    break
                if line.startswith('mail='):
                    self.mail = line[5:].strip()
                if line.startswith('salt='):
                    self.salt = line[5:].strip()
                    self.salt = base64.urlsafe_b64decode(self.salt)
            reader.close()
        except FileNotFoundError as e:
            return False

    def write(self, filepath):
        salt = base64.urlsafe_b64encode(self.salt).decode()
        f = open(filepath, 'w')
        f.write('mail=' + self.mail + '\n' + 'salt=' + salt)
        f.close()

    def print(self):
        print("mail=", self.mail)
        print("salt=", self.salt)
        #print("password=", self.password)

    def readline(self, line, name):
        if line.startswith('name' + '='):
            return line[(len(name) + 1):].strip()

# def readinfo(filepath):
#     mail = ''
#     salt = ''
#     try:
#         reader = open(filepath, 'r')
#         while True:
#             line = reader.readline()
#             if len(line) == 0:
#                 break
#             if line.startswith('mail='):
#                 mail = line[5:].strip()
#             if line.startswith('salt='):
#                 salt = line[5:].strip()
#                 salt = base64.urlsafe_b64decode(salt)
#         reader.close()
#     except FileNotFoundError as e:
#         return False
#     return mail, salt
#
#
# def writeinfo(mail, salt, filepath):
#     salt = base64.urlsafe_b64encode(salt).decode()
#     f = open(filepath, 'w')
#     f.write('mail=' + mail + '\n' + 'salt=' + salt)
#     f.close()
