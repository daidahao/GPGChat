from database.init_db import init_db
from database import db
from uuid import uuid4
import time
import os

dbpath = '123.db'
uuid = uuid4()
keyid = 9999999
text = 'Hello!'

os.remove(dbpath)

init_db('123.db')

db.add_massage(db_path=dbpath,
                       uuid=uuid,
                       seq=3,
                       send_from=None,
                       send_to=keyid,
                       content=text,
                       timestamp=time.time())

db.add_massage(db_path=dbpath,
                       uuid=uuid,
                       seq=4,
                       send_from=None,
                       send_to=keyid,
                       content=text,
                       timestamp=time.time())

db.add_massage(db_path=dbpath,
                       uuid=uuid,
                       seq=5,
                       send_from=keyid,
                       send_to=None,
                       content=text,
                       timestamp=time.time())

db.add_contact(dbpath, 'Zhihao Dai', 'me@daidahao.me', keyid)
db.add_contact(dbpath, 'ZZJ', 'me2@daidahao.me', keyid + 1)


all_messages = db.fetch_all_messages('123.db', keyid)

for message in all_messages:
    print(message)
    print(type(message[0]))
    if not message[0]:
        print('Sent')

print(db.read_contact(dbpath))