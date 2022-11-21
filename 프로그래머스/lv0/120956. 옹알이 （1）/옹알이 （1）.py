def is_babbling(word):
    pronunciation = ["aya", "ye", "woo", "ma"]
    for i in pronunciation:
        word = word.replace(i,' ')
    return 1 if word.isspace() else 0 
    
def solution(babbling):
    babbling_list = [is_babbling(i) for i in babbling]
    return sum(babbling_list)