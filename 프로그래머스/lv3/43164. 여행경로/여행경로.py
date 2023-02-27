def dfs(tickets,departure='ICN',root=[]):
    if not tickets:
        return root+[departure]
    for i in range(len(tickets)):
        if tickets[i][0]==departure:
            travel = dfs(tickets[0:i]+tickets[i+1:],departure=tickets[i][1],root=root+[departure]) 
            if travel : return travel 
            # 처음엔 if 문 없이 return 했으나, 그렇게 하면 잘못된 경로에 들어섰을 땐 None을 리턴하게 되는 문제가 발생.
    return None

def solution(tickets):
    tickets.sort(key = lambda x : (x[0],x[1])) # 알파벳 순으로 앞선 경로를 따르기 위해 정렬 # x[1]만 해도 됨
    return dfs(tickets)