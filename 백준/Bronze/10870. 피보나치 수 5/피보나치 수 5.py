class FibDict(dict):
    def __init__(self):
        self[0] = 0
        self[1] = 1
    def __missing__(self, k):
        self[k] =self[k-1] + self[k-2]
        return self[k]
    
a = int(input())
fib_dict = FibDict()
print(fib_dict[a])