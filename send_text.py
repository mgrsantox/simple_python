#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:34:49 2018

@author: pysantosh
"""

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACee5b02b480f5379c9c7b34ce7d1e3393'
auth_token = '191a2a6f981aacb3cfefd7370cd209fc'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+15709191434',
                              body='Happy Birthday udacity test',
                              to='+9779808434085'
                          )

print(message.sid)