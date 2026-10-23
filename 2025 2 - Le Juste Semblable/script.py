from doctest import testmod
from typing import List

def nb_submarines_left(n: int, m:int, criteres:List[str]) -> int:
    submarines_left = n
    dict = {}
    for crit in criteres:
        if crit in dict:
            if dict[crit]:
                submarines_left -= 2
                dict[crit] = False
            else:
                dict[crit] = True
        else:
            dict[crit] = True
    return submarines_left

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    criteres = [''.join(input().split()) for _ in range(n)]
    print(nb_submarines_left(n, m, criteres))

testmod()
