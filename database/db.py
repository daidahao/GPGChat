# -*- coding:utf-8 -*-
import sqlite3

'''
    format of SELECT result: [ (col_1, ), (col_1, ) ]
'''

'''TABLE CONTACT'''
def add_contact(db_path, key_id, addr, name, public_key):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()
    try:
        cursor.execute('INSERT INTO contact VALUES (?,?,?,?,?)',(key_id,addr, name, public_key, 'W'))
        connection.commit()
    except sqlite3.IntegrityError as e:
        cursor.close()
        connection.close()
        return False

    cursor.close()
    connection.close()
    return True


def delete_contact(db_path, addr):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()

    sql_cmd = 'DELETE FROM contact WHERE email_addr = "%s"' % addr
    cursor.execute(sql_cmd)
    connection.commit()

    cursor.close()
    connection.close()


def alter_contact_block(db_path, addr):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()

    sql_cmd = 'SELECT status FROM contact WHERE email_addr = "%s"' % addr
    cursor.execute(sql_cmd)
    status = cursor.fetchall()[0][0]

    if status == 'W':
        sql_cmd = 'UPDATE contact SET status = "B" WHERE email_addr = "%s"' % addr
        cursor.execute(sql_cmd)
        connection.commit()
    else:
        sql_cmd = 'UPDATE contact SET status = "W" WHERE email_addr = "%s"' % addr
        cursor.execute(sql_cmd)
        connection.commit()

    cursor.close()
    connection.close()

def read_contact(db_path):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()

    cursor.execute('SELECT * FROM contact')
    rst = cursor.fetchall()
    cursor.close()
    connection.close()

    return rst


'''TABLE MESSAGE'''
def add_massage(db_path, uuid, seq, send_from, send_to, content, timestamp):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()
    try:
        sql_cmd = 'INSERT INTO message VALUES ("%s",%d,"%s","%s","%s",%f)'\
                  % (uuid, seq, send_from, send_to, content, timestamp)
        cursor.execute(sql_cmd)
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(e)
        cursor.close()
        connection.close()
        return False

    cursor.close()
    connection.close()
    return True

def fetch_all_messages(db_path, keyId, null=None):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    sql_cmd = 'SELECT (send_from = "%s") send, content, time_stamp, uuid, sequence FROM message ' \
              'WHERE (send_from = "%s" and send_to = "%s") ' \
              'or (send_from = "%s" and send_to = "%s") ' \
              'ORDER BY time_stamp' % (null, keyId, null, null, keyId)
    cursor.execute(sql_cmd)
    rst = cursor.fetchall()

    cursor.close()
    connection.close()
    return rst

# def get_message(db_path, send_from, send_to):
#     connection = sqlite3.connect(db_path)
#     cursor =connection.cursor()
#
#     sql_cmd = 'SELECT uuid, sequence, send_from, send_to, content, time_stamp FROM message ' \
#               'WHERE (send_from = "%s" and send_to = "%s") ' \
#               'or (send_from = "%s" and send_to = "%s") ' \
#               'ORDER BY time_stamp' % (send_from, send_to,send_to,send_from)
#     cursor.execute(sql_cmd)
#     rst = cursor.fetchall()
#
#     cursor.close()
#     connection.close()
#     return rst

# def read_message(db_path):
#     connection = sqlite3.connect(db_path)
#     cursor =connection.cursor()
#
#     cursor.execute('SELECT * FROM message')
#     rst = cursor.fetchall()
#     cursor.close()
#     connection.close()
#
#     return rst