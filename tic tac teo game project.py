i=1
print("Hellow and welcome to tic tac toe game:")
n=int(input("Press 2 for single player 1 for multiplayer and 3 for exit:\n"))
while n!=3:
    if n==2:
        print("it's single player mood:")
        name = input("enter your name:\n")
        while True:
            symbol = (input('choose a  Symbol from x or o: '))
            if (symbol == 'o' or symbol == 'O') or (symbol == 'x' or symbol == 'X'):
                break
            else:
                continue
        player = ''
        computer = ''
        if symbol == 'x' or symbol =='X':
            player = 'x'
            computer = 'o'
        elif symbol == 'o' or symbol =='O':
            player = 'o'
            computer = 'x'
        while True:
            import random
            list = ['head', 'tail']
            toss = random.choice(list)
            guess = input("choose head or tail:\n")
            if guess=='head' or guess=='tail':
                break
            else:
                continue


        def printBoard(board):
            print(board[1] + '|' + board[2] + '|' + board[3])
            print('-+-+-')
            print(board[4] + '|' + board[5] + '|' + board[6])
            print('-+-+-')
            print(board[7] + '|' + board[8] + '|' + board[9])
            print("\n")


        def spaceIsFree(position):
            if board[position] == ' ':
                return True
            else:
                return False


        def insertLetter(letter, position):
            if spaceIsFree(position):
                board[position] = letter
                printBoard(board)
                if (checkDraw()):
                    print("the game has drawn")
                    restart()
                if checkForWin():
                    if letter != player:
                        print("computer have won the game")
                        restart()

                    else:
                        print("you have won the game")
                        restart()

                return


            else:
                print("you can't take this slot try another")
                position = int(input("Please enter new position:  "))
                insertLetter(letter, position)
                return


        def checkForWin():
            if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
                return True
            elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
                return True
            elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
                return True
            elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
                return True
            elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
                return True
            elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
                return True
            elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
                return True
            elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
                return True
            else:
                return False


        def checkWhichMarkWon(mark):
            if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
                return True
            elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
                return True
            elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
                return True
            elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
                return True
            elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
                return True
            elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
                return True
            elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
                return True
            elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
                return True
            else:
                return False


        def checkDraw():
            for key in board.keys():
                if (board[key] == ' '):
                    return False
            return True


        def restart():
            global board
            global name
            global player, computer
            ask = input("Do you want to play again press y for yes or any key for exit")
            if ask == 'y' or ask=='Y':
                board = {1: ' ', 2: ' ', 3: ' ',
                         4: ' ', 5: ' ', 6: ' ',
                         7: ' ', 8: ' ', 9: ' '}
                # checkForWin()
                print("hellow and welcome to tic tac teo game ")
                name = input("enter your name:\n")
                while True:
                    symbol = (input('choose a  Symbol from x OR o: '))
                    if (symbol == 'o' or symbol == 'O') or (symbol == 'x' or symbol == 'X'):
                        break
                    else:
                        continue
                player = ''
                computer = ''
                if symbol == 'x' or symbol=='X':
                    player = 'x'
                    computer = 'o'
                elif symbol == 'o' or symbol=='O':
                    player = 'o'
                    computer = 'x'
                while True:

                    list = ['head', 'tail']
                    toss = random.choice(list)
                    print(toss)
                    guess = input("choose head or tail:\n")
                    if guess=='head' or guess=='tail':
                        break
                    else:
                        continue

                while not checkForWin():
                    if toss == 'head':
                        print('You have won the toss!')
                        playerMove()
                        compMove()
                    elif toss == 'tail':
                        print("Computer have won the toss")
                        compMove()
                        playerMove()

            else:
                exit()


        def playerMove():
                position = int(input("Take a number from 0 to 9 :  "))
                insertLetter(player, position)
                return






        def compMove():
            bestScore = -800
            bestMove = 0
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = computer
                    score = minimax(board, False)
                    board[key] = ' '
                    if (score > bestScore):
                        bestScore = score
                        bestMove = key

            insertLetter(computer, bestMove)
            return


        def minimax(board, isMaximizing):
            if (checkWhichMarkWon(computer)):
                return 1
            elif (checkWhichMarkWon(player)):
                return -1
            elif (checkDraw()):
                return 0

            if (isMaximizing):
                bestScore = -800
                for key in board.keys():
                    if (board[key] == ' '):
                        board[key] = computer
                        score = minimax(board, False)
                        board[key] = ' '
                        if (score > bestScore):
                            bestScore = score
                return bestScore

            else:
                bestScore = 800
                for key in board.keys():
                    if (board[key] == ' '):
                        board[key] = player
                        score = minimax(board, True)
                        board[key] = ' '
                        if (score < bestScore):
                            bestScore = score
                return bestScore


        board = {1: ' ', 2: ' ', 3: ' ',
                 4: ' ', 5: ' ', 6: ' ',
                 7: ' ', 8: ' ', 9: ' '}

        if toss == 'head':
            print('You have won the toss!')
        else:
            print("computer have won the toss")
        printBoard(board)
        print(" Grid positions are as follow:")
        print("1, 2, 3 ")
        print("4, 5, 6 ")
        print("7, 8, 9 ")
        print("\n")

        # print(" from head or tail you choose    " + str(guess) + "      ")
        while not checkForWin():
            if toss == 'head':
                playerMove()
                compMove()
            elif toss == 'tail':
                compMove()
                playerMove()

    elif n==1:
        print("it's multiplayer mood")
        player_1 = input("player_1 enter your name:\n")
        while True:
            print("you must have to choose a symbol 'o' either 'x'")
            symbol_1 = input("enter a symbol:\n")

            if symbol_1=='o' or symbol_1=='x':
                break
            else:
                continue
        player_2=input("player_2 enter a name:\n")
        while True:
            print("you must have to choose a symbol 'o' either 'x'")
            symbol_2 = input("enter a symbol:\n")
            if symbol_2 == 'o' or symbol_2 == 'x':
                if symbol_2 == symbol_1:
                    print("this number is already taken")
                    print(player_2, "choose a different number")
                    continue
                else:
                    break
        print(player_1, "is going to perform the toss")

        while True:

            print(player_2,"you must have to select head or tail")
            toss = input()
            if toss == 'head':

                print(player_1, "you have won the toss")
                current_player = player_1
                grid = ["-", "-", "-",
                        "-", "-", "-",
                        "-", "-", "-"]
                game_is_running = True
                winner = None


                def start_game():
                    display_grid()
                    while game_is_running:
                        control_turn(current_player)
                        check_if_game_over()
                        change_player()

                    if winner == symbol_1:
                        print(player_1, "you are the winner")
                    elif winner == symbol_2:
                        print(player_2, "you are the winner")
                    elif winner == None:
                        print("the game is tie")


                def display_grid():
                    print(grid[0], " | ", grid[1], " | ", grid[2] + "     1 | 2 | 3 ")
                    print(grid[3], " | ", grid[4], " | ", grid[5] + "     4 | 5 | 6 ")
                    print(grid[6], " | ", grid[7], " | ", grid[8] + "     7 | 8 | 9 ")


                def control_turn(player):
                    print(player + "'s turn.")
                    position = input("Take a position from 1-9: ")
                    valid = False
                    while not valid:
                        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "01", "02", "03", "04",
                                               "05", "06", "07", "08", "09"]:
                            position = input("Take a position from 1-9: ")
                        position = int(position) - 1
                        if grid[position] == "-":
                            valid = True
                        else:
                            print("You can't take this slot try another:")
                    if current_player == player_1:
                        grid[position] = symbol_1
                    elif current_player == player_2:
                        grid[position] = symbol_2
                    display_grid()


                def check_if_game_over():
                    check_for_winner()
                    check_for_tie()


                def check_for_winner():
                    global winner
                    row_winner = check_rows()
                    column_winner = check_columns()
                    diagonal_winner = check_diagonals()
                    if row_winner:
                        winner = row_winner
                    elif column_winner:
                        winner = column_winner
                    elif diagonal_winner:
                        winner = diagonal_winner
                    else:
                        winner = None


                def check_rows():
                    global game_is_running
                    row_1 = grid[0] == grid[1] == grid[2] != "-"
                    row_2 = grid[3] == grid[4] == grid[5] != "-"
                    row_3 = grid[6] == grid[7] == grid[8] != "-"
                    if row_1 or row_2 or row_3:
                        game_is_running = False
                    if row_1:
                        return grid[0]
                    elif row_2:
                        return grid[3]
                    elif row_3:
                        return grid[6]
                    else:
                        return None


                def check_columns():
                    global game_is_running
                    column_1 = grid[0] == grid[3] == grid[6] != "-"
                    column_2 = grid[1] == grid[4] == grid[7] != "-"
                    column_3 = grid[2] == grid[5] == grid[8] != "-"
                    if column_1 or column_2 or column_3:
                        game_is_running = False
                    if column_1:
                        return grid[0]
                    elif column_2:
                        return grid[1]
                    elif column_3:
                        return grid[2]
                    else:
                        return None


                def check_diagonals():
                    global game_is_running
                    diagonals_1 = grid[0] == grid[4] == grid[8] != "-"
                    diagonals_2 = grid[6] == grid[4] == grid[2] != "-"
                    if diagonals_1 or diagonals_2:
                        game_is_running = False
                    if diagonals_1:
                        return grid[0]
                    elif diagonals_2:
                        return grid[6]
                    else:
                        return None


                def check_for_tie():
                    global game_is_running
                    if "-" not in grid:
                        game_is_running = False
                        return True
                    else:
                        return False


                def change_player():
                    global current_player
                    if current_player == player_1:
                        current_player = player_2
                    elif current_player == player_2:
                        current_player = player_1


                start_game()
                break

            elif toss=='tail':
                print(player_2, "you have won the toss")
                current_player = player_2
                grid = ["-", "-", "-",
                        "-", "-", "-",
                        "-", "-", "-"]
                game_is_running = True
                winner = None


                def start_game():
                    display_grid()
                    while game_is_running:
                        control_turn(current_player)
                        check_if_game_over()
                        change_player()
                    if winner == symbol_1:
                        print(player_1, "you are the winner")
                    elif winner == symbol_2:
                        print(player_2, "you are the winner")
                    elif winner == None:
                        print("Tie")


                def display_grid():
                    print("\n")
                    print(grid[0] + " | " + grid[1] + " | " + grid[2]+ "     1 | 2 | 3 ")
                    print(grid[3] + " | " + grid[4] + " | " + grid[5]+ "     4 | 5 | 6 ")
                    print(grid[6] + " | " + grid[7] + " | " + grid[8]+ "     7 | 8 | 9 ")
                    print("\n")


                def control_turn(player):
                    print(player + "'s turn.")
                    position = input("Take a position from 1-9: ")
                    valid = False
                    while not valid:
                        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            position = input("Take a position from 1-9: ")
                        position = eval(position) - 1
                        if grid[position] == "-":
                            valid = True
                        else:
                            print("You can't take this slot. try another:")

                    if current_player == player_1:
                        grid[position] = symbol_1
                    elif current_player == player_2:
                        grid[position] = symbol_2
                    display_grid()


                def check_if_game_over():
                    check_for_winner()
                    check_for_tie()


                def check_for_winner():
                    global winner
                    row_winner = check_rows()
                    column_winner = check_columns()
                    diagonal_winner = check_diagonals()
                    if row_winner:
                        winner = row_winner
                    elif column_winner:
                        winner = column_winner
                    elif diagonal_winner:
                        winner = diagonal_winner
                    else:
                        winner = None


                def check_rows():
                    global game_is_running
                    row_1 = grid[0] == grid[1] == grid[2] != "-"
                    row_2 = grid[3] == grid[4] == grid[5] != "-"
                    row_3 = grid[6] == grid[7] == grid[8] != "-"
                    if row_1 or row_2 or row_3:
                        game_is_running = False
                    if row_1:
                        return grid[0]
                    elif row_2:
                        return grid[3]
                    elif row_3:
                        return grid[6]
                    else:
                        return None


                def check_columns():
                    global game_is_running
                    column_1 = grid[0] == grid[3] == grid[6] != "-"
                    column_2 = grid[1] == grid[4] == grid[7] != "-"
                    column_3 = grid[2] == grid[5] == grid[8] != "-"
                    if column_1 or column_2 or column_3:
                        game_is_running = False
                    if column_1:
                        return grid[0]
                    elif column_2:
                        return grid[1]
                    elif column_3:
                        return grid[2]
                    else:
                        return None


                def check_diagonals():
                    global game_is_running
                    diagonals_1 = grid[0] == grid[4] == grid[8] != "-"
                    diagonals_2 = grid[6] == grid[4] == grid[2] != "-"
                    if diagonals_1 or diagonals_2:
                        game_is_running = False
                    if diagonals_1:
                        return grid[0]
                    elif diagonals_2:
                        return grid[6]
                    else:
                        return None


                def check_for_tie():
                    global game_is_running
                    if "-" not in grid:
                        game_is_running = False
                        return True
                    else:
                        return False


                def change_player():
                    global current_player
                    if current_player == player_1:
                        current_player = player_2
                    elif current_player == player_2:
                        current_player = player_1


                start_game()
                break
            else:
                print("enter correct option")
                continue
    else:
        print("enter valid number")

    choose=input((" Do you want to play again then press y/Y: else press any key to exit"))
    if choose == 'y' or choose == 'Y':
        print("Hellow and welcome to tic tac toe game:")
        n = int(input("Press 2 for single player 1 for multiplayer and 3 for exit:\n"))
    else:
        break

    i=i+1


