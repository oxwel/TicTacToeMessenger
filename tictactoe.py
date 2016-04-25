# coding=utf-8
# Tic Tac Toe

import random
player_sessions = {}

def drawBoard(board, player_id, send_message):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    index = 1
    message = ''
    while index < 10:
        message += ' '.join(board[index:index+3])
        message += '\n'
        index += 3

    send_message(player_id, message)

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == '_'

def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

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


def get_existing_game(player_id):
    return player_sessions.get(player_id, None)


def ask_for_input(player_id, send_message):
    send_message(player_id, "What's your next move?")


def send_rules(player_id, send_message):
    rules_part1 = '''
    Two players take turns marking the spaces in a 3×3 grid with X and O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
    This is a grid where we shall play.
    _ | _ | _
    _ | _ | _
    _ | _ | _
    '''
    send_message(player_id, rules_part1)

    rules_part2 = '''Each space has its number:
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9
    Just type a number to make your move - and that's it!
    '''
    send_message(player_id, rules_part2)
    pass


def send_rules_option(player_id, send_message):
    rules_option = '''
        To know the Rules, type Rules.
        To start playing type a number between 1-9
    '''
    send_message(player_id, rules_option)


def get_next_step(player_id, message, send_message):
    player_id = str(player_id)
    board = get_existing_game(player_id)
    print "board:", board
    if not board:
        player_sessions[player_id] = ['_'] * 10
        send_rules_option(player_id, send_message)
        return
    elif message.upper() == 'RULES':
          send_rules(player_id, send_message)
    else:
        try:
            move = int(message)
        except:
            send_message(player_id, "Please enter a valid move")
            return
        if move < 0 or move > 9:
            send_message(player_id, "Please enter a valid move")
        elif not isSpaceFree(board, move):
            send_message(player_id, "Sorry, this space is occipied. Try another number")
        else:
            makeMove(board, 'X', move)
            if isWinner(board, 'X'):
                drawBoard(board, player_id, send_message)
                send_message(player_id, 'Hooray! You have won the game!')
                player_sessions.pop(player_id)
                return
            elif isBoardFull(board):
                drawBoard(board, player_id, send_message)
                send_message(player_id, 'The game is a tie!')
                player_sessions.pop(player_id)
                return
            else:
                move = getComputerMove(board, 'O')
                makeMove(board, 'O', move)

                if isWinner(board, 'O'):
                    drawBoard(board, player_id, send_message)
                    send_message(player_id, 'The computer has beaten you')
                    player_sessions.pop(player_id)
                    return
                elif isBoardFull(board):
                    drawBoard(board, player_id, send_message)
                    send_message(player_id, 'The game is a tie!')
                    player_sessions.pop(player_id)
                    return

        drawBoard(board, player_id, send_message)
    ask_for_input(player_id, send_message)


def playGame(palyer):
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    #if not playAgain():
        #break