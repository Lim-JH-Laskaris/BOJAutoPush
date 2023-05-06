from collections import deque

def solution(bridge_length, weight, truck_weights):
    doing = deque()
    t = 0
    now_weight = 0
    truck_weights = deque(truck_weights)
    while doing or truck_weights:
        if doing and doing[0][0] == t:
            weight += doing.popleft()[1]
        if truck_weights and weight - truck_weights[0] >=0:
            tw = truck_weights.popleft()
            weight -= tw
            doing.append((t+bridge_length, tw))
        t += 1
    return t

