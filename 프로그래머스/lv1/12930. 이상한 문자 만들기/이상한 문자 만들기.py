def change_one_word(word):
    return ''.join([word[i].upper() if i%2==0 else word[i].lower() for i in range(len(word))])

def split_with_space(s):
    """공백이 한 칸이 아닌 경우도 있다는 말이 있어서 s.split() 함수 대신,
    공백도 같이 분리해주는 함수를 만들어 사용.
    """
    s = list(s)
    word_and_space = []
    if s : a = s.pop(0)
    while s :
        b = s.pop(0)
        if (' ' not in a and b !=' ') or (' ' in a and b ==' '): 
            a = a+b
        else:
            word_and_space.append(a)
            a = b
    word_and_space.append(a)
    return word_and_space

def solution(s):
    return ''.join([change_one_word(word) if ' ' not in word else word for word in split_with_space(s)])