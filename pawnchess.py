
from utils import print_board
import time
import threading

board = [[None for _ in range(8)] for _ in range(8)]
for i in range(8):
    board[i][0] = 'white'
    board[i][1] = 'white'
    board[i][7] = 'black'
    board[i][6] = 'black'

input_data = None

def input_thread():
    global input_data
    while True:
        input_data = input()
    

while True:
    print_board(board)
    time.sleep(0.01)