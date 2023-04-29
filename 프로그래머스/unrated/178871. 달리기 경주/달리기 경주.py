def solution(players, callings):
    pi = {p:i for i,p in enumerate(players)}
    ip = {i:p for i,p in enumerate(players)}
    for u in callings:
        i = pi[u]
        d = ip[i-1]
        pi[u],pi[d],ip[i],ip[i-1] = i-1,i,d,u
    players = [ip[i] for i in range(len(players))]
    return players