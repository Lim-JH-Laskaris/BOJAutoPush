def ntrans(n,d):
    """x를 n진수로 변환, 단, 자리수의 리스트 형태로"""
    return (ntrans(n,d//n) if d//n!=0 else []) + [d%n]

def solution(n, t, m, p):
    p -= 1 # 0부터 시작하도록
    digit = [str(i) for i in range(10)] + [chr(i) for i in range(65,71)]
    say_nums = [] # 여기에 10진수의 경우 다음과 같이 채워짐 [0,1,...8,9,1,0,1,1,..]
    d = 0
    while len(say_nums)<t*m: 
        say_nums = say_nums + ntrans(n,d)
        d += 1
    say_nums = list(map(lambda x:digit[x], say_nums)) # 문자열로 바꿔주기 위함
    return ''.join(say_nums[p::m][:t])

