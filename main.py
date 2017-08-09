# -*- coding: utf-8 -*-
import itchat
import requests
from itchat.content import *

API_URL = 'http://www.tuling123.com/openapi/api'
API_KEY = '71c15934b5ff4a57924e0657c4feb447'
API_SECRET = 'ed5dc5d40e7a5899ONOFF'


@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def text_reply(msg):
    data = {
        "key" : API_KEY,
        'info' : msg['Text'],
    }

    res = requests.post(API_URL, data=data )
    result = res.json()
    itchat.send(u'汉光智能: %s' % result['text'], msg['FromUserName'])

itchat.auto_login(True, enableCmdQR=False)
itchat.run() 
itchat.dump_login_status()