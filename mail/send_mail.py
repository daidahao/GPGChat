#-*- encoding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText

def sendMail(server,from_addr, to_addr, text, subject=''):
    # form an email
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = from_addr
    msg['To'] =  to_addr
    msg['Subject'] = Header(subject, 'utf-8').encode()

    # send the email
    server.sendmail(from_addr, [to_addr], msg.as_string())

