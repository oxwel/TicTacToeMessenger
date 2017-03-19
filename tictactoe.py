# coding=utf-8
# Tic Tac Toe
from __future__ import unicode_literals

import random

import os
import re
import requests
from app import db
from flask import current_app as app
from models import User
from reactions import text_message_sender, send_text_message, multiple_messages_sender, start_btn, \
    MsgWithButtons, confirm_ask_human, decline_ask_human, accept_emoji, decline_emoji, cancel, confirm, stats_btn, \
    with_buttons, rules_btn, send_notification, lang_buttons
from static import States, MsgTypes, Langs, Postbacks, emojis, emoji_blank
from requests.exceptions import ConnectionError

player_sessions = {}
message_strings = None


def drawBoard(board, player_id, session):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    index = 1
    message = ''
    while index < 10:
        message += ' '.join(board[index:index + 3])
        message += '\n'
        index += 3

    emoji = session.emoji
    if emoji:
        message = message.replace('X', emoji[0])
        message = message.replace('O', emoji[1])
        message = message.replace('_', emoji_blank)

    send_text_message(player_id, message)


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == '_'


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


def isBoardEmpty(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if not isSpaceFree(board, i):
            return False
    return True


def get_user_profile(player_id):
    payload = {'fields': 'first_name,locale,last_name',
               'access_token': os.environ['PAGE_ACCESS_TOKEN']}
    url = "https://graph.facebook.com/v2.6/{user_id:s}".format(user_id=player_id)
    try:
        resp = requests.get(url, params=payload)
        return resp.json()
    except ConnectionError:
        return {}


class Session(object):
    def __init__(self, user_id):
        self.board = None
        self.play_first = True
        self.state = States.NEW
        self.previous_state = None
        self.callback = None

        profile = get_user_profile(user_id)

        self.name = profile.get('first_name')
        self.lang = Langs.read_locale(profile.get('locale'), Langs.EN)
        self.emoji = False
        self.profile = profile
        self.user_id = user_id

    def reset(self):
        self.board = None
        self.play_first = not self.play_first
        self.state = States.NEW


def get_session(user_id):
    session = player_sessions.get(user_id)
    if session is None:
        session = Session(user_id)
        player_sessions[user_id] = session
    return session


def send_rules_option(player_id, send_message):
    send_message(player_id, message_strings.rules_option)


def send_language_option(player_id, send_message):
    language_option = '''
    If you speak English type EN.
    If you speak Russian type RU.
    '''
    send_message(player_id, language_option)


def set_lang(message, **kw):
    if message and Langs.RU in message.upper():
        import strings_ru as message_strings_local
    elif message and Langs.UA in message.upper():
        import strings_ua as message_strings_local
    else:
        import strings_en as message_strings_local
    global message_strings
    message_strings = message_strings_local


def make_computer_move(player_id, session):
    """

    :type session: Session
    """
    board = session.board

    if board.count('_') == 9:
        send_text_message(player_id, message_strings.good_start)

    move = getComputerMove(board, 'O')
    makeMove(board, 'O', move)
    drawBoard(board, player_id, session)
    if isWinner(board, 'O'):
        MsgWithButtons([start_btn, stats_btn], message_strings.lose_message).send(player_id)
        # send_text_message(player_id, message_strings.lose_message)
        session.reset()
        user = User.query.filter_by(fb_id=player_id).first()
        user.losses += 1
        db.session.add(user)
    elif isBoardFull(board):
        MsgWithButtons([start_btn, stats_btn], message_strings.tie_message).send(player_id)
        # send_text_message(player_id, message_strings.tie_message)
        session.reset()
        user = User.query.filter_by(fb_id=player_id).first()
        user.ties += 1
        db.session.add(user)
    elif board.count('_') <= 3:
        send_text_message(player_id, message_strings.one_left)
    session.board = board


def make_player_move(user_id, session, message):
    """

    :type session: Session
    """
    try:
        move = int(message)
    except:
        send_text_message(user_id, message_strings.valid_move_string)
        return False
    board = session.board
    if move < 1 or move > 9:
        send_text_message(user_id, message_strings.valid_move_string)
        return False
    elif not isSpaceFree(board, move):
        send_text_message(user_id, message_strings.space_occupied)
        return False
    else:
        makeMove(board, 'X', move)
        drawBoard(board, user_id, session)
        if isWinner(board, 'X'):
            MsgWithButtons([start_btn, stats_btn], message_strings.win_message).send(user_id)
            if not session.emoji:
                propose_emojis(user_id)
            session.reset()
            user = User.query.filter_by(fb_id=user_id).first()
            user.wins += 1
            db.session.add(user)
            return False
        elif isBoardFull(board):
            MsgWithButtons([start_btn, stats_btn], message_strings.tie_message).send(user_id)
            session.reset()
            user = User.query.filter_by(fb_id=user_id).first()
            user.ties += 1
            db.session.add(user)
            return False
        else:
            make_computer_move(user_id, session)
    return True


def change_lang(user_id, session, message):
    session.lang = Langs.read(message, default=Langs.EN)
    set_lang(session.lang)
    send_text_message(user_id, message_strings.lang_confirmation)


def ask_for_move(user_id):
    send_text_message(user_id, message_strings.ask_for_move)


def new_board():
    return ['_'] * 10


def start_the_game(user_id, session, message):
    user = User.query.filter_by(fb_id=user_id).first()
    if user is None:
        user = User(fb_id=user_id)
    user.games += 1
    db.session.add(user)

    session.state = States.IN_GAME
    session.board = new_board()
    if session.play_first:
        ask_for_move(user_id)
    else:
        make_computer_move(user_id, session)


def turn_emoji(user_id, session, message):
    if message == Postbacks.ACCEPT_EMOJI:
        session.emoji = random.choice(emojis)
    elif message == Postbacks.DECLINE_EMOJI:
        session.emoji = False


def greeting(username):
    text = random.choice(message_strings.greeting_reactions).format(username=username)
    return text_message_sender(text)

def send_id(user_id, session, message):
    send_text_message(user_id, str(user_id))

def greeting_new(user_id, session, message):
    text = random.choice(message_strings.greeting_reactions).format(username=session.name)
    MsgWithButtons([start_btn], text).send(user_id)


def ask_human(user_id, session, message):
    MsgWithButtons([confirm_ask_human, decline_ask_human], message_strings.prompt_human_request).send(user_id)


def call_human(user_id, session, message):
    send_notification(session.profile)
    send_text_message(user_id, message_strings.confirm_human)


def _continue(**kwargs):
    pass


def propose_emojis(user_id):
    MsgWithButtons([accept_emoji, decline_emoji], message_strings.propose_emojis).send(user_id)


def show_stats(user_id, **kwargs):
    user = User.query.filter_by(fb_id=user_id).first()
    msg = message_strings.stats.format(total=user.games,
                                       wins=user.wins,
                                       losses=user.losses,
                                       ties=user.ties)
    MsgWithButtons([start_btn, rules_btn], msg).send(user_id)


def make_sure(action, msg_type):
    # msg_type: (prompt msg, cancel title, confirm title)
    MSGS = {
        MsgTypes.START: message_strings.prompt_for_new_game,
    }
    prompt_msg, cancel_title, confirm_title = MSGS.get(msg_type, message_strings.basic_prompt)
    def with_sure(user_id, session, message):
        """

        :type session: Session
        """
        session.previous_state = session.state
        session.state = States.PROMPT
        session.callback = action
        MsgWithButtons([cancel(cancel_title), confirm(confirm_title)], prompt_msg).send(user_id)
    return with_sure


def do_cancel(user_id, session, message):
    session.state = session.previous_state
    session.callback = None


def do_confirm(user_id, session, message):
    callback = session.callback
    session.callback = None
    callback(user_id, session, message)


def get_reaction(state, msg_type, username):
    """
    :rtype: function
    """
    REACTIONS = {
        States.NEW: {
            MsgTypes.MY_ID: send_id,
            MsgTypes.GREETING: greeting_new,
            MsgTypes.LANGUAGE: change_lang,
            MsgTypes.RULES: with_buttons(text_message_sender, [start_btn], message_strings.rules_part2)(message_strings.rules_part1),
            MsgTypes.START: start_the_game,
            MsgTypes.UNCLASSIFIED: text_message_sender(random.choice(message_strings.ask_again)),
            MsgTypes.EMOJI: turn_emoji,
            MsgTypes.ASK_HUMAN: ask_human,
            MsgTypes.CALL_HUMAN: call_human,
            MsgTypes.CONTINUE: _continue,
            MsgTypes.STATS: show_stats,
            MsgTypes.LANG_REQUEST: lambda user_id, **kw: MsgWithButtons(lang_buttons, 'Choose language:').send(user_id)
        },
        States.IN_GAME: {
            MsgTypes.MY_ID: send_id,
            MsgTypes.GREETING: greeting(username),
            MsgTypes.LANGUAGE: change_lang,
            MsgTypes.RULES: multiple_messages_sender(message_strings.rules_part1, message_strings.rules_part2),
            MsgTypes.TURN: make_player_move,
            MsgTypes.UNCLASSIFIED: text_message_sender(message_strings.rules_part2),
            MsgTypes.START: make_sure(start_the_game, msg_type),
            MsgTypes.EMOJI: turn_emoji,
            MsgTypes.ASK_HUMAN: ask_human,
            MsgTypes.STATS: show_stats,
        },
        States.PROMPT: {
            MsgTypes.MY_ID: send_id,
            MsgTypes.CANCEL: do_cancel,
            MsgTypes.CONFIRM: do_confirm,
        }
    }
    return REACTIONS[state].get(msg_type, text_message_sender(random.choice(message_strings.ask_again)))


def pattern(s):
    return ur'\b{0:s}\b'.format(s)


def classify_msg(message):
    clues = {
        MsgTypes.GREETING: message_strings.expected_greetings,
        MsgTypes.LANGUAGE: message_strings.language,
        MsgTypes.RULES: message_strings.rules_request,
        MsgTypes.START: message_strings.start,
        MsgTypes.TURN: message_strings.turn,
        MsgTypes.ASK_HUMAN: message_strings.human_requests,
        MsgTypes.MY_ID: message_strings.id_request
    }
    for msg_type, clues in clues.items():
        if any([re.search(pattern(s), message, re.UNICODE) for s in clues]):
            return msg_type
    else:
        return MsgTypes.UNCLASSIFIED


def process_user_input(user_id, message):
    session = get_session(user_id)
    state = session.state
    set_lang(session.lang)
    msg_type = classify_msg(message)
    get_reaction(state, msg_type, session.name)(user_id=user_id, session=session, message=message)


def identify_postback(payload):
    return {Postbacks.START_NEW_GAME: MsgTypes.START,
            Postbacks.ACCEPT_EMOJI: MsgTypes.EMOJI,
            Postbacks.DECLINE_EMOJI: MsgTypes.EMOJI,
            Postbacks.ASK_HUMAN: MsgTypes.CALL_HUMAN,
            Postbacks.DECLINE_HUMAN: MsgTypes.CONTINUE,
            Postbacks.SHOW_STATS: MsgTypes.STATS,
            Postbacks.CONFIRM: MsgTypes.CONFIRM,
            Postbacks.CANCEL: MsgTypes.CANCEL,
            Postbacks.RULES: MsgTypes.RULES,
            Postbacks.CHAT: MsgTypes.CALL_HUMAN,
            Postbacks.LANG: MsgTypes.LANG_REQUEST,
            Postbacks.EN: MsgTypes.LANGUAGE,
            Postbacks.RU: MsgTypes.LANGUAGE,
            Postbacks.UA: MsgTypes.LANGUAGE,
            }.get(payload, MsgTypes.UNCLASSIFIED)


def process_postback(user_id, payload):
    session = get_session(user_id)
    state = session.state
    set_lang(session.lang)
    msg_type = identify_postback(payload)
    get_reaction(state, msg_type, session.name)(user_id=user_id, session=session, message=payload)
