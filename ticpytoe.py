board = {
    7: ' ', 8: ' ', 9: ' ',
    4: ' ', 5: ' ', 6: ' ',
    1: ' ', 2: ' ', 3: ' '
}

def game_screen():
    board[7], board[5], board[3] = 'X'
    print(f"""
        {board[7]} {board[6]} {board[5]}
        {board[4]} {board[5]} {board[6]}
        {board[1]} {board[2]} {board[3]}
    """)

game_screen()