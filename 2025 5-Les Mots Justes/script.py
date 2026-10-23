from typing import List

def nb_corrections(n: int, A: List[str], B: List[str]) -> int:
    # Count the occurrences of each syllable in A and B
    A_count = {}
    B_count = {}
    for i in range(n):
        if A[i] in A_count: A_count[A[i]] += 1
        else: A_count[A[i]] = 1
        if B[i] in B_count: B_count[B[i]] += 1
        else: B_count[B[i]] = 1

    # Get a sorted list of the occurrences of each word
    sorted_occurrences = [0] + sorted([a * b for a in A_count.values() for b in B_count.values()])
    m = len(A_count)*len(B_count)

    # Get a prefix sum list
    prefix_sum = [0]
    for i in range(1, m+1):
        prefix_sum.append(prefix_sum[i-1] + sorted_occurrences[i])

    # Determine the minimal corrections required for each number
    # The point in the array that minimizes the correction of each point is always in the list 
    min_corrections = float("inf")
    for i in range(1, m+1):
        # Do not run if it has already been computed
        if sorted_occurrences[i] == sorted_occurrences[i-1]:
            continue

        # Dichotomy approach
        left = 1
        right = i
        target = sorted_occurrences[i]/2
        result = -1
        while left <= right:
            j = (left + right)//2
            if sorted_occurrences[j] <= target:
                result = j
                left = j + 1
            else:
                right = j - 1
        if sorted_occurrences[j] > target:
            j-=1

        # Closer to 0
        nb_corr = prefix_sum[j]
        # On the left of sorted_occurrences[i]
        nb_corr += (i-j-1)*sorted_occurrences[i] - prefix_sum[i-1] + prefix_sum[j]
        # On the right of sorted_occurrences[i]
        nb_corr += prefix_sum[m] - prefix_sum[i] - (m-i)*sorted_occurrences[i]
        if nb_corr < min_corrections:
            min_corrections = nb_corr

    return min_corrections

if __name__ == '__main__':
    n = int(input())
    A = [input() for _ in range(n)]
    B = [input() for _ in range(n)]

    print(nb_corrections(n, A, B))