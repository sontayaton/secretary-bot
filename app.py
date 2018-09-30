from __future__ import unicode_literals

import errno
import os
import sys
import tempfile
from argparse import ArgumentParser

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,SourceUser, SourceGroup, SourceRoom,StickerMessage, StickerSendMessage,QuickReply)


app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            print("  %s: %s" % (m.property, m.message))
        print("\n")
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    
    msgforwarder.forwardMsgToUser(line_bot_api,event)



# Load the configuration file
#configuration_file = "config/config.ini"

#with open(configuration_file) as f:
#    app_config = f.read()
#config = ConfigParser.RawConfigParser(allow_no_value=True)
#config.readfp(io.BytesIO(app_config))

## Handler function

#def lambda_handler(event, context):

##	body = json.loads(event['body'])

#	for event in body['events']:

#		payload = {
#        	'replyToken': event['replyToken'],
 #       	'messages': []
#        }

#        if event['message']['type'] == 'text':

        	## Use forward MsgToUser Module ##
#        	msgforwarder.forwardMsgToUser(payload)

 #       elif event['message']['type'] == 'sticker':
 #           payload['messages'].append({
 #               'type': 'sticker',
 #               'stickerId': event['message']['stickerId'],
 #               'packageId': event['message']['packageId']
 #           })


if __name__ == "__main__":
    app.run()
        