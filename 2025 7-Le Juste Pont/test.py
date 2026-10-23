def max_strength(N, bridge):
    # Identify segments of 0s and 1s
    segments = []
    count = 1
    for i in range(1, N):
        if bridge[i] == bridge[i-1]:
            count += 1
        else:
            segments.append((bridge[i-1], count))
            count = 1
    segments.append((bridge[-1], count))  # last segment
    print(segments)

    max_strength_value = float('-inf')

    # Check all combinations of R and E
    for E in range(1, N + 1):  # Possible endurance values
        for R in range(1, N+1):  # Possible rest values (must be less than E)
            current_position = 0
            can_cross = True
            while current_position < N:
                if bridge[current_position] == 1:
                    # Swim through this segment
                    segment_length = 0
                    while current_position < N and bridge[current_position] == 1:
                        segment_length += 1
                        current_position += 1
                    if segment_length > E:
                        can_cross = False  # Cannot swim this segment
                        break
                    # Swim successful, need to walk afterwards
                    if current_position < N and (current_position + R) > N:
                        can_cross = False  # Can't rest anymore
                        break
                else:
                    # Can choose to walk or swim
                    segment_length = 0
                    while current_position < N and bridge[current_position] == 0:
                        segment_length += 1
                        current_position += 1
                    if current_position < N and bridge[current_position] == 1:
                        # Swimming required again, check limits
                        if segment_length < R:
                            can_cross = False  # Cannot walk enough to rest
                            break
                    else:
                        # Successfully crossed
                        break

            if can_cross:
                max_strength_value = max(max_strength_value, R - E)

    return max_strength_value

if __name__ == '__main__':
    N = int(input())
    bridge = list(map(int,input().split()))
    print(max_strength(N, bridge))