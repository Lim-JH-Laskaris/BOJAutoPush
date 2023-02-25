from collections import deque


def differs_by_only_one(a,b):
    """a와 b가 알파벳 하나만 다르고 나머지는 같은지를 반환. 
    두 철자 이상 다르거나 모두 같으면 False 반환"""
    different_letter_num = sum([ aa!=bb for aa,bb in zip(a,b)])
    return True if different_letter_num==1 else False

def solution(begin, target, words):
    """ BFS를 사용하여 변환된 횟수를 딕셔너리에 기록하며 진행."""
    queue = deque([begin]) 
    answer = 0
    words_dict = {w:0 for w in words} # begin에서 변환된 횟수 체크 위한 딕셔너리
    words_dict[begin] = 0 
    while queue:
        pop = queue.popleft()
        if pop == target : return words_dict[target]
        for w in [w for w in words if differs_by_only_one(pop,w)]:
            words_dict[w] = words_dict[pop]+1
            words.remove(w)
            queue.append(w)
    return 0