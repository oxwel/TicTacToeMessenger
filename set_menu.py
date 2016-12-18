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
        postback_item('Start new game', Postbacks.START_NEW_GAME),
        postback_item('Show stats', Postbacks.SHOW_STATS),
        postback_item('Show rules', Postbacks.RULES)
    ],
    access_token).content