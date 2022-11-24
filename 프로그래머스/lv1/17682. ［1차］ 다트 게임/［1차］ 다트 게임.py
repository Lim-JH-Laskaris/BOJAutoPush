from collections import deque

def make_lists(dartResult):
    """점수|보너스|[옵션] 문자열을 받아 각각의 리스트를 반환
    
    Args:
        dartResult : "점수|보너스|[옵션]" 형식
        
    Returns:
        score_list  : 원점수를 순서대로 기록 ['0','1', ... , '9','10']
        bonus_list  : 보너스를 순서대로 기록 ['S','D','T']
        option_list : 옵션을 순서대로 기록. 없다면 '-'. ['-','*','#']
        
    Notes:
        list의 pop(0)보다 deque의 popleft()가 시간복잡도가 좋아 이를 채택.
        다만, 입력 문자열이 짧을 경우, 변환 자체의 소요시간 탓에 더 느려질수도.
    """
    
    dR_deque = deque(dartResult) 
    score_list =[]
    bonus_list =[]
    option_list=[]
    while len(dR_deque)>1: 
        if not dR_deque[1].isdigit() : # 10의 경우를 구분 위해 추가
            score_list.append(dR_deque.popleft())
        else :
            score_list.append(dR_deque.popleft()+dR_deque.popleft())
        bonus_list.append(dR_deque.popleft())
        if dR_deque and dR_deque[0] in ['*','#']: 
            option_list.append(dR_deque.popleft())
        else : 
            option_list.append('-') #옵션이 없다는 의미로 활용
    return score_list, bonus_list, option_list

def bonus_str_to_int(bonus_list):
    """S,D,T로 표기된 보너스 리스트를 받아 1,2,3으로 변환한 리스트 반환
    """
    str_int_dict = {'S':1,'D':2,'T':3}
    return list(map(lambda x:str_int_dict[x], bonus_list))

def option_str_to_int(option_list):
    """-,*,#로 표기된 보너스 리스트를 받아 1,2,-1로 변환한 리스트 반환
    """
    str_int_dict = {'-':1,'*':2,'#':-1}
    return list(map(lambda x:str_int_dict[x], option_list))

def cal_final_score(score_list,bonus_list,option_list):
    """점수 리스트와, 정수화된 보너스 리스트,정수화된 옵션리스트를 받아서
    최종 총점수를 반환하는 함수
    
    Args:
        score_list  (list[int]) : 원점수를 순서대로 기록
        bonus_list  (list[int]) : 보너스(정수)를 순서대로 기록 (제곱수)
        option_list (list[int]) : 옵션(정수)을 순서대로 기록 (곱셈값)  
        
    Returns:
        원점수에 보너스와 옵션을 적용한 후 이를 모두 합한 점수를 반환
        
    Notes:
        단, 2배 옵션(*, 스타상)의 경우 이전 차례 점수도 2배로 바꾸므로 유의
    """
    star_option_plus = [i if i==2 else 1 for i in option_list][1:]+[1]
                        #스타상의 이전 점수 2배 효과 적용을 위한 리스트
    sbop_zip = zip(score_list,bonus_list,option_list,star_option_plus)
    score_with_b_and_o = [(s**b)*o*p for s,b,o,p in sbop_zip]
    return sum(score_with_b_and_o)
    
def solution(dartResult):
    score_list, bonus_list, option_list = make_lists(dartResult)
    score_list = list(map(int,score_list))
    bonus_list = bonus_str_to_int(bonus_list)
    option_list = option_str_to_int(option_list)
    final_score = cal_final_score(score_list,bonus_list,option_list)
    return final_score
