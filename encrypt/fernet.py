import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import InvalidToken
from cryptography.fernet import Fernet
from util.file import rm_file


def encrypt(password, filepath):
    salt = os.urandom(16)
    key = derivekey(password, salt)
    f = Fernet(key)
    data = readfile(filepath)
    token = f.encrypt(data)
    writefile(filepath + ".encrypt", token)
    rm_file(filepath)
    return salt


def decrypt(password, salt, filepath):
    key = derivekey(password, salt)
    f = Fernet(key)
    data = readfile(filepath + ".encrypt")
    try:
        dec = f.decrypt(data)
    except InvalidToken as e:
        print(e)
        return False
    return dec


def encryptstring(password, salt, string):
    key = derivekey(password, salt)
    f = Fernet(key)
    result = f.encrypt(string.encode())
    result = base64.urlsafe_b64encode(result).decode()
    return result


def decryptstring(password, salt, string):
    key = derivekey(password, salt)
    f = Fernet(key)
    return f.decrypt(base64.urlsafe_b64decode(string)).decode()

def derivekey(password, salt):
    password = password.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key


def readfile(filepath):
    try:
        f = open(filepath, 'rb')
        data = f.read()
        return data
    except FileNotFoundError as e:
        print(e)


def writefile(filepath, data):
    try:
        f = open(filepath, 'wb')
        f.write(data)
        f.close()
    except FileNotFoundError as e:
        print(e)