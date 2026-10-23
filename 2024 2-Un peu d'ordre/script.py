from doctest import testmod
from typing import List



if __name__ == '__main__':
    k = int(input())
    n = int(input())
    sizes = list(map(int, input().split(' ')))

testmod()