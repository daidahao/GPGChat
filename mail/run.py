from mail import mail
import time

# print(mail.connect_smtp("dzh@daidahao.me", "Mima123", "smtp.exmail.qq.com"))

u1 = "dzh@daidahao.me"
u2 = "zxw@daidahao.me"
pw = "Mima123"

# send
con,m = mail.connect_smtp(u1, pw, "smtp.exmail.qq.com")
if con != None:
    t1 = time.time()
    mail.send_mail(con,u1, u2, 'Test 1, 中文测试', '[GPGChat] uuid0001' )
    print(time.time()-t1)
    mail.send_mail(con,u1, u2, 'Test 2, 中文测试', '[GPGChat] uuid0002' )


time.sleep(7)

# receive
con = mail.connect_imap(u2, pw, "imap.exmail.qq.com")
if con != None:

    t1 = time.time()
    while True:
        t2 = time.time()
        msg = mail.receive_mail(con)
        if msg != None and len(msg)!= 0:
            print('start till now ', time.time()-t1)
            print('receive time ', time.time()-t2)
            print(msg)