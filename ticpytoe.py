import os, time
import random as rd

def clear_board():
    board = {
        7: '-', 8: '-', 9: '-',
        4: '-', 5: '-', 6: '-',
        1: '-', 2: '-', 3: '-'
    }
    return board

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
        {board[7]} {board[8]} {board[9]}
        {board[4]} {board[5]} {board[6]}
        {board[1]} {board[2]} {board[3]}
    """)

def player_turn():
    ok = False
    while not ok:
        Xstr = input(":")
        if Xstr.isdigit():
            X = int(Xstr)
            if int(X) >= 1 and int(X) <= 9:
                ok = True
                return X
            else:
                print(f"{Xstr} não é uma casa válida")
                continue
        else:
            # there's a bug with non Digit inputs, fix to-do
            # doesn't even look at the "ok" while, i know it's ugly, has to fix that
            print(f"{Xstr} não é um número")
            continue
            
def computer_turn():
    # time.sleep(0.1)
    O = rd.randint(1, 9)
    return O

def check_win(board, choice):
    # To-do:
    # clear this bs
    if (choice == board[1] == board[2] == board[3]) or (choice == board[4] == board[5] == board[6]) or (choice == board[7] == board[8] == board[9]):
        if choice == 'X':
            winner = "PLAYER"
        elif choice == 'O':
            winner = "COMPUTER"
        return winner
    if (choice == board[7] == board[4] == board[1]) or (choice == board[8] == board[5] == board[2]) or (choice == board[9] == board[6] == board[3]):
        if choice == 'X':
            winner = "PLAYER"
        elif choice == 'O':
            winner = "COMPUTER"
        return winner
    if (choice == board[1] == board[5] == board[9]) or (choice == board[7] == board[5] == board[3]):
        if choice == 'X':
            winner = "PLAYER"
        elif choice == 'O':
            winner = "COMPUTER"
        return winner
    return None

def game():
    over = False
    winner = None
    board = clear_board()
    print_board(board)

    # Randomly choose the first player
    if rd.randint(0, 1) == 0:
        print("O jogador começa!\n")
        turn = 'PLAY'
    else:
        print("O computador começa!\n")
        turn = 'COMP'

    while not over:
        # Check for a valid winner
        winner = check_win(board, 'X')
        if winner != None:
            turn = None
            return winner
        winner = check_win(board, 'O')
        if winner != None:
            turn = None
            return winner
        
        # Check for a tie game
        all_taken = all(taken != '-' for taken in board.values())
        if all_taken and (winner == None):
            turn = None
            winner = "VELHA"
            return winner
                
        
        # Player turn
        while turn == 'PLAY':
            play = player_turn()
            if board[play] == '-':
                board[play] = 'X'
                turn = 'COMP'
        print_board(board)

        # Computer turn
        while turn == 'COMP':
            comp = computer_turn()
            if board[comp] == '-':
                board[comp] = 'O'
                turn = 'PLAY'
        print_board(board)
     

winner = game()
print("GAME OVER")
print(f"O vencedor foi {winner}\n")

# To-do:
# Play again routine