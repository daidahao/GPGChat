import gnupg

class GPG:
    gpg=gnupg.GPG(gnupghome='gpghome',verbose=False, gpgbinary='gpg')
    gpg.encoding = 'utf-8'

    #产生密钥
    def gen_key(self,name,email,lock):
        #产生输入数据
        input_data = GPG.gpg.gen_key_input(name_real=name,name_email=email,passphrase=lock)
        keyid = GPG.gpg.gen_key(input_data)
        # print(keyid)
        #发送密钥到服务器
        GPG.gpg.send_keys('pgp.mit.edu', str(keyid))
        return keyid

    #导出密钥
    #keyid必须，secret=True表示导出私钥，否则导出公钥
    def export_key(self,keyid,secret=False,lock=None):
        if secret:        
            print(GPG.gpg.export_keys(keyid,True,passphrase=lock))
        else:
            print(GPG.gpg.export_keys(keyid))

    #搜索公钥
    def search(self,keyword):
        keys=GPG.gpg.search_keys(keyword, 'pgp.mit.edu')        
        return keys

    #下载公钥
    def download_key(self,keyid):
        import_result = GPG.gpg.recv_keys('pgp.mit.edu', keyid)
        print(import_result.fingerprints)
        

    #加密
    def encrypt(self,data,keyid):
        encrypted_data = GPG.gpg.encrypt(data.encode(),keyid, always_trust=True)
        return str(encrypted_data)

    #解密
    def decrypt(self,encrypted_data,lock):
        decrypted_data = GPG.gpg.decrypt(encrypted_data.encode(),passphrase=lock)
        return str(decrypted_data)