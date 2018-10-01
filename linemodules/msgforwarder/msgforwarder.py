# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
import os

from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,SourceUser, SourceGroup, SourceRoom,StickerMessage, StickerSendMessage,QuickReply)



mention_id = os.getenv('LINE_MODFORWARD_ID', None) 

####### Read keyword from json ############   
#with open('data/mention.json', 'r') as f:
#    mention_dict = json.load(f)
##########################################

keywords = ["ton","tonson","ต้น","ต้นสน"]

def forwardMsgToUser(line_bot_api,event):

	# Get message from Line event
	text = event.message.text
	#user_id = event.source.userId

	for word in keywords:
		if word in text:
			try:
				# Push message that contain keyword to User,Group,Room 
				#profile = line_bot_api.get_profile(user_id)
				#print(event)
				#text = profile.display_name + " : " + text
			    line_bot_api.push_message(mention_id, TextSendMessage(text=text))

			    # Reply "Read" message to Chanel if contain keyword occur 
			    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Read'))
			    break
			except LineBotApiError as e:
			    # error handle
			    print("Got exception from LINE Messaging API: %s\n" % e.message)
	
			