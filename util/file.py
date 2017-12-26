import os

def rm_file(filepath):
    os.remove(filepath)


def write_file(filepath, data):
    try:
        f = open(filepath, 'wb')
        f.write(data)
        f.close()
    except FileNotFoundError as e:
        print(e)