def solution(k, score):
    honor_list = []
    result = []
    for i in score:
        honor_list = sorted(honor_list+[i],reverse=True)[:k]
        result.append(honor_list[-1])
    return result