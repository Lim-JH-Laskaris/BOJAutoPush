def solution(k, score):
    q = []
    answer = []
    for s in score:
        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))
    return answer


# def solution(k, score):
#     honor_list = []
#     result = []
#     for i in score:
#         # honor_list = insert(honor_list, i)[:k] 
#         honor_list = sorted(honor_list+[i],reverse=True)[:k]
#         result.append(honor_list[-1])
#     return result

#매번 sort하는 것은 k에대해 선형로그만큼 커지므로 그때그때 삽입하는 방식으로 코드를 짰으나, 오히려 시간이 더 걸리게 되었다. 
# def insert(list_, n):
#     idx = 0
#     for i in range(len(list_)):
#         if list_[i]>n:
#             idx += 1
#         else :
#             break
#     list_.insert(idx,n)
#     return list_

