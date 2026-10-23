#from doctest import testmod
#from time import time
from typing import List

cache = {}




def max_strength(N: int, bridge: List[int]) -> int:
    ...

if __name__ == '__main__':
    N = int(input())
    bridge = list(map(int,input().split()))
    print(max_strength(N, bridge))

#testmod()