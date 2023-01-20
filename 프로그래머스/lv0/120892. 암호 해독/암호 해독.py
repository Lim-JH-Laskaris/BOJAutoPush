#solution = lambda cipher, code : ''.join([cipher[i] for i in range(code-1,len(cipher),code)])
solution = lambda cipher, code : cipher[code-1::code]