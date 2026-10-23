from typing import List
from collections import deque

def correct_path(N: int, M: int, K: int,  scores: List[int], paths: List[List[int]]) -> int:
    # Get the graph
    graph = [[] for _ in range(N)]
    for path in paths:
        graph[path[0]-1].append(path[1]-1)
        graph[path[1]-1].append(path[0]-1)

    # Compute the distances to the fist house
    # using BFS algorithm
    
    distances = [float("inf")] * (N)
    distances[0] = 0
    dict_distances = {0: [1]}
    dict_visited = {0: 1}
    queue = deque([0])

    sum_scores_by_distance = [0] * (K+1)
    sum_scores_by_distance[0] = scores[0]

    while queue:
        current_node = queue.popleft()
        curr_dist = distances[current_node]
        if curr_dist >= K:
            break
        for neighbor in graph[current_node]:
            if neighbor not in dict_visited:
                distances[neighbor] = curr_dist + 1
                sum_scores_by_distance[curr_dist + 1] += scores[neighbor]
                queue.append(neighbor)
                dict_visited[neighbor] = 1

    cum_sum_scores = [0] * (K+1)
    cum_sum_scores[0] = sum_scores_by_distance[0]
    for i in range(1, K+1):
        cum_sum_scores[i] = cum_sum_scores[i-1] + sum_scores_by_distance[i]

    # Compute the final score
    final_score = 0
    for i in range(K+1):
        final_score = (final_score + sum_scores_by_distance[i] * cum_sum_scores[K-i]) % (10**9+7)
    return final_score % (10**9+7)

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    K = int(input())

    scores = list(map(int, input().split()))
    paths = [list(map(int,input().split())) for _ in range(M)]
    print(correct_path(N, M, K, scores, paths))