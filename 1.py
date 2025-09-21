import sys
import math


def calculate_distance_squared(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def determine_action(t1, x1, y1, t2, x2, y2):
    time_diff = t2 - t1
    distance_sq = calculate_distance_squared(x1, y1, x2, y2)
    if time_diff < 100:
        return 1
    else:
        if distance_sq <= 2500:
            if 100 <= time_diff <= 1000:
                return 2
            else:
                return 3
        else:
            return 4


input = sys.stdin.read().split()
idx = 0
C = int(input[idx])
idx += 1
results = []
for _ in range(C):
    t1 = int(input[idx])
    x1 = int(input[idx + 1])
    y1 = int(input[idx + 2])
    idx += 3
    t2 = int(input[idx])
    x2 = int(input[idx + 1])
    y2 = int(input[idx + 2])
    idx += 3
    action = determine_action(t1, x1, y1, t2, x2, y2)
    results.append(str(action))
print('\n'.join(results))
