from heapq import heapify, heappush, heappop
def solution(book_time):
    book_time = list(map(lambda x: 
                         list(map(lambda y: int(y[:2])*60+int(y[3:]),x)),
                         book_time))
                # 시각을 분단위 정수시각으로 변환
    book_time.sort()
    use_heapq = [] # 종료시각만 원소로 넣음. 넣을 때 준비시간도 포함예정.
    answer = 0 # use_heapq의 최대 길이.
    for b in book_time:
        while use_heapq and use_heapq[0]<=b[0] : #b시작시각 전에 끝나는 예약이 있다면,
            heappop(use_heapq)
        heappush(use_heapq,b[1]+10) #앞서 말했듯 종료시각 +10분 추가
        answer = max(answer, len(use_heapq)) 
    return answer

"""book_time.sort()가 아닌 heapify(book_time)을 한뒤 pop해서 사용하는 방식을 실험해 봤으나
그 방법으로 할 때가 오히려 2배 정도 느린 것으로 나타난다."""