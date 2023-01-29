def solution(X, Y):
    set_XY = set(X).intersection(Y)
    if not set_XY : return "-1"
    elif set_XY == {'0'} : return '0'
    else: 
        answer = ''
        for i in sorted(list(set_XY), reverse=True):
            answer = answer + i*min(X.count(i),Y.count(i))
        return answer 
 
# 아래 코드 마지막의 str(int(answer))는 '00'을 '0'으로 바꾸기 위해 사용했는데,
# 긴 문자열의 경우 형변환에 불필요하게 시간이 오래걸려서 11~15케이스에서 시간초과가 떴다.

# from collections import Counter

# def str_count(str_):
#     c = Counter(list(str_))
#     c_list = [0]*10
#     for i in c.keys():
#         c_list[int(i)] = c[i]
#     return c_list

# def count_to_zzakgung(min_count):
#     return "".join([str(i)*min_count[i] for i in range(10)][::-1])

# def solution(X, Y):
#     X_count = str_count(X)
#     Y_count = str_count(Y)
#     min_count_XY = [min(x,y) for x,y in zip(X_count,Y_count)]
#     answer = count_to_zzakgung(min_count_XY)
#     return '-1' if answer=='' else str(int(answer))