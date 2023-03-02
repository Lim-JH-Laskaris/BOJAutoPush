def solution(k, score):
    honor_list = []
    result = []
    for i in score:
        honor_list = sorted(honor_list+[i],reverse=True)[:k]
        result.append(honor_list[-1])
    return result

#매번 sort하는 것은 k에대해 선형로그만큼 커지므로 그때그때 삽입하는 방식으로 코드를 짰으나, 오히려 시간이 더 걸리게 되었다. 
#파이썬 sorted 함수가 최적화가 잘되어있는것 같다.
