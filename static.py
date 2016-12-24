# coding=utf-8
import emoji


class States():
    PROMPT = 'PROMPT'
    IN_GAME = 'IN_GAME'
    NEW = 'NEW'
    EXISTING = 'EXISTING'


class MsgTypes():
    CANCEL = 'CANCEL'
    CONFIRM = 'CONFIRM'
    CONTINUE = 'CONTINUE'
    CALL_HUMAN = 'CALL_HUMAN'
    EMOJI = 'EMOJI'
    UNCLASSIFIED = 'UNCLASSIFIED'
    GREETING = 'GREETING'
    LANGUAGE = 'LANGUAGE'
    RULES = 'RULES'
    HELP = 'HELP'
    START = 'START'
    TURN = 'TURN'
    ASK_HUMAN = 'ASK_HUMAN'
    STATS = 'STATS'


class Choise:
    @classmethod
    def choices(cls):
        return [(k, v) for k, v in cls.__dict__.items() if isinstance(v, str) and not k.startswith('__')]

    @classmethod
    def read(cls, message, default):
        for alias, lang in cls.choices():
            if message.upper() == lang:
                return lang
        else:
            return default


class Langs(Choise):
    EN = 'EN'
    RU = 'RU'

    @classmethod
    def read_locale(cls, locale, default):
        if not locale:
            return default
        for alias, lang in cls.choices():
            if lang in locale.upper():
                return lang
        else:
            return default


class Postbacks(Choise):
    RULES = 'RULES'
    CONFIRM = 'CONFIRM'
    CANCEL = 'CANCEL'
    DECLINE_HUMAN = 'DECLINE_HUMAN'
    ASK_HUMAN = 'ASK_HUMAN'
    ACCEPT_EMOJI = 'ACCEPT_EMOJI'
    DECLINE_EMOJI = 'DECLINE_EMOJI'
    START_NEW_GAME = 'PAYLOAD_START_NEW_GAME'
    SHOW_STATS = 'PAYLOAD_STATISTICS'


emoji_blank = emoji.emojize(':white_medium_square:')
emojis = [(emoji.emojize(':strawberry:'), emoji.emojize(':banana:')),
          ]
