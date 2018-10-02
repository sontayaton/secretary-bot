# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
import os

from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (MessageEvent, TextMessage, FlexSendMessage, TextSendMessage,SourceUser, SourceGroup, SourceRoom,StickerMessage, StickerSendMessage,QuickReply)



mention_id = os.getenv('LINE_MODFORWARD_ID', None) 

####### Read keyword from json ############   
#with open('data/mention.json', 'r') as f:
#    mention_dict = json.load(f)
##########################################

keywords = ["ton","tonson","ต้น","ต้นสน"]

def forwardMsgToUser(line_bot_api,event):

	# Get message from Line event
	text = event.message.text

	for word in keywords:
		if word in text:
			try:
				with open('models/flexmessage_group.json', 'r') as f:
					flexMsg = json.load(f)
				
				# Compose message for forwarding to user
				if event.source.type == 'group':
					flexMsg = json.load('models/flexmessage_group.json')
					group = line_bot_api.get_group_member_profile(event.source.group_id,event.source.user_id)
					profile = line_bot_api.get_profile(event.source.user_id)
					flexMsg['header']['contents'][0]['url'] = group.picture_url
					print(json.dump(flexMsg))
					
				# Push message that contain keyword to User,Group,Room 
			    #line_bot_api.push_message(mention_id, FlexSendMessage(contents=text))

			    # Reply "Read" message to Chanel if contain keyword occur 
			    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Read'))
			    break
			except LineBotApiError as e:
			    # error handle
			    print("Got exception from LINE Messaging API: %s\n" % e.message)
	
			