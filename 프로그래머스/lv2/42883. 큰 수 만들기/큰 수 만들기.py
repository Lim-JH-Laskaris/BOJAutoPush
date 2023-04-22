def argmax(str_):
    """최대값의 인덱스를 반환하는 함수. 
    단, '0'부터'9'까지만 확인하므로, 
    '9'를 찾으면 즉시 해당 인덱스를 반환"""
    max_num = '0'
    max_idx = 0 
    for i,x in enumerate(str_):
        if x == '9' :return i
        if max_num != max(max_num,x):
            max_idx, max_num = i, x
    return max_idx

def solution(number, k):
    """k번 제거할 수 있으므로, 먼저 앞의 k+1개 문자들 중, 
    최대값의 앞에 있는 모든 문자를 제거한 뒤, 해당 최대값은 answer문자열에 추가.
    그후 제거한 문자열 수를 차감하여 k를 갱신한다. 이때 k>0이면,
    최대값 이후의 number문자열에 대해 갱신된 k에 따라 앞의 과정을 반복한다.
    단, 남은문자열의 길이가 k일 때, 최대값과 관계 없이 모두 지워야한다. 
    """
    answer = ''
    while k:
        if k == len(number): 
            return answer
        am = argmax(number[:k+1])
        answer += number[am]
        number = number[am+1:]
        k -= am
    return answer+number
