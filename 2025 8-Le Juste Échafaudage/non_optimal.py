from typing import List

cache = {}

def min_sum_non_adjacent(N, offset, K, arr):
    cache = {}
    if K == 0:
        return 0
    if (N-offset)/2+1 <= K:
        return float("inf")
    if (offset, K) in cache:
        return cache[(offset, K)]
    sum1 = arr[offset] + min_sum_non_adjacent(N, offset + 2, K -1, arr)
    sum2 = min_sum_non_adjacent(N, offset + 1, K, arr)
    result = min(sum1, sum2)
    cache[(offset, K)] = result
    return result

def min_dizziness_suboptimal(N: int, K: int, bars: List[int]) -> int:
    sorted_bars = sorted(bars)
    height_diff = [sorted_bars[i]-sorted_bars[i-1] for i in range(1, N)]

    min_sum = min_sum_non_adjacent(N-1, 0, K, height_diff)
    return min_sum

if __name__ == '__main__':
    N = int(input())
    K = int(input())
    bars = list(map(int,input().split()))
    print(min_dizziness_suboptimal(N, K, bars))