import random
# for random moves by the user

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
# grid architecture
currentPlayer = "X"
# keeps track of turn
winner = None
#value of the winner
gameRunning = True
#checks whether game is in progress or not

# Printing game board
def printBoard(board):
         #prints the cuurent state
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Player's input
def playerInput(board):
         #player to input the move
    global currentPlayer  
    # Declare as global
    inp = int(input(f"Player {currentPlayer}, enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
             #range between 1 to 9
        board[inp - 1] = currentPlayer
    else:
        print("Spot is already taken! Try again.")
        playerInput(board)

# Check for win or tie
def checkHorizontle(board):
         #checks for horzontal win
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

def checkRow(board):
         #checks for vertical win
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkDiag(board):
         #resulting diagonals
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkTie(board):
         # resulting in a tie 
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False

def checkWin(board):
         # checks for any type of win
    global winner
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")
        return True
    return False

# Switch player
def switchPlayer():
         #changes turn to other players
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Computer makes a move
def computer(board):
         #random selection of spot
    global currentPlayer
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            break

# Main game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    if checkWin(board):
        gameRunning = False
        break
    checkTie(board)
    if not gameRunning:
        break
    switchPlayer()
    computer(board)
    if checkWin(board):
        gameRunning = False
        break
    checkTie(board)
    if not gameRunning:
        break
    switchPlayer()
