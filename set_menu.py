import json

import sys

import os

import requests
from static import Postbacks


def set_menu(menu_items, acces_token):
    menu_json = {
        "setting_type": "call_to_actions",
        "thread_state": "existing_thread",
        "call_to_actions": menu_items
    }
    prepared_request = requests.Request('POST',
                               'https://graph.facebook.com/v2.6/me/thread_settings',
                               json=menu_json,
                               params={'access_token': acces_token}).prepare()
    response = requests.Session().send(prepared_request)
    return response


def postback_item(title, payload):
    return {
        "type": "postback",
        "title": title,
        "payload": payload,
    }


def read(filename):
    with open(filename) as f:
        content = f.read()
    return content


if __name__ == '__main__':
    access_token=read('pat.txt')
    print set_menu([
        postback_item('Start New Game', Postbacks.START_NEW_GAME),
        postback_item('Explain Rules', Postbacks.RULES),
        postback_item('Show Stats', Postbacks.SHOW_STATS),
        postback_item('Change Language', Postbacks.LANG),
        postback_item('Chat with Operator', Postbacks.CHAT)
    ],
    access_token).content