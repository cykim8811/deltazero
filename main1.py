
import time
import utils

a, b, c = 2, 3, 0

def adder_worker():
    global a, b, c
    c = a + b

def root_worker():
    adder_worker()

    utils.clear_shell()

    print('a:', a)
    print('b:', b)
    print('c:', c)

while True:
    root_worker()
    time.sleep(0.001)

