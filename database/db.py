# -*- coding:utf-8 -*-
import sqlite3

'''
    format of SELECT result: [ (col_1, ), (col_1, ) ]
'''

'''TABLE CONTACT'''
def add_contact(db_path, name, addr, key_id):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()
    try:
        cursor.execute('INSERT INTO contact (key_id, email_addr, name, status) VALUES (?,?,?,?)', (key_id, addr, name, 'C'))
        connection.commit()
    except sqlite3.IntegrityError as e:
        cursor.close()
        connection.close()
        return False
    cursor.close()
    connection.close()
    return True


def delete_contact(db_path, keyid):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    try:
        sql_cmd = 'DELETE FROM contact WHERE key_id = "%s"' % keyid
        cursor.execute(sql_cmd)
        connection.commit()
    except sqlite3.IntegrityError as e:
        cursor.close()
        connection.close()
        return False

    cursor.close()
    connection.close()
    return True


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

def read_contact(db_path, status='C'):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()
    command = \
    "SELECT c.name, c.email_addr, c.key_id, coalesce(a.last_message, 0) last_message FROM contact c"" \
    ""LEFT JOIN ( SELECT max(time_stamp) last_message, key_id"" \
    "" FROM ( SELECT time_stamp, CASE send_from WHEN 'None' THEN send_to"" \
    "" ELSE send_from END key_id FROM message ) b GROUP BY key_id ) a"" \
    "" ON a.key_id = c.key_id WHERE c.status = ?;"""
    cursor.execute(command, (status,))
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

def get_message(db_path, send_from, send_to):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()

    sql_cmd = 'SELECT uuid, sequence, send_from, send_to, content, time_stamp FROM message ' \
              'WHERE (send_from = "%s" and send_to = "%s") ' \
              'or (send_from = "%s" and send_to = "%s") ' \
              'ORDER BY time_stamp' % (send_from, send_to,send_to,send_from)
    cursor.execute(sql_cmd)
    rst = cursor.fetchall()

    cursor.close()
    connection.close()
    return rst

def read_message(db_path):
    connection = sqlite3.connect(db_path)
    cursor =connection.cursor()

    cursor.execute('SELECT * FROM message')
    rst = cursor.fetchall()
    cursor.close()
    connection.close()

    return rst