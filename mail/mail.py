#-*- encoding: utf-8 -*-
import email
import smtplib, imaplib
from email.header import Header
from email.mime.text import MIMEText
import socket
#确认需要连接的smtp信息
def check_smtp_info(mail_addr, password, server_addr):
    connection, message = connect_smtp(mail_addr, password, server_addr)
    if connection is None:
        return False, message
    connection.close()
    return True, message

# Don't forget close connection when log out
#连接smtp
def connect_smtp(mail_addr, password, server_addr):
    connection = None
    hostname, port = split_addr(server_addr)
    try:
        # print("hostname=", hostname)
        # print("port=", port)
        connection = smtplib.SMTP_SSL(hostname, port)
        connection.login(mail_addr, password)
    except smtplib.SMTPAuthenticationError as e:
        connection.close()
        return None, "Email or password is not correct!"
    except smtplib.SMTPConnectError as e:
        connection.close()
        return None, "Please check the server address or your connection!"
    except smtplib.SMTPHeloError as e:
        connection.close()
        return None, "The server didn't reply to the HELO greeting."
    except smtplib.SMTPNotSupportedError as e:
        connection.close()
        return None, "The AUTH command is not supported by the server."
    except smtplib.SMTPException as e:
        connection.close()
        return None, "No suitable authentication method was found."
    except ConnectionRefusedError as e:
        if connection is not None:
            connection.close()
        return None, "Please check the server address or your connection!"
    except socket.timeout as e:
        if connection is not None:
            connection.close()
        return None, "Timeout!"
    return connection, "Success"

#连接imap
def connect_imap(email_addr, password,server_addr):
    hostname, port = split_addr(server_addr)
    try:
        if port == 0:
            port = 993
        connection = imaplib.IMAP4_SSL(hostname, port)
        connection.login(email_addr, password)
        return connection
    except imaplib.IMAP4_SSL.error:
        return None

#获取完整独立地址
def split_addr(addr):
    addr_split = addr.split(':')
    if len(addr_split) == 2:
        return addr_split[0], int(addr_split[1])
    return addr, 0

#邮件发送端
def send_mail(smtp_connection, from_addr, to_addr, text, title=''):
    # form an email
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = from_addr
    msg['To'] =  to_addr
    msg['Subject'] = Header(generate_subject(title), 'utf-8').encode()

    # send the email
    try:
        smtp_connection.sendmail(from_addr, [to_addr], msg.as_string())
    except smtplib.SMTPRecipientsRefused as e:
        smtp_connection.close()
        return False, "All recipients were refused. Nobody got the mail."
    except smtplib.SMTPHeloError as e:
        smtp_connection.close()
        return False, "The server didn’t reply properly to the HELO greeting."
    except smtplib.SMTPSenderRefused as e:
        smtp_connection.close()
        return False, "The server didn’t accept the from_addr."
    except smtplib.SMTPDataError as e:
        smtp_connection.close()
        return False, "The server replied with an unexpected error code (other than a refusal of a recipient)."
    except smtplib.SMTPNotSupportedError as e:
        smtp_connection.close()
        return False, "SMTPUTF8 was given in the mail_options but is not supported by the server."
    smtp_connection.close()
    return True, "Success"

def generate_subject(title):
    return '[GPGChat] ' + title
#邮件接收端
def receive_mail(imap_connection):
    try:
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
            subject = sub[0][0]
            if isinstance(subject,str) == False:
                subject = subject.decode()

            if subject.startswith('[GPGChat] '):
                imap_connection.store(email_id,'+FLAGS','\Seen')
                new_msg.append(msg)

        messages = []
        for msg in new_msg:
            subject = email.header.make_header(email.header.decode_header(msg['SUBJECT']))
            mail_from = email.header.make_header(email.header.decode_header(msg['From']))
            mail_content = ''

            maintype = msg.get_content_maintype()
            if maintype == 'multipart':
                for part in msg.get_payload():
                    if part.get_content_maintype() == 'text':
                        mail_content = part.get_payload(decode=True).strip()
            elif maintype == 'text':
                mail_content = msg.get_payload(decode=True).strip()

            mail_content = mail_content.decode()

            messages.append({'subject':str(subject),'mail_from':str(mail_from),'mail_content':str(mail_content)})

        return messages

    except imaplib.IMAP4_SSL.error as e:
        print(e)
        return None