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
	# print(event.source)
	for word in keywords:
		if word in text:
			try:
				#profile = line_bot_api.get_profile(event.source.user_id)
				#Compose message for forwarding to user
				if isinstance(event.source, SourceGroup):
					profile = line_bot_api.get_group_member_profile(event.source.group_id,event.source.user_id)
				#### HERO BLOCK ####
					header_components = list()
					header_user_icon = IconComponent(url=profile.picture_url,size='3xl')
					header_recvd_msg = TextComponent(text=profile.display_name,size='md')
					header_components.append(header_user_icon)
					header_components.append(header_recvd_msg)
					header = BoxComponent(contents=header_components,layout='baseline', spacing='md')
				#### END HERO BLOCK ###

				#### BODY BLOCK ####
				# Build flex message body as message push 
					body_components = list()
					#user_icon = IconComponent(url=profile.picture_url,size='xl')
					recvd_msg = TextComponent(text=text,size='md',wrap=True)
					#body_components.append(user_icon)
					body_components.append(recvd_msg)
					body = BoxComponent(contents=body_components,layout='baseline')
				#### END BODY BLOCK ###
					bubbleContainer = BubbleContainer(header=header,body=body)
					flex = FlexSendMessage(contents=bubbleContainer,alt_text=word)

				elif isinstance(event.source, SourceUser):
					profile = line_bot_api.get_profile(event.source.user_id)
				#### HERO BLOCK ####
					header_components = list()
					header_user_icon = IconComponent(url=profile.picture_url,size='3xl')
					header_recvd_msg = TextComponent(text=profile.display_name,size='md')
					header_components.append(header_user_icon)
					header_components.append(header_recvd_msg)
					header = BoxComponent(contents=header_components,layout='baseline', spacing='md')
				#### END HERO BLOCK ###

				#### BODY BLOCK ####
				# Build flex message body as message push 
					body_components = list()
					#user_icon = IconComponent(url=profile.picture_url,size='xl')
					recvd_msg = TextComponent(text=text,size='md',wrap=True)
					#body_components.append(user_icon)
					body_components.append(recvd_msg)
					body = BoxComponent(contents=body_components,layout='baseline')
				#### END BODY BLOCK ###
					bubbleContainer = BubbleContainer(header=header,body=body)
					flex = FlexSendMessage(contents=bubbleContainer,alt_text=word)
					# Push message that contain keyword to User,Group,Room 
				line_bot_api.push_message(mention_id,flex)
				# push_text = profile.display_name + ' > ' + text
				# line_bot_api.push_message(mention_id, TextSendMessage(text=push_text))
				# Reply "Read" message to Chanel if contain keyword occur 
				line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Read'))
				break
			except LineBotApiError as e:
				# error handle
				print("Got exception from LINE Messaging API: %s\n" % e)
	
			
