def solution(prices):
    len_prices = len(prices)
    stack = []
    answer= [0]*len_prices
    stack_end = -1
    for i,p in enumerate(prices):
        if stack_end > p:
            while stack and stack[-1][1] > p:
                si,sp = stack.pop()
                answer[si] = i-si
        stack.append((i,p))
        stack_end = p
    while stack:
        si,sp = stack.pop()
        answer[si] = (len_prices-1)-si
    return answer
        
                
        