from typing import List
from bisect import bisect_left

def min_sum_non_adjacent(N, K, arr):
    # Sort by increasing cost, while keeping their starting indexes
    priority_queue = sorted([[arr[i], i] for i in range(N)], key=lambda x: x[0])
    # Keep the remaining unused indexes
    linked_list = [i for i in range(N)]
    final_sum = 0 
    for _ in range(K):
        # let i be the iteration counter 
        # final_sum contains the minimal sum of exactly i non-adjacent elements of arr

        queue_length = len(priority_queue)

        # Remove the least cost element e from the queue
        e_cost, e_idx = priority_queue.pop(0)
        
        final_sum += e_cost

        e_idx_in_linked_list = bisect_left(linked_list, e_idx)

        left_neighbor = e_idx_in_linked_list > 0
        right_neighbor = e_idx_in_linked_list < queue_length - 1

        if left_neighbor:
            # Search for the position of the left neighbor in the priority_queue using binary search
            left_neighbor_idx = linked_list.pop(e_idx_in_linked_list-1)
            left_neighbor_cost = arr[left_neighbor_idx]
            left_neighbor_idx_in_queue = bisect_left(priority_queue, [left_neighbor_cost, left_neighbor_idx] , )
            priority_queue.pop(left_neighbor_idx_in_queue)
        else:
            linked_list.pop(0)
        
        if right_neighbor:
            # Search for the position of the right neighbor in the priority_queue using binary search
            right_neighbor_idx = linked_list.pop(e_idx_in_linked_list)
            right_neighbor_cost = arr[right_neighbor_idx]
            right_neighbor_idx_in_queue = bisect_left(priority_queue, [right_neighbor_cost, right_neighbor_idx])
            priority_queue.pop(right_neighbor_idx_in_queue)
        elif left_neighbor:
            linked_list.pop()

        if left_neighbor and right_neighbor:
            # Modify the cost of e
            new_cost = right_neighbor_cost + left_neighbor_cost - e_cost
            arr[e_idx] = new_cost
            new_e = [new_cost, e_idx]
            # Keep priority_queue sorted while inserting new element
            priority_queue.insert(bisect_left(priority_queue, new_e), new_e)

    return final_sum

def min_dizziness_old(N: int, K: int, bars: List[int]) -> int:
    sorted_bars = sorted(bars)
    height_diff = [sorted_bars[i]-sorted_bars[i-1] for i in range(1, N)]
    min_sum = min_sum_non_adjacent(N-1, K, height_diff)
    return min_sum

if __name__ == '__main__':
    N = int(input())
    K = int(input())
    bars = list(map(int,input().split()))
    print(min_dizziness_old(N, K, bars))
