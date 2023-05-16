def solution(n, s):
    """중복집합내 원소가 균일할 수록 곱의 값이 커진다."""
    if n>s :return [-1]
    d,m = divmod(s,n)
    return [d]*(n-m)+[d+1]*m