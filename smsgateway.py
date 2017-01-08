#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SMSGateway.me API

import requests


class SmsgatewayAccount:  # Account at smsgateway.me
    username = ""
    password = ""

    # Constructor
    def __init__(self, username, password):
        self.username = username
        self.password = password


class SmsgatewayDevice:  # Mobile divice at smsgateway.me
    account = ""
    deviceId = ""

    # Constructor
    def __init__(self, account, deviceId):
        self.account = account
        self.deviceId = deviceId

    # Send a text message
    def send(self, number, msg):
        # print("SMS to "+number+" : "+msg)
        url = 'http://smsgateway.me/api/v3/messages/send'
        print(self.account.username)
        args = {
            u'email': self.account.username,
            u'password': self.account.password,
            u'device': self.deviceId,
            u'number': number,
            u'message': msg,
        }
        response = requests.post(url, data=args)
        return response
