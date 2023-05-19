n = int(input())
score = [int(input()) for _ in range(n)]
if n<3 : 
    print(sum(score))
else:
    step = [[(score[0],0)],[(score[1],0),(score[0]+score[1],1)]] 
        # list<list<(int,int)>> :[[(누적점수,연속스택)]] 
        # 연속스택: 해당 스탭 직전에 연속으로 밟은 계단수. 큰점프면 0, 작은걸음은 1, 2는 3연속이므로 불가능
    for i in range(2,n):
        step.append([])
        # 두계단 전에서 크게 올라오는 경우 - 스택 0로 초기화 (가장 점수가 큰 것만 더함)
        step[i].append((max(step[i-2])[0]+score[i],0)) 
        # 한계단 전에서 작게 올라오는 경우 - 스택 +1함 (이미 1인 경로는 업데이트 불가능)
        step[i].extend([(a+score[i],1) for a,b in step[i-1] if b<1])
    print(max(step[-1])[0])
    