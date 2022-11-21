def is_babbling(str_):
    pronunciation = ["aya", "ye", "woo", "ma"]
    for i in pronunciation:
        str_ = str_.replace(i,' ')
    return 1 if str_.isspace() else 0 
    

def solution(babbling):
    babbling_list = [is_babbling(i) for i in babbling]
    return sum(babbling_list)