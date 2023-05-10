def shift(a,i,skip):
    if i==0: 
        return a
    next_a = chr((ord(a)+1-97)%26+97)
    if next_a in skip : 
        return shift(next_a,i,skip)
    else : 
        return shift(next_a,i-1,skip)
    
def solution(s, skip, index):
    return ''.join([shift(a,index,skip) for a in s])
    

