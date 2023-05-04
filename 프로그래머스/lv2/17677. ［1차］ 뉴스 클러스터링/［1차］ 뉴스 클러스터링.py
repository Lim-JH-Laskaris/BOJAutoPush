from collections import Counter

def is_az(x):
    """x가 소문자 알파벳인지 여부를 반환"""
    return ord(x)>=ord('a') and ord(x)<=ord('z')

def multiset(str_):
    """두문자씩 묶은 원소의 다중집합을 반환. 단, 소문자 알파벳으로 이루어진 원소만을 포함하여."""
    return [str_[i-1:i+1]  
            for i in range(1,len(str_)) if is_az(str_[i-1]) and is_az(str_[i])]
    
def solution(str1, str2):
    str1,str2 = str1.lower(),   str2.lower()
    set1,set2 = multiset(str1), multiset(str2)
    cnt1,cnt2 = Counter(set1),  Counter(set2)
    min_set   = sum([min(cnt1[i],cnt2[i]) 
                     for i in list(set(cnt1.keys()).intersection(cnt2.keys()))])
    max_set   = sum([max(cnt1[i],cnt2[i]) 
                     for i in list(set(cnt1.keys()).union(cnt2.keys()))])
    return int(65536*min_set/max_set) if max_set else 65536