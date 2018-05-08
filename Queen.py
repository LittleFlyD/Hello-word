import random

def confict(pos, state):
    nextY = len(state) # Next Line
    if pos in state: return True
    for i in range(nextY):
        if pos - state[i] == abs(nextY-i): return True
    return False

def Queen(num, state=()):
    if num-1 == len(state):
        for i in range(num):
            if not confict(i, state):
                yield(i,)
    else:
        for pos in range(num):
            if not confict(pos, state):
                for result in Queen(num, state+(pos,)):
                    yield(pos, ) + result
        
def RandomPrintQueen(queen):
    print(random.choice(list(queen)))
