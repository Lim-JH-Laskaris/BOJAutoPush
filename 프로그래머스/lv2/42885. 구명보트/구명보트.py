from collections import deque
def solution(people, limit):
    people = deque(sorted(people))
    answer = 0
    while people:
        a = people.pop()
        if people and people[0] <= limit-a:
            people.popleft()
        answer += 1
    return answer

# 최초 코드, 효율성 문제
# def solution(people, limit):
#     """탐욕법: 가장 무거운 사람부터 태우고, 동승 가능 인원중 가장 무거운 이부터 동승시킨다."""
#     people.sort()
#     answer = 0
#     while people:
#         a = people.pop()
#         b_can = [p for p in people if p<=limit-a] #효율성 저하 원인 후보
#         if b_can : 
#             people.pop(people.index(b_can[-1])) #효율성 저하 원인 후보
#         answer += 1
#     return answer

# Counter를 통해 개선했으나 여전히 효율성 문제.
# from collections import Counter
# def solution(people, limit):
#     people = Counter(people)
#     answer = 0
#     while people:
#         a = max(people.keys())
#         if people[a] == 1 : people.pop(a)
#         else : people[a] -= 1
#         b_can = [p for p in people.keys() if p<=limit-a]
#         if b_can : 
#             b = max(b_can)
#             if people[b] == 1 : people.pop(b)
#             else : people[b] -= 1
#         answer += 1
#     return answer
"""인원수는 2명으로 제한되어 있을때는 굳이 동승자 b의 무게가
최대가 되게 할 필요가 없음을 알고 이를 고쳐서 해결"""