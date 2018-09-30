# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json

with open('data/mention.json', 'r') as f:
    mention_dict = json.load(f)

def forwardMsgToUser(line_bot_api,event):
	text = event.message.text

	for word in mention_dict["keywords"]:
		if word in text:
			line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Display name: ' + profile.display_name),
                    TextSendMessage(text='Status message: ' + profile.status_message)
                ]
            )
	
			