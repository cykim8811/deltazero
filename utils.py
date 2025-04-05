

RESET = "\033[0m"

WHITE_FG = "\033[38;2;255;255;255m"
WHITE_BG = "\033[48;2;255;255;255m"
GRAY_FG = "\033[38;2;64;64;72m"
DG_FG = "\033[38;2;32;32;48m"
BLACK_FG = "\033[38;2;0;0;0m"
BLACK_BG = "\033[48;2;64;64;72m"

BROWN_BG = "\033[48;2;139;69;19m"
BROWN_FG = "\033[38;2;139;69;19m"
DARKBROWN_BG = "\033[48;2;101;67;33m"

PAWN_STROKE = "\u2659"
PAWN_FILL = "\u265F"

LEFT_HALF_BLOCK = "\u258C"
RIGHT_HALF_BLOCK = "\u2590"
BOTTOM_QUARTER_BLOCK = "\u2582"
TOP_HALF_BLOCK = "\u2580"
CLEAR_SCREEN = "\033[2J"

def print_board(board):
    print(CLEAR_SCREEN)
    print('   a b c d e f g h')
    print('  ' + BROWN_FG + BOTTOM_QUARTER_BLOCK * 17 + RESET)
    for col in range(8):
        print(8 - col, end=" ")
        if col % 2 == 0:
            print(WHITE_BG + BROWN_FG + LEFT_HALF_BLOCK, end="")
        else:
            print(BLACK_BG + BROWN_FG + LEFT_HALF_BLOCK, end="")
        for row in range(8):
            if (row + col) % 2 == 0:
                piece = " "
                if board[row][col] == 'white':
                    piece = BLACK_FG + PAWN_STROKE
                elif board[row][col] == 'black':
                    piece = BLACK_FG + PAWN_FILL
                print(WHITE_BG + piece, end="")
                if row != 7:
                    print(WHITE_BG + GRAY_FG + RIGHT_HALF_BLOCK, end="")
            else:
                piece = " "
                if board[row][col] == 'white':
                    piece = WHITE_FG + PAWN_STROKE
                elif board[row][col] == 'black':
                    piece = DG_FG + PAWN_FILL
                print(BLACK_BG + piece, end="")
                if row != 7:
                    print(BLACK_BG + WHITE_FG + RIGHT_HALF_BLOCK, end="")
        if col % 2 == 0:
            print(BLACK_BG + BROWN_FG + RIGHT_HALF_BLOCK, end="")
        else:
            print(WHITE_BG + BROWN_FG + RIGHT_HALF_BLOCK, end="")
        print(RESET)
    print('  ' + BROWN_FG + TOP_HALF_BLOCK * 17 + RESET)

