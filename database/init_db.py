# -*- coding:utf-8 -*-
import sqlite3

connection = sqlite3.connect('gpg.db')
cursor =connection.cursor()

# cursor.execute("drop table contact")
# cursor.execute("drop table message")

# create tables
cursor.execute("create table contact (key_id varchar primary key,email_addr varchar unique,name varchar,"
               " public_key varchar not null, status varchar not null)")
cursor.execute("create table message (uuid varchar, sequence int,send_from varchar, send_to varchar,"
               " content varchar NOT NULL, time_stamp REAL NOT NULL, CONSTRAINT pk_2 PRIMARY KEY (uuid,sequence))")


cursor.close()
connection.close()