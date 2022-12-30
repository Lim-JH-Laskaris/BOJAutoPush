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
    if answer[0] == 0 :
        if answer[1] == 0 : 
            return ''
        else :
            return str(answer[1])
    elif answer[0] == 1:
        if answer[1] == 0 : 
            return 'x'
        else :
            return f'x + {answer[1]}'
    else:
        if answer[1] == 0 : 
            return str(answer[0])+'x'
        else :
            return f'{answer[0]}x + {answer[1]}'