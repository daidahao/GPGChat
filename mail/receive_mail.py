#-*- encoding: utf-8 -*-
import email
import imaplib

# 标记已读、未读
# search 【GPGChat】开头的未读的邮件

def receive_mail(M):
    M.select('INBOX')
    '''邮件状态设置
        https://www.example-code.com/python/imap_search.asp
        网页端的需要刷新一下'''
    typ, data = M.search(None, 'All')

    id_list = data[0].split()
    for email_id in id_list:
        # fetch the email body
        typ,data=M.fetch(email_id,'(RFC822)')
        '''here's the body, which is raw text of the whole email, including headers and alternate payloads'''
        raw_mail = data[0][1].decode()
        msg=email.message_from_string(raw_mail)
        sub=email.header.decode_header(msg['Subject'])
        subject = sub[0][0].decode()

        if '[GPGChat]' in subject:
            M.store(email_id,'+FLAGS','\Seen')
            print(subject)

    # search unseen 有时可以工作，有时不能
    # store 也是
    # 还没有读邮件主体

# if __name__ == '__main__':
#     mail_user='test@mail.test'
#     password = 'test'
#
#     M = imaplib.IMAP4_SSL('imap.exmail.qq.com')
#     M.login(mail_user, password)
#
#     receive_mail(M)
#
#     M.close()
#     M.logout()
