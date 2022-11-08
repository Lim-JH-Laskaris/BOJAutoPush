def int_doscount(want, discount):
    # want의 원소를 기준으로 discount의 원소를 정수화, 없는 변수는 모두 11로
    want_dict = {want[i]:i for i in range(len(want))}
    return [want_dict[j] if j in want else 11 for j in discount]

def number_to_len11(number):
    # number를 길이가 11인 리스트로 변환 (나머지는 모두 0)
    return number+[0]*(12-len(number))

def count_by_group(list_):
    # discount의 일부분(10연속)을 가져와 number와 같은형식으로 변환
    count_list = [0]*12
    for i in list_:
        count_list[i] += 1
    return count_list

def solution(want, number, discount):
    answer = 0
    # want의 원소를 기준으로 discount의 원소를 정수화, 없는 변수는 모두 11로
    discount = int_doscount(want, discount)
    # number를 길이가 11인 리스트로 변환 (나머지는 모두 0)
    number = number_to_len11(number)
    # discount의 일부분(10연속)을 가져와 number와 같은형식으로 변환하고 서로 동일한지 확인하고 카운트
    c = 0
    for i in range(len(discount)-9):
        if number == count_by_group(discount[i:i+10]): c+=1
    return c