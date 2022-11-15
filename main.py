import random

import itchat
from itchat.content import TEXT


@itchat.msg_register([TEXT])
def text_reply(msg):
    if msg['Type'] == 'Text':
        kword = ['ark', 'arknights']
        responses = ['这是收到ark的自动回复', '已经收到ark了']
        info = msg['Content']
        for word in kword:
            if word in info:
                index = random.randint(0, len(responses) - 1)
                itchat.send_msg(responses[index], msg['FromUserName'])
                break


if __name__ == '__main__':
    itchat.auto_login()
    # users = itchat.search_friends(name='slackcoder')
    # print(users)
    # userName = users[0]['UserName']
    # itchat.send('itchat test', toUserName=userName)
    itchat.run()
