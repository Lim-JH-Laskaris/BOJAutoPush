import numpy as np 


def solution(board):
    n = len(board)
    board_np = np.array(board)
    safezone = [sum([1 if np.sum(board_np[max(0,i-1):min(n,i+2),max(0,j-1):min(n,j+2)])==0 else 0 for j in range(n)]) for i in range(n)]
    return sum(safezone)
