def solution(citations):
    """citations리스트를 역정렬하면, 
    해당 리스트의 인덱스+1은 해당 요소 값 이상의 요소의 개수를 의미. 
    이를 토대로 지수의 조건을 만족하는 최초의 숫자를 반복문으로 구한다.
    반복문 도중에 처음으로 조건에 만족하는 수가 나오면 그대로 출력한다.
    반복문이 완료되었다면 모든 논문의 인용수가 인덱스보다 크다는 뜻이므로 
    리스트의 길이(출판논문수)를 출력한다.
    """
    citations.sort(reverse=True)
    print(citations)
    for i in range(len(citations)):
        if i+1 > citations[i]:
            return i
    return len(citations)
    