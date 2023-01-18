def check_odd_palindrome(s,mod_index):
    """문자열 s 에서 mod_index번째 문자를 중심으로 하는 
    홀수 길이의 팰린드롬의 최대 길이를 찾는 함수"""
    last_index = len(s) -1
    a = 0
    while mod_index-a >= 0 and mod_index+a <= last_index:
        if s[mod_index-a] != s[mod_index+a] : break
        else : a += 1
    return a*2-1

def check_even_palindrome(s,mod_index):
    """문자열 s 에서 mod_index번째 문자와 mod_index+1번째 문자를 중심으로 하는 
    짝수 길이의 팰린드롬의 최대 길이를 찾는 함수"""
    last_index = len(s) -1
    a = 0
    while mod_index-a >= 0 and mod_index+1+a <= last_index:
        if s[mod_index-a] != s[mod_index+1+a] : break
        else : a += 1
    return a*2    

def solution(s):
    """ 홀수 길이 팰린드롬 중 최대값과 짝수 길이 팰린드롬 중 최대값 중 큰 값을 반환
    """
    max_odd_palindrome  = max([check_odd_palindrome(s,i)  for i in range(len(s))])
    max_even_palindrome = max([check_even_palindrome(s,i) for i in range(len(s))])
    return max(max_odd_palindrome,max_even_palindrome)