# coding=utf-8
import json

import os
import requests
from app import app
from static import Postbacks


def call_send_api(message_data):
    r = requests.post('https://graph.facebook.com/v2.6/me/messages',
                      data=message_data,
                      params={'access_token': os.environ['PAGE_ACCESS_TOKEN']},
                      headers={'Content-Type': 'application/json'})
    app.logger.info('fb api response: {}'.format(r.content))


def send_text_message(recipient_id, text):
    app.logger.info('sending message to {}'.format(recipient_id))
    message_data = json.dumps({
        'recipient': {
            'id': recipient_id
        },
        'message': {
            'text': text
        }
    })
    call_send_api(message_data)


def text_message_sender(text):
    def f(user_id, **kwargs):
        return send_text_message(user_id, text)

    return f


def multiple_messages_sender(*messages):
    def f(user_id, **kwargs):
        for msg in messages:
            send_text_message(user_id, msg)

    return f


class PostbackButton(object):
    def __init__(self, title, payload):
        self.title = title
        self.payload = payload

    def dict(self):
        return {
            "type": "postback",
            "title": self.title,
            "payload": self.payload
        }

accept_emoji = PostbackButton('OK', Postbacks.ACCEPT_EMOJI)
decline_emoji = PostbackButton('Cancel', Postbacks.DECLINE_EMOJI)
start_btn = PostbackButton('Play!', Postbacks.START_NEW_GAME)
confirm_ask_human = PostbackButton('OK', Postbacks.ASK_HUMAN)
decline_ask_human = PostbackButton('Cancel', Postbacks.DECLINE_HUMAN)
cancel = lambda caption: PostbackButton(caption, Postbacks.CANCEL)
confirm = lambda caption: PostbackButton(caption, Postbacks.CONFIRM)
stats_btn = PostbackButton('Statistics', Postbacks.SHOW_STATS)

class MsgWithButtons(object):
    def __init__(self, buttons, text=None):
        self.text = text
        self.buttons = buttons

    def dict(self):
        return {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": self.text,
                    "buttons": [button.dict() for button in self.buttons]
                }
            }
        }

    def send(self, recipient_id):
        msg_data = json.dumps({"recipient": {"id": recipient_id},
                               "message": self.dict()})
        return call_send_api(msg_data)


