solution=lambda word:len(word)+sum(['AEIOU'.index(word[i])*[781,156,31,6,1][i] for i in range(len(word))])


"""
#아래는 가장 기본적인 완전탐색법
def solution(word):
    c = 0 
    for i1 in 'AEIOU':
        c+=1
        if word == i1 : return c
        for i2 in 'AEIOU':
            c+=1
            if word == i1+i2 : return c
            for i3 in 'AEIOU':
                c+=1
                if word == i1+i2+i3 : return c
                for i4 in 'AEIOU':
                    c+=1
                    if word == i1+i2+i3+i4 : return c
                    for i5 in 'AEIOU':
                        c+=1
                        if word == i1+i2+i3+i4+i5 : return c

#위의 식을 재귀함수로 짧게 나타냈다. 하지만 알아보기 힘들고 깔끔하지 못하다... 좋은 코드를 보며 익혀야 할듯
def solution(word, s='',c=0): 
    if word == s : return c, True
    elif len(s)<5 :
        for i in 'AEIOU':
            c+=1
            c,tf = solution(word, s+i,c)
            if   s!='' and tf : return c, True
            elif s=='' and tf : return c
    return c, False
"""
