# coding=utf-8
rules_part1 = '''
Two players take turns marking the spaces in a 3x3 grid with X and O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
This is a grid where we shall play.
_ | _ | _
_ | _ | _
_ | _ | _
'''

rules_part2 = '''Each space has its number:
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
Just type a number to make your move - and that's it!
'''

rules_option = '''
Let's play Tic-tac-toe!
To read how to play type RULES.
To start playing type a number between 1-9
'''

ask_for_move = "What's your next move?"

valid_move_string = "Please enter a valid move"

space_occupied = "Sorry, this space is occupied. Try other number"

rule_string = 'RULES'

win_message = 'Hooray! You have won the game! Type PLAY to start again'

lose_message = ['Sorry, you lost. Type PLAY to start again']

tie_message = 'Well, the game is a tie. Type PLAY to start again'

expected_greetings = ['hi', 'hello', 'hallo', 'good morning', 'good afternoon', 'good evening', 'wassup']
language = ['language', 'ru', 'en']
rules_request = ['rules', 'help']
start = ['play', 'start']
turn = ['\d']

greeting_reaction = 'greeting reaction'
greeting_reactions = ['Hi, {username}. Let\'s play!,
                      'Howdy. I\'m here to play with you,
                      'Oh, hello. Let\'s start!',
                      'Hi there. Wanna play with me?',
                      'Wassup!!! Play with me!',
                      'Thanks for stopping by, {username}. Let\'s start!'
                      ]
late_greeting_reaction = 'late greeting reaction'

ask_again = ['I need to ask someone what you mean',
             'Sorry, I don’t get it',
             'I should have lost my babel fish, as I don’t understand you',
             'Can you repeat once again?',
             'Maybe we should find an interpreter? ']

lang_confirmation = 'Language changed'

good_start = 'Good start!'

one_left = 'Only one move left. Come on!'

propose_emojis = "Do you want to play with strawberries and bananas?"

human_requests = ['human',
                  'chat',
                  'talk',
                  'order',
                  'shop',
                  'купит',
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

prompt_human_request = "Would you like to talk to a human being?"
confirm_human = 'The operator will join the conversation soon. Please write your question'

stats = 'Games total: {total}\nWins: {wins}\nTies: {ties}\nLosses: {losses}'

# (prompt msg, cancel title, confirm title)
prompt_for_new_game = ('Are you sure you want to start a new game?', 'Resume game', 'New game')
basic_prompt = ('Are you sure?', 'Cancel', 'Confirm')

id_request = ['SHOW MY ID PLEASE']