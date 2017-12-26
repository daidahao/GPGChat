from mail import check_mail_info


print(check_mail_info("dzh@daidahao.me", "Mima123", "smtp.exmail.qq.com"))

mail = input()
password = input()
server = input()
print(check_mail_info(mail, password,server))