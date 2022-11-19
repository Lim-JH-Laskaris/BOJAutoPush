def solution(A:str, B:str, N:int=0):
    """ A문자열을 오른쪽으로 몇 번 밀어야 B문자열을 만들 수 있는지
    찾는 재귀함수
    
    Args:
        A : 밀어야 하는 문자열
        B : 밀어서 만들어야하는 문자열
        N : 재귀 과정을 몇 번 거쳤는지(몇 번 밀었는지)를 의미
        
    Returns:
        A와B가 같으면 지금까지 밀어낸 횟수 N을 반환.
        A와B가 다르면서 N이 A의 길이와 같다면, A로 B를 못 만들기에 -1 반환
        둘다 아니면, A를 한 칸씩 밀고 N에 1을 더하여 이 함수를 재귀적으로 호출
    """
    if   A==B      : return N
    elif N==len(A) : return -1 
    else : return solution(A[-1]+A[:-1],B,N+1)