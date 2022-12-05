solution = lambda s: ''.join([i for i in sorted(list(set(s))) if s.count(i)==1])
    