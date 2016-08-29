import logging
from logging.handlers import RotatingFileHandler

import sys

from flask import Flask, request, send_from_directory
import os
import requests

app = Flask(__name__, static_url_path='')
app.config.from_pyfile('config.py')
app.config.from_pyfile('phrases_config.py')
app.config['SECRET_KEY'] = 'top-secret!'
app.config['LOGFILE'] = 'application.log'

# file_handler = RotatingFileHandler(app.config['LOGFILE'], 'w', 1 * 1024 * 1024, 10)
# file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.setLevel(logging.INFO)
# file_handler.setLevel(logging.INFO)
stdout_handler.setLevel(logging.INFO)
app.logger.addHandler(stdout_handler)
app.logger.info('Application startup\nVersion: {}'.format(app.config['VERSION']))

import tictactoe


@app.route('/okmijnsecretpath', methods=['GET'])
def logs():
    return send_from_directory('.', app.config['LOGFILE'])


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == os.environ['VERIFY_TOKEN']:
            return request.args.get("hub.challenge")
        else:
            return "Error, wrong validation token"
    else:
        try:
            output = request.json
            event = output['entry'][0]['messaging']
            for x in event:
                if x.get('message') and x['message'].get('text'):
                    message = x['message']['text']
                    recipient_id = x['sender']['id']
                    app.logger.info('Message from {0}:\n\t{1}'.format(recipient_id,message))
                    tictactoe.get_next_step(recipient_id, message, send_message)
                else:
                    pass
        except Exception, e:
            print e
        return "failure"


def send_to_server(payload, url):
    result = requests.post(url, json=payload)
    print result.json()
    return result.json()


def send_message(recipient_id, message):
    payload = {'recipient': {'id': recipient_id},
               'message': {'text': message}
               }
    print payload
    url = 'https://graph.facebook.com/v2.6/me/messages?access_token={}'.format(os.environ['PAGE_ACCESS_TOKEN'])
    send_to_server(payload, url)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0',port=port)