import os
#确认是否存在文件
def rm_file(filepath):
    try:
        os.remove(filepath)
    except FileNotFoundError as e:
        print(filepath + " cannot be found!")

#向文件中写入信息
def write_file(filepath, data):
    try:
        f = open(filepath, 'wb')
        f.write(data)
        f.close()
    except FileNotFoundError as e:
        print(filepath + " cannot be found!")