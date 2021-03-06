# https://gist.github.com/jjlumagbas/40ac3e6cd568d81ebb83e9d5575004bc
import getpass

def get_player_bid(max_amount, text='player bid: '):
    bid = -1

    while True:
        try:
            bid = int(getpass.getpass(text))
        except ValueError:
            print('Invalid input, try again')
            continue

        if bid > max_amount:
            print('You bid more than you own! Try again')
        elif bid < 0:
            print("dude you can't bid a negative amount. Try again")
        else:
            return bid

def get_player_bids(player1, amount1, player2, amount2):
    bid1 = get_player_bid(amount1, f'{player1} bid: ')
    bid2 = get_player_bid(amount2, f'{player2} bid: ')
    print(f'{player1} bid {bid1}, {player2} bid {bid2}')

    while bid1 == bid2:
        print('Both players bids are the same! Bid again:')
        bid1 = get_player_bid(amount1, f'{player1} bid: ')
        bid2 = get_player_bid(amount2, f'{player2} bid: ')
        print(f'{player1} bid {bid1}, {player2} bid {bid2}')
    
    return bid1, bid2

# Drawing the board by passing in current list of board. There are 9 elements in the dictionary each representing a position.            
def theBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Print amount of cash each player has
def status(player1name, player2name):
    print(f"{player1name} you have ${player1cash}")
    print(f"{player2name} you have ${player2cash}")

# get player's move (0 - 9)
def get_player_move(text):
    while True:
        try:
            move = int(input(text))
        except ValueError:
            print('Invalid input, try again')
            continue

        if move not in list(range(1, 10)):
            print(f'Invalid move: {move}')
            continue
        
        return str(move)

#Function that alters list that goes into theBoard. Letter corresponds to player1move or player2move
def makeMove(board, name, letter):
    prompt = "{}, please enter a number from 1-9 representing your play " 
    move = get_player_move(prompt.format(name))

    while board[move] != ' ': 
        print('That space has been taken up already, please enter another number')
        move = get_player_move(prompt.format(name))

    board[move] = letter

#Check if player has won
def get_winner():
    # return piece (X or O) of winning player
    # returns None if there's no winner

    if board['7'] == board['8'] == board['9'] != ' ': # across the top
        return board['7']

    elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
        return board['4']  

    elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
        return board['1']    

    elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
        return board['1']     

    elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
        return board['2']

    elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
        return board['3']  

    elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
        return board['7']   

    elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
        return board['1']

    return None

#Initialisation of initial cash, letters of each player,and empty gameboard
player1move = 'X'
player2move = 'O'


#Main Game
def game():
    global player1cash
    global player2cash

    player1name = input("Player 1, what is your name? ")
    player2name = input("Player 2, what is your name? ")
    winner = None

    for turn in range(9):
        status(player1name, player2name) #Prints cash
        theBoard(board) #Displays board
        player1bid, player2bid = get_player_bids(
            player1name, player1cash,
            player2name, player2cash
        )

        if player1bid > player2bid:
            player2cash += player1bid
            player1cash -= player1bid
            print(f"{player1name} wins the bid")
            makeMove(board, player1name, player1move)

        else: 
            player1cash += player2bid
            player2cash -= player2bid
            print(f"{player2name} wins the bid")
            makeMove(board, player2name, player2move)

        winner = get_winner()
        theBoard(board)

        if winner == player1move:
            print(f'{player1name} won!')
            break
        elif winner == player2move:
            print(f'{player2name} won!')
            break

    if winner is None:
        print('No more empty pieces. Game is a draw')

player1cash = 100
player2cash = 100

# Introduction
print("Hello! Welcome to Bidding Tic-Tac-Toe. \n [Insert Description of Game and Rules] \n Both players start with $100")
print("Player 1 is X and Player 2 is O. The board is arranged like a number pad with your play being a number from 1-9")

# The empty board
board = {str(k): ' ' for k in range(1, 10)}


if __name__ == '__main__':
    game()