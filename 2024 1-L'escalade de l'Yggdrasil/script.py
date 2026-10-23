from doctest import testmod
from typing import List

def max_jump(n:int, height_diff:List[int])->int:
    """
    >>> max_jump(4, [3, 2, -5, 4])
    3
    """
    max_jump = 0
    max_height = 1
    curr_height = 1
    curr_max_jump = 0
    for diff in height_diff:
        curr_height += diff
        if diff > max_jump: 
            curr_max_jump = diff
        if curr_height > max_height:
            max_height = curr_height
            max_jump = curr_max_jump
    return max_jump


if __name__ == '__main__':
    n = int(input())
    height_diff = list(map(int, input().split(' ')))
    print(max_jump(n, height_diff))

testmod()