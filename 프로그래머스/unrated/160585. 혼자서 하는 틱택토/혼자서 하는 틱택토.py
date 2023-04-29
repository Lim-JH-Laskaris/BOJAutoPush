def solution(board):
    t_board = [board[0][i]+board[1][i]+board[2][i] for i in range(3)]
    x_board = [board[0][0]+board[1][1]+board[2][2],
               board[0][2]+board[1][1]+board[2][0]]
    l_board = list(board[0]+board[1]+board[2])
    o = l_board.count('O')
    x = l_board.count('X')
    if x>o or o>x+1: return 0
    if 'OOO' in board:
        if 'XXX' in board or x==o: return 0
    if 'OOO' in t_board:
        if 'XXX' in t_board or x==o: return 0    
    if 'OOO' in x_board:
        if x==o: return 0 
    if 'XXX' in board+t_board+x_board:
        if not x==o: return 0
    return 1