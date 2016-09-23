# coding=utf-8
import emoji


class States():
    IN_GAME = 'IN_GAME'
    NEW = 'NEW'
    EXISTING = 'EXISTING'


class MsgTypes():
    EMOJI = 'EMOJI'
    UNCLASSIFIED = 'UNCLASSIFIED'
    GREETING = 'GREETING'
    LANGUAGE = 'LANGUAGE'
    RULES = 'RULES'
    HELP = 'HELP'
    START = 'START'
    TURN = 'TURN'


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
        for alias, lang in cls.choices():
            if lang in locale.upper():
                return lang
        else:
            return default


class Postbacks(Choise):
    ACCEPT_EMOJI = 'ACCEPT_EMOJI'
    DECLINE_EMOJI = 'DECLINE_EMOJI'
    START_NEW_GAME = 'PAYLOAD_START_NEW_GAME'


emojis = [(emoji.emojize(':strawberry:'), emoji.emojize(':banana:')),
          ()]
