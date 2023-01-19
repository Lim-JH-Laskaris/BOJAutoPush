def solution(n):
    """최단거리 경우의수 문제로 치환해서 풀었습니다. 
    괄호 문자열을 맨앞문자 부터 차례로 받아, '('이면 x축으로+1, ')' y축으로+1 이동한다고 합시다.
    이때 '(',')'모두 n개 있으므로, 총 이동가능한 지도는 정사각형 모양이 됩니다.
    단, x=y 선위에 있는 지점들은 예를들어 '())'같은 경우로, 이미 올바르지 못하기 때문에 이방향으로는 갈 수 없으니 지워줍니다.
    이 다음은 구글에서 최단거리 경우의 수 공식을 검색해보시면, 고등학교시절 기억을 되새기실 수 있을 겁니다.
    """
    prev_list = [1]*(n+1)
    for i in range(n):
        prev_num = 0
        next_list = []
        for i in prev_list[1:]:
            prev_num += i
            next_list.append(prev_num)
        prev_list = next_list
    return prev_num   
            
    