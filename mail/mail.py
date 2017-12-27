#-*- encoding: utf-8 -*-
import email
import smtplib, imaplib
from email.header import Header
from email.mime.text import MIMEText

def check_mail_info(mail_addr, password, server_addr):
    connection, message = connect_smtp(mail_addr, password, server_addr)
    if connection is None:
        return False, message
    connection.close()
    return True, message

# Don't forget close connection when log out
def connect_smtp(mail_addr, password, server_addr):
    connection = None
    hostname, port = split_addr(server_addr)
    try:
        # print("hostname=", hostname)
        # print("port=", port)
        connection = smtplib.SMTP(hostname, port)
        connection.login(mail_addr, password)
    except smtplib.SMTPAuthenticationError as e:
        connection.close()
        return None, "Email or password is not correct!"
    except smtplib.SMTPConnectError as e:
        connection.close()
        return None, "Please check the server address or your connection!"
    except ConnectionRefusedError as e:
        if connection is not None:
            connection.close()
        return None, "Please check the server address or your connection!"
    return connection, "Success"


def connect_imap(email_addr, password,server_addr):
    connection = imaplib.IMAP4_SSL(server_addr)
    connection.login(email_addr, password)
    return connection


def split_addr(addr):
    addr_split = addr.split(':')
    if len(addr_split) == 2:
        return addr_split[0], int(addr_split[1])
    return addr, 25


def send_mail(smtp_connection, from_addr, to_addr, text, subject=''):
    # form an email
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = from_addr
    msg['To'] =  to_addr
    msg['Subject'] = Header(subject, 'utf-8').encode()

    # send the email
    smtp_connection.sendmail(from_addr, [to_addr], msg.as_string())


def receive_mail(imap_connection):

    new_msg = []

    imap_connection.select('INBOX')
    # email status settinghttps://www.example-code.com/python/imap_search.asp

    # # TEST: set all emails as unseen
    # typ, data = M.search(None, 'All')
    # id_list = data[0].split()
    # for email_id in id_list:
    #     M.store(email_id,'-FLAGS','\Seen')

    # Fetch UNSEEN emails
    typ, data = imap_connection.search(None, 'UNSEEN')
    id_list = data[0].split()
    for email_id in id_list:
        # fetch the email body
        typ,data=imap_connection.fetch(email_id,'(RFC822)')

        # here's the body, which is raw text of the whole email, including headers and alternate payloads
        raw_mail = data[0][1].decode()
        msg=email.message_from_string(raw_mail)

        # Select emails with a prefix [GPGChat]
        sub=email.header.decode_header(msg['Subject'])
        subject = sub[0][0].decode()
        if '[GPGChat]' in subject:
            imap_connection.store(email_id,'+FLAGS','\Seen')
            new_msg.append(msg)

    # # TEST FUNCTION: parse the new msgs
    # for msg in new_msg:
    #     subject = email.header.make_header(email.header.decode_header(msg['SUBJECT']))
    #     mail_from = email.header.make_header(email.header.decode_header(msg['From']))
    #     mail_content = ''
    #
    #     maintype = msg.get_content_maintype()
    #     if maintype == 'multipart':
    #         for part in msg.get_payload():
    #             if part.get_content_maintype() == 'text':
    #                 mail_content = part.get_payload(decode=True).strip()
    #     elif maintype == 'text':
    #         mail_content = msg.get_payload(decode=True).strip()
    #
    #     mail_content = mail_content.decode()
    #
    #     print(subject,mail_from,mail_content,sep='\n')
    #     print()

    return new_msg
