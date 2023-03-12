def solution(t, p):
    n_p = len(p)
    int_p = int(p)
    c = 0
    t, sub_t = t[n_p:],t[:n_p]
    if int(sub_t)<=int_p : c+=1
    while t:
        t, sub_t = t[1:],sub_t[1:]+t[0]
        if int(sub_t)<=int_p : c+=1
    return c