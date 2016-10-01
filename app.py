# coding=utf-8
import logging

import sys

from psycopg2._psycopg import InternalError

from flask import Flask, request, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import requests
from sqlalchemy.exc import OperationalError, ProgrammingError

app = Flask(__name__, static_url_path='')
app.config.from_pyfile('config.py')
app.config.from_pyfile('phrases_config.py')
app.config['SECRET_KEY'] = 'top-secret!'
app.config['LOGFILE'] = 'application.log'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')#'postgresql://localhost/tictactoebot'


db = SQLAlchemy(app)

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


@app.route('/stats', methods=['GET'])
def stats():
    from models import User
    try:
        stats = User.query.limit(250).all()
        return render_template('stats.html', users=stats)
    except ProgrammingError:
        db.create_all()


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
            events = output['entry'][0]['messaging']
            for msg_event in events:
                if msg_event.get('message') and msg_event['message'].get('text'):
                    message = msg_event['message']['text']
                    recipient_id = msg_event['sender']['id']
                    app.logger.info(u'Message from {0}:\n\t{1}'.format(recipient_id,message))
                    tictactoe.process_user_input(recipient_id, message)
                    db.session.commit()
                elif msg_event.get('postback'):
                    recipient_id = msg_event['sender']['id']
                    postback = msg_event['postback']
                    app.logger.info('postback received from {}'.format(recipient_id))
                    if 'payload' in postback:
                        app.logger.info('payload: {}'.format(postback['payload']))
                        tictactoe.process_postback(user_id=recipient_id, payload=postback['payload'])
                        db.session.commit()
                else:
                    pass
        except ProgrammingError:
            db.create_all()
        except InternalError:
            db.session.rollback()
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