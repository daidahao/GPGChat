import platform
import mail as mail_agent

class Packet:
    def __init__(self):
        self.uuid=''
        self.sender=''
        self.receiver=''
        self.sequence=0
        self.message=''
        self.signed_keyid=''

    def set_uuid(self, uuid):
        self.uuid = uuid

    def set_sender(self, send_from):
        self.sender = send_from

    def set_receiver(self, send_to):
        self.receiver = send_to

    def set_sequence(self, seq):
        self.sequence = seq

    def set_message(self, msg):
        self.message = msg

    def set_signedkeyid(self, keyid):
        self.signed_keyid = keyid


class Agent:
    agent_edition = 'GPGChat 0.0.1'
    os_info = platform.system() + ' ' + platform.release() + ' ' + platform.machine()

    def send_packet(self, smtp_connection, packet):
        text = ''
        text += 'UserAgent: ' + self.agent_edition +' ('+self.os_info+')\r\n'
        text += 'Sequence: ' + str(packet.sequence) + '\r\n'
        text +='Keyid: '+packet.signed_keyid+'\r\n'
        text += '\r\n' + packet.message
        return mail_agent.send_mail(smtp_connection, packet.sender, packet.receiver, text, packet.uuid)

    def receive_packet(self, imap_connect):
        packets = []
        new_mails=mail_agent.receive_mail(con_imap)
        for mail in new_mails:
            try:
                packet=Packet()
                packet.set_uuid(mail['subject'].strip('[GPGChat] '))
                packet.set_sender(mail['mail_from'])
                content=mail['mail_content'].splitlines()
                packet.set_sequence(int(content[1].split(':')[1].strip()))
                packet.set_signedkeyid(content[2].split(':')[1].strip())
                packet.set_message('\r\n'.join(content[4:]))
                packets.append(packet)
            except IndexError:
                pass
        return packets

if __name__ == '__main__':
    #       mail will be like this:
    # UserAgent: GPGChat 0.0.1 (Windows 10 AMD64)
    # Sequence: 1
    # signed keyid: hafjkdahfanfklhsf
    #
    # Hello world
    # 你好，世界！
    #

    agent = Agent()
          # send mail test
    # con_smtp,state=mail_agent.connect_smtp('scc@daidahao.me','Mima123','smtp.exmail.qq.com')
    # packet=Packet()
    # packet.set_uuid('16164656464862')
    # packet.set_message('Hello world\r\n你好，世界！')
    # packet.set_sender('scc@daidahao.me')
    # packet.set_receiver('dzh@daidahao.me')
    # packet.set_sequence(1)
    # packet.set_signedkeyid('hafjkdahfanfklhsf')
    # print(agent.send_packet(con_smtp,packet))
    # quit()


    #       receive mail test
    # con_imap=mail_agent.connect_imap('dzh@daidahao.me','Mima123','imap.exmail.qq.com')
    # if con_imap:
    #     new_msgs=agent.receive_packet(con_imap)
    #     print(new_msgs)
    #     for packet in new_msgs:
    #         print(packet.uuid)
    #         print(packet.sender)
    #         print(packet.sequence)
    #         print(packet.signed_keyid)
    #         print(packet.message)
    #         print()
    #     con_imap.logout()
