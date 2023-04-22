def solution(N, number):
    if N==number : return 1
    can_num = {i:{int(str(N)*i)} for i in range(1,10)}
    for i in range(2,9):# can_num의 새로운 key (7까지만 계산)
        for j in range(1,i): #can_num의 기존 키
            # print(i,j,i-j)
            for k in can_num[j]:
                for l in can_num[i-j]:
                    can_num[i] = can_num[i].union({k+l,k-l,k*l})
                    if l!=0 and k%l==0: can_num[i].add(k//l)
            if number in can_num[i] : return i
    # print(can_num)
    return -1