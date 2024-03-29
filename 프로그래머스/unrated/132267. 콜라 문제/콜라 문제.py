import sys
sys.setrecursionlimit(3000) # 이 부분 질문하기 게시판의 답변 참고

def solution(a:int, b:int, n:int, c:int=0):
    """ 빈병으로 받을 수 있는 콜라 수를 반환하는 재귀함수 입니다.
    Args:
        a : 콜라를 받기 위해 마트에 주어야 하는 병 수
        b : 빈 병 a개를 가져다 주면 마트가 주는 콜라 병 수
        n : 상빈이가 가지고 있는 빈 병의 개수
        c : 현재까지 받은 콜라의 누적수량, 초기값 0으로 지정
        
    Returns:
        a>n 인 경우, 재귀과정을 종료하고 누적수량을 반환. 
        그렇지 않은 경우, 가능한 빈병을 모두 주고 콜라를 받는 과정을 수행 한 값을 
        인수로 주고 해당 함수를 반환
        
    Notes:
        처음엔 재귀한계 탓에 테스트 12번에서 런타임에러 발생.
        재귀한계를 통과 가능한 수준으로 수정
    """
    if a>n : return c
    else   : return solution(a,b,b*(n//a)+n%a,c+b*(n//a))
    