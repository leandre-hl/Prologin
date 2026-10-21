from collections import deque
from sys import setrecursionlimit

setrecursionlimit(1000*1000*42)

N = int(input())
M = int(input())
beaute = [0] + list(map(int, input().split()))
etage = [0] + list(map(int, input().split()))

def get_enfants(N, etage):
    enfants = {}
    for i in range(1, N+1):
        enfants[i] = []
    for i in range(2, N+1):
        enfants[etage[i]].append(i)
    return enfants

enfants = get_enfants(N, etage)
cumsum = [0] * (N+42)
max_score = [0] * (N+42)

def min_sabotage():
    # Dichotomie
    lft = 0
    rht = N
    while lft < rht:
        k = (lft + rht) // 2
        if DFS(k, 1, 1):
            rht = k
        else:
            lft = k + 1
    return (lft + rht) // 2

def DFS(k, i, depth):
    # Commencer a depth = 1 et i = 1
    cumsum[depth] = beaute[i] + cumsum[depth-1]
    score = cumsum[depth] - cumsum[max(0, depth-k)]
    max_score[depth] = max(max_score[depth-1], score)
    if enfants[i] == []:
        return max_score[depth] >= cumsum[depth] - M
    valid = True
    for e in enfants[i]:
        valid &= DFS(k, e, depth+1)
    return valid

def min_kit():
    print(min_sabotage())

min_kit()