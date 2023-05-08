def date(day):
    '2000.01.01을 0일로 두고 하루씩 셈'
    day = day.split('.')
    return (int(day[0])-2000)*28*12 + (int(day[1])-1)*28 + (int(day[2])-1)

def solution(today, terms, privacies):
    today = date(today) # 2022.05.19 -> 
    terms = {t.split()[0]:int(t.split()[1])*28 for t in terms} # {A:6*28}
    answer = []
    for i in range(len(privacies)):
        d,t = privacies[i].split()
        if date(d)+terms[t] <= today: # 수집 유효기간이 지났으면.
            answer.append(i+1)
    return answer