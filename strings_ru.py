# coding=utf-8
from __future__ import unicode_literals

rules_part1 = '''
Играть очень просто! Два игрока ходят по очереди, заполняя свободные клетки поля размером 3х3 крестиками (Х) и ноликами (О). Игрок, которому удастся выстроить в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.
_ | _ | _
_ | _ | _
_ | _ | _
'''

rules_part2 = '''У каждой клетки свой номер:
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
Чтобы сделать ход, просто введи число. Вперед!
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

win_message = 'Ура!!! Победа твоя!'

lose_message = ['Ой, тебе не повезло на этот раз',
                'Прости, я выиграл. Еще одну партию?',
                'Иногда ты ешь медведя, иногда медведь ест тебя;)',
                'Просто я не люблю проигрывать. Давай езе раз?'
               ]

tie_message = ['Победила дружба! Давай еще',
               'Ничья. Еще разок?',
               'Мы с тобой достойные соперники!',
               'Никто не любит проигрывать. И прекрасно!'
              ]

expected_greetings = ['привет', 'прив', 'добрый день', 'доброе утро', 'добрый вечер', 'здравствуй', 'здравствуйте',
                      'хай', 'хей', 'хелло', 'йоу']
language = ['language', 'ru', 'en']
rules_request = ['rules', 'help']
start = ['play', 'start']
turn = ['\d']

greeting_reaction = 'greeting reaction ru'
greeting_reactions = ['Привет, {username}. Поиграем?',
                      'Приветы! Давай играть',
                      'Бонжур. Начнем?',
                      'Привет-привет! Сыграем?',
                      'Хей, {username}, рад тебя снова видеть! Давай играть',
                      'Йоу, {username}. Жми уже на кнопку Play!',
                      'Классно, что помнишь про меня! Начнем?'
                      ]
late_greeting_reaction = 'late greeting reaction ru'

ask_again = ['Что-то я тебя не понимаю',
             'Попробуй выбрать что-то в меню',
             'Что ты имеешь в виду?',
             'Если хочешь сыграть, набери Play',
             'Может поиграем? Введи Play',
             'В каком смысле?',
             'Вроде вчера не пил, но голова плохо соображает. Что-что?',
             'Можешь повторить то же самое, только другими словами?'
            ]

lang_confirmation = 'Язык изменен'

good_start = ['Отличное начало!',
              'Хороший ход',
              'Неожиданно',
              'Похоже на новую стратегию',
              'Неплохо-неплохо',
              'А ты гроссмейстер!',
              'Что же делать, что же делать?',
              'Так, а что ты на это скажешь?',
              'А я вот так!',
              'Хм. Ладно'
              ]

one_left = ['Давай же, остался всего один ход!',
            'Так, последний ход',
            'Интересно, как же ты походишь???',
            'Ну давай уже',
            'Сделай это!',
            'Смотри, не ошибись',
            'Может подумаешь хорошенько?'
            ]

propose_emojis = "Как насчет того, чтобы поиграть с клубничкой?:)"

human_requests = ['купит',
                  'поддержк',
                  'говорит',
                  'общаться',
                  'уточн',
                  'оператор',
                  'менеджер',
                  'заказ',
                  'телефон',
                  'замовлення',
                  'артикул',
                  'налич',
                  'магазин']

prompt_human_request = "Вы хотите связаться с менеджером магазина GameClub?"
confirm_human = 'Я сейчас позову кого-то, кто сможет с вами поговорить. А пока напишите, что именно вы хотите уточнить'

stats = 'Всего игр: {total}\nПобеды: {wins}\nНичьи: {ties}\nПоражения: {losses}'

prompt_for_new_game = (
'Перед тем, как начать новую игру, я хочу убедиться, что ты находишься в трезвом уме и твердой памяти. Точно хочешь начать новую игру?',
'Вернуться к игре', 'Новая игра')
basic_prompt = ('Точно?', 'Отмена', 'Да')

id_request = ['SHOW MY ID PLEASE']