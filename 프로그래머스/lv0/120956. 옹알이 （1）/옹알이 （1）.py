def is_babbling(word):
    pronunciation = ["aya", "ye", "woo", "ma"]
    for i in pronunciation:
        word = word.replace(i,' ',1) 
        # 제한사항에 한번만 등장한다 되어있으니 세번째 인수 1 없어도 무관
    return 1 if word.isspace() else 0 
    
def solution(babbling):
    babbling_list = [is_babbling(i) for i in babbling]
    return sum(babbling_list)