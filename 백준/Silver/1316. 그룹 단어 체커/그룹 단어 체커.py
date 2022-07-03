c=0
for i in range(int(input())):
    l = [ chr(i) for i in range(97,123) ]
    a = '?'
    t=input()
    for j in range(len(t)):
        if t[j] in l: 
            a = t[j]
            l.remove(t[j])
        elif t[j] == a: pass
        else: 
            c -= 1
            break
    c +=1
print(c)