def div_list(list_,div=2):
    # 리스트의 원소들을 모두 2로 나눔
    return list(map(lambda x:x//div, list_))
    
def place_food(food_div):
    # food_div에 맞추어 한 사람의 순서대로 문자열 생성 하고 0과 반대 사람의 음식순서를 추가
    place_food_on_one_side = ''.join([str(i)*food_div[i] for i in range(len(food_div)) if i>0])
    return place_food_on_one_side + '0' + place_food_on_one_side[::-1]

def solution(food):
    food_div = div_list(food)  
    answer = place_food(food_div)
    return answer