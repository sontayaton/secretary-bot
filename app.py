# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import errno
import os
import sys
import json
import tempfile
from linemodules.msgforwarder import msgforwarder
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


@app.route("/")
def hello():
    return 'OK'

def lambda_handler(event, context):
    body = event['body']
    signature = event['headers']['X-Line-Signature']
    print("Request body: " + str(event))
    callHandler(body,signature)
    return response({'message': 'OK'}, 200)

def response(message, status_code):
    return {
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
            },
        }



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print("Request body: " + body)

    result = callHandler(body,signature)
    return result

   

def callHandler(body,signature):
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
    
    ## Use Message Forwarder Module ##
    msgforwarder.forwardMsgToUser(line_bot_api,event)
    


if __name__ == "__main__":
    app.run()
