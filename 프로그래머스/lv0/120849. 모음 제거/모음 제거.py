solution = lambda my_string, c=0 : solution(my_string.replace('aeiou'[c],''), c+1) if c<5 else my_string
