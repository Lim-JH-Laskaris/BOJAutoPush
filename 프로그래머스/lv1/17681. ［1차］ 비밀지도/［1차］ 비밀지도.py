def solution(n, arr1, arr2):
    arr1 = map(lambda x: str(bin(x))[2:].rjust(n,'0'), arr1)
    arr2 = map(lambda x: str(bin(x))[2:].rjust(n,'0'), arr2)
    return [''.join([' ' if c+d =='00' else '#' for c,d in zip(a,b)])for a,b in zip(arr1,arr2)]