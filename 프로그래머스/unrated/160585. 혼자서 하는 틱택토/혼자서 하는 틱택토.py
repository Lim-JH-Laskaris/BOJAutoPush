def solution(board):
    t_board = [board[0][i]+board[1][i]+board[2][i] for i in range(3)] #전치행렬
    x_board = [board[0][0]+board[1][1]+board[2][2], 
               board[0][2]+board[1][1]+board[2][0]] # 대각선 방향에 'OOO'나'XXX'유무 확인
    all_board = board+t_board+x_board 
    l_board = list(board[0]+board[1]+board[2]) # 아래에서 o,x 개수 세기 위함
    o = l_board.count('O')
    x = l_board.count('X')
    if x>o or o>x+1: return 0 # 승패 상관없이, 가능한 o,x 개수인지 확인
    if 'OOO' in all_board:
        if 'XXX' in all_board or x==o: return 0
    if 'XXX' in board+t_board+x_board:
        if not x==o: return 0
    return 1