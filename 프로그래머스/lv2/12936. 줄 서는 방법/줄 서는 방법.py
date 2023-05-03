def factorial(x):
    return 1 if x==0 else x*factorial(x-1)

def solution(n, k):
    answer = []
    k -= 1 
    n = list(range(1,n+1))
    while n : 
        d, k = k//factorial(len(n)-1),k%factorial(len(n)-1)
        answer.append(n.pop(d))
    return answer