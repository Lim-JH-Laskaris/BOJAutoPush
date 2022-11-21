def is_babbling(word):
    pronunciation = ["aya", "ye", "woo", "ma"]
    for i in range(len(pronunciation)):
        word = word.replace(pronunciation[i],f'{i}')
    for i in range(len(pronunciation)):
        if f'{i}{i}' in word: return 0
    return 1 if word.isdigit() else 0

    
def solution(babbling):
    babbling_list = [is_babbling(i) for i in babbling]
    return sum(babbling_list)