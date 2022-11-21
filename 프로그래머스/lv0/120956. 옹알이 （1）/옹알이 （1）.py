def is_babbling(word):
    pronunciation = ["aya", "ye", "woo", "ma"]
    for i in pronunciation:
        word = word.replace(i,' ',1)
    return 1 if word.isspace() else 0 
    
def solution(babbling):
    babbling_list = [is_babbling(i) for i in babbling]
    return sum(babbling_list)

# 문제에는 최대 한번씩만 사용할 수 있다고 하는데 그걸 고려하지 않아도 통과되네요
# word = word.replace(i,' ',1)을 word = word.replace(i,' ')로만 써도 되는 이상이 있습니다.