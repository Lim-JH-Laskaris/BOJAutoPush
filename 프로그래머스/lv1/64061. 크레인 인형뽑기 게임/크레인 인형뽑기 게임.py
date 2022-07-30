def take_up_puppet(board,line,deepth=0):
    """지정된 라인에 맞춰 인형 높이가 높은 곳에서 부터 탐색하여 찾아내고,
    인형을 찾으면 인형과, 바뀐 board를 같이 출력하는 함수.
    특정 높이에서 인형이 존재하지 않으면 그 아래를 탐색하는 함수를 재귀적으로 호출.
    만약 맨 아래단 까지 갔음에도 인형이 없다면 0을 출력
    """
    if len(board)==deepth:
        return 0, board
    elif board[deepth][line-1]==0:
        return take_up_puppet(board,line,deepth+1) 
    else : 
        puppet, board[deepth][line-1] = board[deepth][line-1], 0
        return puppet, board

def solution(board, moves):
    """ 각 move별로 순서대로 take_up_puppet를 출력하며,
    이때 나온 인형 값과 바구니 안의 마지막 인형이 동일한지를 비교한다.
    만약 출력된 인형이 0이라면(아무것도 뽑지 못했다면), 그대로 다음 함수로 넘어간다.
    만약 동일한 인형이면 바구니의 마지막 인형을 제거하고(함수에서 나온 인형도 넣지 않게 된다.)
    동일한 인형이 아니거나 바구니가 비어있다면, 함수에서 나온 인형을 바구니에 추가한다.
    제거 할 때마다 count변수에 2씩 추가하여 최종적으론 count를 리턴
    """
    basket = []
    count  = 0
    for move in moves:
        puppet, board = take_up_puppet(board,move)
        if puppet == 0:
            continue
        elif len(basket)!=0 and basket[-1]==puppet:
            basket.pop()
            count += 2
        else : 
            basket.append(puppet)
    return count