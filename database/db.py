# -*- coding:utf-8 -*-
import sqlite3

'''
    format of SELECT result: [ (col_1, ), (col_1, ) 
'''

'''TABLE CONTACT'''
def add_contact(db_path, addr, name, public_key):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()

    try:
        cursor.execute('INSERT INTO contact VALUES (?,?,?,?)',(addr, name, public_key, 'W'))
        connection.commit()
    except sqlite3.IntegrityError as e:
        cursor.close()
        connection.close()
        return 0

    cursor.close()
    connection.close()
    return 1


def delete_contact(db_path, addr):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()

    sql_cmd = 'DELETE FROM contact WHERE email_addr = "%s"' % addr
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

'''TABLE CHAT'''
def add_chat(db_path, uuid, send_by, send_from):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()

    try:
        cursor.execute('INSERT INTO chat VALUES (?,?,?)', (uuid, send_by, send_from))
        connection.commit()
    except sqlite3.IntegrityError as e:
        cursor.close()
        connection.close()
        return 0

    cursor.close()
    connection.close()
    return 1

def get_uuid(db_path,send_by, send_to):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()

    sql_cmd = 'SELECT uuid FROM chat WHERE send_by = "%s" and send_to = "%s"' %(send_by, send_to)
    cursor.execute(sql_cmd)
    uuid = cursor.fetchall()

    cursor.close()
    connection.close()

    return uuid

'''TABLE MESSAGE'''
def add_massage(db_path,uuid, seq, content, timestamp):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()

    try:
        sql_cmd = 'INSERT INTO message VALUES ("%s",%d,"%s",%f)'%(uuid, seq, content, timestamp)
        cursor.execute(sql_cmd)
        connection.commit()
    except sqlite3.IntegrityError as e:
        cursor.close()
        connection.close()
        return 0

    cursor.close()
    connection.close()
    return 1

def get_message(db_path, uuid):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()

    sql_cmd = 'SECLECT * FROM message WHERE uuid = "%s" ORDER BY time_stamp' % uuid
    cursor.execute(sql_cmd)
    rst = cursor.fetchall()

    cursor.close()
    connection.close()
    return rst
