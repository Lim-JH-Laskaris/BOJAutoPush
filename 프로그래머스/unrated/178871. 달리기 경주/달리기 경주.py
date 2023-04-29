def solution(players, callings):
    pi = {p:i for i,p in enumerate(players)}
    ip = {i:p for i,p in enumerate(players)}
    for u in callings:
        i = pi[u]
        d = ip[i-1]
        pi[u],pi[d],ip[i],ip[i-1] = i-1,i,d,u
    players = [ip[i] for i in range(len(players))]
    return players

# 처음엔 아래와 같이 리스트에서 직접 바꿔주는 방법을 취했는데, 시간 초과가 떴다.
# def solution(players, callings):
#     for c in callings:
#         i = players.index(c)
#         players[i-1],players[i] = players[i],players[i-1]
#     return players
