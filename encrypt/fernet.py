import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import InvalidToken
from cryptography.fernet import Fernet
from util.file import rm_file

# 使用Fernet对用户设置的密码进行加密并返回密码的salt
def encrypt_file(password, filepath):
    #随机生成一个16bytes的salt
    salt = os.urandom(16)
    #为用户设置的密码添加salt生成key
    key = derivekey(password, salt)
    #对key进行加密
    f = Fernet(key)
    data = readfile(filepath)
    token = f.encrypt(data)
    writefile(filepath + ".encrypt", token)
    rm_file(filepath)
    return salt

# 当用户输入密码，在文件中找到相应的salt，组合成key，对key进行解密，返回解密后的数据
def decrypt_file(password, salt, filepath):
    key = derivekey(password, salt)
    f = Fernet(key)
    data = readfile(filepath + ".encrypt")
    try:
        dec = f.decrypt(data)
    except InvalidToken as e:
        # print(e)
        return False
    #返回解密后的data
    return dec

#加密字符串，将用户输入的密码所对应的string进行转码
def encrypt_string(password, salt, string):
    key = derivekey(password, salt)
    f = Fernet(key)
    result = f.encrypt(string.encode())
    result = base64.urlsafe_b64encode(result).decode()
    #返回加密字符串
    return result

#解密字符串，将用户输入密码所对应的string进行解码
def decrypt_string(password, salt, string):
    key = derivekey(password, salt)
    f = Fernet(key)
    #返回加密字符串解密后的结果
    return f.decrypt(base64.urlsafe_b64decode(string)).decode()
#通过用户输入的密码及其对应的salt获取相应的key
def derivekey(password, salt):
    #对password进行解码
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

#读取文件
def readfile(filepath):
    try:
        f = open(filepath, 'rb')
        data = f.read()
        return data
    except FileNotFoundError as e:
        print(e)

#将需要的data写入文件
def writefile(filepath, data):
    try:
        f = open(filepath, 'wb')
        f.write(data)
        f.close()
    except FileNotFoundError as e:
        print(e)