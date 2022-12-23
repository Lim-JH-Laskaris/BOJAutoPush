solution = lambda n , r=0 : r if n==0 else (
    solution(n-1, r+1) if ((r+1)%3)*('3' not in str(r+1)) else solution(n, r+1))  
