import smtplib
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

#
# if __name__ == '__main__':
#
#     '''send'''
#     from_addr = 'test@mail'
#     password = getpass.getpass('Enter password: ')
#     to_addr = 'test@mail.test'
#     smtp_server = 'smtp.exmail.qq.com'
#
#     text = '关关雎鸠，在河之洲'
#     subject = 'test4'
#
#     server = smtplib.SMTP(smtp_server, 25)
#     # 打印出和SMTP服务器交互的所有信息
#     server.set_debuglevel(1)
#     server.login(from_addr, password)
#
#     send_mail.sendMail(server, from_addr, to_addr, text, subject)
#
#     server.quit()