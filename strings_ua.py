# coding=utf-8
from __future__ import unicode_literals

rules_part1 = '''
Два игрока ходят по очереди, заполняя свободные клетки поля размером 3х3 крестиками (Х) и ноликами (О). Игрок, которому удастся выстроить в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.
_ | _ | _
_ | _ | _
_ | _ | _
'''

rules_part2 = '''У каждой клетки свой номер:
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
Чтобы сделать ход, просто введи число!
'''

rules_option = '''
Сыграем в Крестики-нолики?
Чтобы узнать, как играть, напиши RULES.
Для начала игры напиши число от 1 до 9
'''

ask_for_move = "Твой ход!"

valid_move_string = "Что-то не то. Введи правильное число."

space_occupied = "Эта клетка занята. Введи другое число"

rule_string = 'RULES'

win_message = 'Ура!!! Ты выиграл!'

lose_message = 'Ой, ты проиграл.'

tie_message = 'Победила дружба!'

expected_greetings = ['hi', 'hello']
language = ['language', 'ru', 'en']
rules_request = ['rules', 'help']
start = ['play', 'start']
turn = ['\d']

greeting_reaction = 'greeting reaction ru'
greeting_reactions = ['Hi, {username}',
                      'Howdy',
                      'Oh, hello',
                      'Wassup!',
                      '{username}, glad to see you again!',
                      'Hi there',
                      'Thanks for stopping by, {username}!'
                      ]
late_greeting_reaction = 'late greeting reaction ru'

ask_again = ['Не понимаю']

lang_confirmation = 'Язык изменен'

good_start = 'Гуд start!'

one_left = 'Онли one move left. Come on!'

propose_emojis = "Ду ю want to play with strawberries and bananas?"

human_requests = ['Human',
                  'Chat',
                  'Talk',
                  'Order',
                  'Shop']

prompt_human_request = "Would you лайк to talk to a human being?"
confirm_human = 'The оператор will join the conversation soon. Please write your question'

stats = 'Games total: {total}\nWins: {wins}\nTies: {ties}\nLosses: {losses}'

prompt_for_new_game = ('Are you sure you want to start a new game?', 'Resume game', 'New game')
basic_prompt = ('Are you sure?', 'Cancel', 'Confirm')