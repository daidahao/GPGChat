# -*- coding:utf-8 -*-
import sqlite3

connection = sqlite3.connect('gpg.db')
cursor =connection.cursor()

cursor.execute("drop table contact")
cursor.execute("drop table chat")
cursor.execute("drop table message")

# create tables
cursor.execute("create table contact (email_addr varchar primary key,name varchar, public_key varchar not null, status varchar not null)")
cursor.execute("create table chat (uuid varchar, send_by varchar, send_to varchar, CONSTRAINT pk_3 PRIMARY KEY (uuid,send_by,send_to))")
cursor.execute("create table message (uuid varchar, sequence int, content varchar NOT NULL, time_stamp REAL NOT NULL, "
               "CONSTRAINT pk_2 PRIMARY KEY (uuid,sequence))")

cursor.close()
connection.close()
