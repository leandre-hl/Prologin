from doctest import testmod

from typing import List

def is_palindrome(word: str)-> bool:
    """ Return True if the string is a palindrome
    >>> is_palindrome('1234')
    False
    >>> is_palindrome('KAYAK')
    True
    """
    n = len(word)
    for i in range(n//2):
        if word[i] != word[n-1-i]:
            return False
    return True

def extract(word: str):
    """ return digits, lowercase, uppercase
    >>> extract("HellO e0H")
    ('0', 'elle', 'HOH')
    """
    digits, alpha_min, alpha_maj = "", "", ""
    for l in word:
        if l.isdigit():
            digits += l
        elif l.isalpha():
            if l.islower():
                alpha_min += l
            else:
                alpha_maj += l
    return digits, alpha_min, alpha_maj

def nb_pas_malin_drome(n:int, words:List[str]) -> None:
    pal_count = 0
    for word in words:
        digits, alpha_min, alpha_maj = extract(word)
        if is_palindrome(digits) and is_palindrome(alpha_min) and is_palindrome(alpha_maj):
            pal_count += 1
    print(pal_count)

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]
    nb_pas_malin_drome(n, words)


testmod()