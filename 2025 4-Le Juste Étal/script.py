from typing import List

def nb_right_series(n: int, value: int, boxes: List[int]) -> int:
    prefix_sum = [0] * n
    prefix_sum[0] = boxes[0] % value
    for i in range(1, n):
        prefix_sum[i] = (prefix_sum[i-1] + boxes[i]) % value  # Calculate prefix sum modulo value
    count = 0
    prefix_sum_count = {0: 1}  # Initialize count for prefix sum 0
    for i in range(0, n):
        count += prefix_sum_count.get(prefix_sum[i], 0)
        prefix_sum_count[prefix_sum[i]] = prefix_sum_count.get(prefix_sum[i], 0) + 1
    return count % (10**9+7)

if __name__ == '__main__':
    n = int(input())
    value = int(input())
    boxes = list(map(int, input().split()))
    print(nb_right_series(n, value, boxes))


# from typing import List

# def nb_right_series(n: int, value:int, boxes:List[int]) -> int:
#     prefix_sum = [0] * (n+1)
#     for i in range(n):
#         prefix_sum[i+1] = ((prefix_sum[i] + boxes[i]) % value)
#     count = 0
#     prefix_sum_count = {}
#     for i in range(n+1):
#         count += prefix_sum_count.get(prefix_sum[i], 0)
#         prefix_sum_count[prefix_sum[i]] = prefix_sum_count.get(prefix_sum[i], 0) + 1
#     return count

# if __name__ == '__main__':
#     n = int(input())
#     value = int(input())
#     boxes = list(map(int,input().split()))
#     print(nb_right_series(n, value, boxes))