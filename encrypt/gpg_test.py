from gpg import GPG

gpg=GPG(binary='gpg2')

#生成新的密钥并上传到服务器
# keyid=gpg.gen_key('test','8888@999.com','test')
# print(keyid)
#按邮箱搜索服务器密钥列表
keys=gpg.search('8888@999.com')
print(keys)
print(len(keys))
keys_list = gpg.keys_to_datamap(keys)
print(keys_list)
# if len(keys)>0:
#     keyid1=keys[0]['keyid']#获取keyid
#     gpg.download_key(keyid1)#按keyid下载密钥
#     message="Hello World!\n你好，世界！"#原文
#     # print(message)
#     encrypted = gpg.encrypt(message, keyid1)#使用keyid1对应的密钥加密
#     print("encrypted = ", encrypted)
#     # text=gpg.decrypt(encrypted,'test')#解密，需要lock
#     # print(text)