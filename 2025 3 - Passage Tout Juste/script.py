from doctest import testmod
from time import time
from typing import List

def max_strength(n: int, tunnel:str) -> int:
    E = 0
    R = n
    curr_E = 0
    curr_R = 0
    for position in tunnel:
        if position == '0':
            curr_R += 1
            curr_E = 0
        elif position == '1':
            if curr_R > 0 and curr_R < R:
                R = curr_R
            curr_E += 1
            if curr_E > E:
                E = curr_E
            curr_R = 0
    if curr_R > 0 and curr_R < R:
        R = curr_R

    return R-E

if __name__ == '__main__':
    start_time = time()

    n = int(input())
    tunnel = ''.join(input().split())
    print(max_strength(n, tunnel))

testmod()