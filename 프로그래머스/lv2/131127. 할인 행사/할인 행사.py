from collections import defaultdict
from copy import deepcopy

def solution(want, number, discount):
    # discount 기준, 전체 상품 기본 dict 생성. 예) {상품:0}
    all_product = defaultdict(int)
    for i in list(set(discount)):
        all_product[i]
        
    # 기본dict를 바탕으로 원하는 상품의 수량을 덧씌움
    want_num_dict = deepcopy(all_product)
    for w,n in zip(want,number):
        want_num_dict[w] =n
        
    # 기본dict를 바탕으로 첫10일간의 할인 상품들을 count하고, 일치여부판단
    discount10day_dict = deepcopy(all_product)
    for i in discount[0:10]:
        discount10day_dict[i] +=1
    c = 1 if want_num_dict == discount10day_dict else 0
    
    # 그다음부터의 계산은 기존의 dict에서 빼고 더하는 식으로 계산량 줄임 
    for i in range(len(discount)-10):
        discount10day_dict[discount[i]] -= 1
        discount10day_dict[discount[i+10]] += 1 
        if want_num_dict == discount10day_dict: c+=1
    return c