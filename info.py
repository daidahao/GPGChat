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
        self.realpassword = None
        self.dbpath = None
        self.reallock = None

    def read(self, filepath):
        try:
            reader = open(filepath, 'r')
            while True:
                line = reader.readline()
                if len(line) == 0:
                    break
                if line.startswith('mail='):
                    self.mail = self.readline(line, 'mail')
                if line.startswith('salt='):
                    self.salt = self.readline(line, 'salt')
                    self.salt = base64.urlsafe_b64decode(self.salt)
                if line.startswith('password='):
                    self.password = self.readline(line, 'password')
                if line.startswith('server='):
                    self.server = self.readline(line, 'server')
                if line.startswith('name='):
                    self.name = self.readline(line, 'name')
                if line.startswith('dbpath='):
                    self.dbpath = self.readline(line, 'dbpath')
            reader.close()
        except FileNotFoundError as e:
            return False

    def write(self, filepath):
        salt = base64.urlsafe_b64encode(self.salt).decode()
        # password = base64.urlsafe_b64encode(self.password).decode()
        f = open(filepath, 'w')
        f.write(self.writeline('mail', self.mail) +
                self.writeline('salt', salt) +
                self.writeline('password', self.password) +
                self.writeline('server', self.server) +
                self.writeline('name', self.name) +
                self.writeline('dbpath', self.dbpath))
        f.close()

    def print(self):
        print("mail=", self.mail)
        print("salt=", self.salt)
        print("password=", self.password)
        print("server=", self.server)
        print("name=", self.name)
        # print("realpassword=", self.realpassword)
        print("dbpath=", self.dbpath)

    def readline(self, line, name):
        if line.startswith(name + '='):
            return line[(len(name) + 1):].strip()

    def writeline(self, name, value):
        return name + '=' + value + '\n'
