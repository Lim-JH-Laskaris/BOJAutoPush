def is_babbling(word):
    """한 단어가 조카가 발음가능한지 여부를 0,1로 반환
    
    Args :
        word (str) : 발음가능한지 판단해야하는 단어
    
    Returns :
        같은 발음이 연속되거나 불가능한 발음이 있으면 0
        그렇지 않은 경우 1
    """
    pronunciation = ["aya", "ye", "woo", "ma"]
    for i in range(len(pronunciation)):
        word = word.replace(pronunciation[i],f'{i}')
    for i in range(len(pronunciation)):
        if f'{i}{i}' in word: return 0
    return 1 if word.isdigit() else 0

    
def solution(babbling):
    babbling_list = [is_babbling(i) for i in babbling]
    return sum(babbling_list)