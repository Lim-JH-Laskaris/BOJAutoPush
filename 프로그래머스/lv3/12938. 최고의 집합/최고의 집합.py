def solution(n, s):
    """중복집합내 원소가 균일할 수록 곱의 값이 커진다."""
    if n>s :return [-1]
    answer = []
    for i in range(n,0,-1):
        j = s//i
        answer.append(j)
        s -= j
    return sorted(answer)