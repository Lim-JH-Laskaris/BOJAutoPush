def solution(polynomial):
    polynomial = ' '+polynomial+' '
    polynomial = polynomial.replace(' x ',' 1x ')[1:-1]
    poly_list = polynomial.split(' + ')
    
    answer = [0,0]
    while poly_list :
        if poly_list[-1][-1] =='x':
            answer[0] += int(poly_list.pop()[:-1])
        else :
            answer[1] += int(poly_list.pop())
            
    if   answer[0] == 0 : answer_str = ''
    elif answer[0] == 1 : answer_str = 'x'
    else : answer_str = f'{answer[0]}x'
         
    if answer[1] > 0 and answer_str != '' : 
        answer_str = answer_str+' + '
            
    if answer[1] > 0 : 
        answer_str = answer_str+f'{answer[1]}'
        
    return answer_str
    
