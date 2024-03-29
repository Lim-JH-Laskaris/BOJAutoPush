def solution(n,q=[]):
    """dfs를 사용. 한 열에 퀸은 반드시 하나가 들어감(nxn보드에 n개의 퀸이 들어가므로)에 착안, 
    각 열의 몇 행에 퀸이 들어가는지를 q리스트에 기록하고, 
    이에따라 다음 열에서 퀸이 놓일 수 있는 행(board)을 찾아 dfs를 수행.
    """
    board = [1]*n
    column_index = len(q)
    if column_index == n : #배치해야할 모든 퀸을 배치했다면.
        return 1
    for i in range(column_index): #이전 퀸들로 인해 놓을 수 없는 지점을 소거
        pre_q_row = q[i] 
        dist = column_index-i #열간격. 대각선 착지불가지점 계산에 활용
        board[pre_q_row] = 0
        if pre_q_row+dist< n : board[pre_q_row+dist] = 0
        if pre_q_row-dist>=0 : board[pre_q_row-dist] = 0
    if sum(board) == 0 : #더이상 배치할 수 있는 자리가 없다면. 
        return 0
    else : #배치할 수 있는 자리가 있다면, 그곳에 배치하고 dfs 탐색
        return sum([solution(n,q=q+[i]) for i in range(n) if board[i]])