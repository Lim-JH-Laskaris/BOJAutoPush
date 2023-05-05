def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
  
"""
비트 연산자
a^b : XOR 

bin(0b1101 & 0b1001)    # 비트 AND
'0b1001'

>>> 13 & 9                  # 비트 AND
9

>>> bin(0b1101 | 0b1001)    # 비트 OR
'0b1101'

>>> 13 | 9                  # 비트 OR
13

>>> bin(0b1101 ^ 0b1001)    # 비트 XOR
'0b100'

>>> 13 ^ 9                  # 비트 XOR
4
>>> bin(~0b1101)            # 비트 NOT
'-0b1110'

>>> ~13                     # 비트 NOT
-14
출처 : https://dojang.io/mod/page/view.php?id=2460
"""
