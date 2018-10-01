# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
import os


mention_id = os.getenv('LINE_MODFORWARD_ID', None)    
with open('data/mention.json', 'r') as f:
    mention_dict = json.load(f)


def forwardMsgToUser(line_bot_api,event):
	text = event.message.text

	for word in mention_dict["keywords"]:
		if word in text:
			try:
			    line_bot_api.push_message(mention_id, TextSendMessage(text=text))
			except LineBotApiError as e:
			    # error handle
			    print("Got exception from LINE Messaging API: %s\n" % e.message)
	
			