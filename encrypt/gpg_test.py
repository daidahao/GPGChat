import gpg

gpg=gpg.GPG()

#keyid=gpg.gen_key('test','scc@daidahao.me','scc')#生成新的密钥并上传到服务器
keys=gpg.search('scc@daidahao.me')#按邮箱搜索服务器密钥列表
print(keys)
if len(keys)>0:    
    keyid1=keys[0]['keyid']#获取keyid
    gpg.download_key(keyid1)#按keyid下载密钥   
    message="Hello World!\n你好，世界！"#原文
    print(message)
    encrypted=gpg.encrypt(message,keyid1)#使用keyid1对应的密钥加密
    print(encrypted)
    text=gpg.decrypt(encrypted,'scc')#解密，需要lock
    print(text)