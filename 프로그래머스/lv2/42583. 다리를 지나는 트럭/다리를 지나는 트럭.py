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

# 맨처음에 " 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 " 라는 부분을 놓쳐서, 정렬하고이분탐색하고..... 불필요한 일을 하느라 시간을 잡아먹었다. 

