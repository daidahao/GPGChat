import os

def rm_file(filepath):
    try:
        os.remove(filepath)
    except FileNotFoundError as e:
        print(filepath + " cannot be found!")


def write_file(filepath, data):
    try:
        f = open(filepath, 'wb')
        f.write(data)
        f.close()
    except FileNotFoundError as e:
        print(filepath + " cannot be found!")