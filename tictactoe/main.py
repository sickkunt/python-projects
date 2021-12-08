import random

#def menu():

def pvp():
    table = ['_'] * 9
    tableCoordinates = [0,1,2,3,4,5,6,7,8]
    usedCoordinatesList = []
    turn = 0
    win = 0
    player1Choice = ''
    player2Choice = ''
    player1Turn = 0 #remember to erase memory
    player2Turn = 0 #remember to erase memory

    print("Welcome to tic-tac-toe. The objective of the game is to line up 3 x's or o's horizontally, vertically, or diagonally.\n")

    print("This is what the board looks like. The numbers correspond to the position on the board.\n")

    for i in range(0,8,3):
        print(f' {tableCoordinates[i]} | {tableCoordinates[i+1]} | {tableCoordinates[i+2]}')

    print()

    player1Choice = input("Player 1. Choose a symbol - 'x' or 'o': ").lower()
    while player1Choice != 'x' and player1Choice != 'o':
        player1Choice = input("Symbol can only be either 'x' or 'o'. Choose a symbol: ").lower()
    if player1Choice == 'x':
        player2Choice = 'o'
        print(f"Player 1 is '{player1Choice}'. Player 2 is '{player2Choice}'.")
    elif player1Choice == 'o':
        player2Choice = 'x'
        print(f"Player 1 is '{player1Choice}'. Player 2 is '{player2Choice}'.")

    while win == 0:
        player1Turn = int(input('Player 1. Enter a coordinate from 0 to 8: '))
        while player1Turn not in tableCoordinates:
            player1Turn = int(input(f'{player1Turn} is not a valid coordinate. Enter a coordinate from 0 to 8: '))
        while isinstance(table[player1Turn], str) == True and table[player1Turn] != '_':
            print()
            for i in range(0,8,3):
                print(f' {table[i]} | {table[i+1]} | {table[i+2]}')
            print()
            player1Turn = int(input(f"Player 1. {player1Turn}'s coordinate is already filled'. Enter a coordinate from 0 to 8 that isn't {usedCoordinatesList}: "))
        table.pop(player1Turn)
        table.insert(player1Turn, player1Choice)
        usedCoordinatesList.append(player1Turn)
        turn += 1

        print()
        for i in range(0,8,3):
            print(f' {table[i]} | {table[i+1]} | {table[i+2]}')
        print()

        if turn == 9:
            print("Neither Player 1 or Player 2 has won. Game will exit.")
            quit()
        win = is_win(table, player1Choice, player2Choice)
        if win == 1:
            print("Player 1 has won!")
            quit()
        elif win == 2:
            print("Player 2 has won!")
            quit()
        else:
            win = 0

        player2Turn = int(input('Player 2. Enter a coordinate from 0 to 8: '))
        while player2Turn not in tableCoordinates:
            player2Turn = int(input(f'{player2Turn} is not a valid coordinate. Enter a coordinate from 0 to 8: '))
        while isinstance(table[player2Turn], str) == True and table[player2Turn] != '_':
            print()
            for i in range(0,8,3):
                print(f' {table[i]} | {table[i+1]} | {table[i+2]}')
            print()
            player2Turn = int(input(f"Player 2. {player2Turn}'s coordinate is already filled'. Enter a coordinate from 0 to 8 that isn't {usedCoordinatesList}: "))
        table.pop(player2Turn)
        table.insert(player2Turn, player2Choice)
        usedCoordinatesList.append(player2Turn)
        turn += 1

        print()
        for i in range(0,8,3):
            print(f' {table[i]} | {table[i+1]} | {table[i+2]}')
        print()

        win = is_win(table, player1Choice, player2Choice)
        if win == 1:
            print("Player 1 has won!")
        elif win == 2:
            print("Player 2 has won!")
        else:
            win = 0

def is_win(table, player1Choice, player2Choice):
    player1row1Score = 0
    player2row1Score = 0
    player1row2Score = 0
    player2row2Score = 0
    player1row3Score = 0
    player2row3Score = 0

    #checking row 1
    for i in range(0,3):
        if table[i] == player1Choice:
            player1row1Score += 1
        elif table[i] == player2Choice:
            player2row1Score += 1
    if player1row1Score == 3:
        return 1
    elif player2row1Score == 3:
        return 2

    #checking row 2
    for i in range(3,6):
        if table[i] == player1Choice:
            player1row2Score +=1
        elif table[i] == player2Choice:
            player2row2Score +=1
    if player1row2Score == 3:
        return 1
    elif player2row2Score == 3:
        return 2

    #checking row 3
    for i in range(6,9):
        if table[i] == player1Choice:
            player1row3Score +=1
        elif table[i] == player2Choice:
            player2row3Score +=1
    if player1row3Score == 3:
        return 1
    elif player2row3Score == 3:
        return 2

    player1col1Score = 0
    player2col1Score = 0
    player1col2Score = 0
    player2col2Score = 0
    player1col3Score = 0
    player2col3Score = 0

    #checking column 1
    for i in range(0,8,3):
        if table[i] == player1Choice:
            player1col1Score +=1
        elif table[i] == player2Choice:
            player2col1Score +=1
    if player1col1Score == 3:
        return 1
    elif player2col1Score == 3:
        return 2

    #checking column 2
    for i in range(-8,0,3):
        if table[i] == player1Choice:
            player1col2Score +=1
        elif table[i] == player2Choice:
            player2col2Score +=1
    if player1col2Score == 3:
        return 1
    elif player2col2Score == 3:
        return 2

    #checking column 3
    for i in range(-7,1,3):
        if table[i] == player1Choice:
            player1col3Score +=1
        elif table[i] == player2Choice:
            player2col3Score +=1
    if player1col3Score == 3:
        return 1
    elif player2col3Score == 3:
        return 2

    player1diag1Score = 0
    player2diag1Score = 0
    player1diag2Score = 0
    player2diag2Score = 0

    #checking diagonal 1
    for i in range(0,9,4):
        if table[i] == player1Choice:
            player1diag1Score +=1
        elif table[i] == player2Choice:
            player2diag1Score +=1
    if player1diag1Score == 3:
        return 1
    elif player2diag1Score == 3:
        return 2

    #checking diagonal 2
    for i in range(2,7,2):
        if table[i] == player1Choice:
            player1diag2Score +=1
        elif table[i] == player2Choice:
            player2diag2Score +=1
    if player1diag2Score == 3:
        return 1
    elif player2diag2Score == 3:
        return 2

#menu()
pvp()
