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

ask_for_input_string = "What's your next move?"

valid_move_string = "Please enter a valid move"

space_occupied = "Sorry, this space is occupied. Try other number"

rule_string = 'RULES'

win_message = 'Hooray! You have won the game! Type PLAY to start again'

lose_message = 'Sorry, you lost. Type PLAY to start again'

tie_message = 'Well, the game is a tie. Type PLAY to start again'

expected_greetings = ['hi', 'hello']
language = ['language', 'ru', 'en']
rules_request = ['rules', 'help']
start = ['play', 'start']
turn = ['\d']

greeting_reaction = 'greeting reaction'

ask_again = 'I don\'t understand you'

lang_confirmation = 'Language changed'