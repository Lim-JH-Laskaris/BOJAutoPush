def argmax(str_):
    max_num = '0'
    max_idx = 0 
    for i,x in enumerate(str_):
        if x == '9' :return i
        if max_num != max(max_num,x):
            max_idx, max_num = i, x
    return max_idx

def solution(number, k):
    answer = ''
    while k:
        if k == len(number): 
            return answer
        am = argmax(number[:k+1])
        answer += number[am]
        number = number[am+1:]
        k -= am
    return answer+number
