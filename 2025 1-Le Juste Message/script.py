from doctest import testmod
from typing import List

def correct_message(n: int, message:str) -> str:
    """
    >>> correct_message(42, "go_to_215.32498887125,3_-7501.853723432117")
    'go_to_25.498825,_-71.873417'
    >>> correct_message(5, "54321")
    '5'
    >>> correct_message(5, "12345")
    '12345'
    >>> correct_message(3, "655")
    '65'
    """
    corrected = ""
    last_digit = -1
    for l in message:
        if l.isdigit():
            if last_digit <= int(l):
                corrected += l
            last_digit = int(l)
        else:
            corrected += l
    
    return corrected

if __name__ == '__main__':
    n = int(input())
    message = input()
    print(correct_message(n, message))

testmod()