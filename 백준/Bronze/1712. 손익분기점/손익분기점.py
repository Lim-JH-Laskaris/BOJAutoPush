    # a는 고정비용, b는 가변비용, c는 가격
    # 변수명은 문제를 따름
input_ = input()
a,b,c = input_.split(' ')
a,b,c = int(a),int(b),int(c)

    # 이때 c-b를 한계이익(Marginal Benefit)이라한다.
    # 한계이익이란 제품 한단위를 더 팔때 추가되는 이익을 의미
marginal_benefit = c-b

    # 만약 한계이익이 0보다 작으면 팔면팔수록 손해이고, 
    # 한계이익이 0이면 a가 음수가 아닌한 총이익이 양수가 될 수 없으므로 두 경우 -1리턴
    
if marginal_benefit<=0: print(-1)
    
    # 고정비용을 한계이익으로 나누면, 손익분기점 직전의 판매량이 구해진다.
    # 여기에 1을 더해 리턴 
else : print(a//marginal_benefit +1)
