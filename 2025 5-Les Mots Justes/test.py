from typing import List

def corrections_typeA(target: int, n:int, words_counts:List[int]) -> int:
    total_occurrences = sum([abs(words_counts[i] - target) for i in range(n*n)])
    return total_occurrences

def corrections_typeB(target: int, n:int, words_counts:List[int]) -> int:
    total_occurrences = sum([abs(words_counts[i] - target) for i in range(n*n)])
    i = 0
    while target > 2*word_counts[i]:
        total_occurrences += word_counts[i] - target 
        i+= 1
    return total_occurrences

target = 12
n = 3
A = [1, 3, 5]
B = [2, 3, 4]
word_counts = [a * b for a in A for b in B]
print(n)
print(target)
print(word_counts)
print(corrections_typeA(target, n, word_counts))
print(corrections_typeB(target, n, word_counts))