# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
import os

from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (MessageEvent,TextMessage, FlexSendMessage, TextSendMessage,SourceUser, SourceGroup, SourceRoom,StickerMessage, StickerSendMessage,QuickReply,BubbleContainer,FlexContainer,CarouselContainer,IconComponent,BoxComponent,TextComponent)



mention_id = os.getenv('LINE_MODFORWARD_ID', None) 

####### Read keyword from json ############   
#with open('data/mention.json', 'r') as f:
#    mention_dict = json.load(f)
##########################################

keywords = ["ton","tonson","ต้น","ต้นสน"]

def forwardMsgToUser(line_bot_api,event):

	# Get message from Line event
	text = event.message.text
	print(event.source)
	for word in keywords:
		if word in text:
			try:
				
				# Compose message for forwarding to user
				if isinstance(event.source, SourceGroup):
					group = line_bot_api.get_group_member_profile(event.source.group_id,event.source.user_id)
					profile = line_bot_api.get_profile(event.source.user_id)
					# Build flex message body as message push 
					body_components = list()
					user_icon = IconComponent(url=group.picture_url,size='md')
					recvd_msg = TextComponent(text=text,size='md')
					body_components.append(user_icon)
					body_components.append(recvd_msg)
					body_box = BoxComponent(contents=body_components,layout='baseline')
					body = BoxComponent(contents=body_box,layout='vertical')

					push_mssage_container = BubbleContainer(body=body)
					print(push_mssage_container)
					#flexMsg['header']['contents'][0]['url'] = group.picture_url
					# Push message that contain keyword to User,Group,Room 
				line_bot_api.push_message(mention_id, FlexSendMessage(contents=push_mssage_container))
				# Reply "Read" message to Chanel if contain keyword occur 
				line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Read'))
				break
			except LineBotApiError as e:
				# error handle
				print("Got exception from LINE Messaging API: %s\n" % e.message)
	
			