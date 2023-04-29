def solution(s):
    s = list(s.lower()+' ')
    bar = [0]+[i+1 for i in range(len(s)) if s[i]==' '][:-1]
    for i in bar:
        s[i] = s[i].upper()
    return ''.join(s[:-1])
