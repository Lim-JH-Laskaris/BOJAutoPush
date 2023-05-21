class TriangleDict(dict):
    def __init__(self):
        for i,x in enumerate([1,1,1,2,2]):
            self[i] = x
    def __missing__(self,k):
        self[k] = self[k-1]+self[k-5]
        return self[k]

tri_dict = TriangleDict()
test_cases = [int(input()) for _ in range(int(input()))] 
for n in test_cases:
    print(tri_dict[n-1])
        