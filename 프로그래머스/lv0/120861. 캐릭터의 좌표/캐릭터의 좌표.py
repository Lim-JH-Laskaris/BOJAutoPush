def solution(keyinput, board):
    move = {'up':[0,1],'down':[0,-1],'left':[-1,0],'right':[1,0]}
    minmax_x, minmax_y = board[0]//2, board[1]//2
    x,y = 0,0
    while keyinput:
        dx,dy = move[keyinput.pop(0)]
        x = min(minmax_x, max(-minmax_x,x+dx))
        y = min(minmax_y, max(-minmax_y,y+dy))
    return [x,y]