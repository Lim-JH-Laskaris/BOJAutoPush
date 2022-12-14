solution = lambda my_string, answer='': answer if my_string=='' else (
    solution(my_string[1:],answer) if my_string[0] in answer
    else solution(my_string[1:],answer+my_string[0])
)

"""출력할 문자열을 answer에 하나씩 쌓아갑니다. my_string문자를 맨앞부터 하나씩 검사하여, 
answer에 있으면 넘어가고, 없으면 추가합니다. my_string의 끝에 도달하면 answer를 출력합니다.
"""