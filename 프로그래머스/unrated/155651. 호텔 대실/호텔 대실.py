from heapq import heapify, heappush, heappop
def solution(book_time):
    book_time = list(map(lambda x: 
                         list(map(lambda y: int(y[:2])*60+int(y[3:]),x)),
                         book_time))
                # 시각을 분단위 정수시각으로 변환
    # book_time.sort()
    heapify(book_time)
    use_heapq = [] # 종료시각만 원소로 넣음. 넣을 때 준비시간도 포함예정.
    answer = 0 # use_heapq의 최대 길이.
    # for b in book_time:
    while book_time:
        while use_heapq and use_heapq[0]<=book_time[0][0] : #b시작시각 전에 끝나는 예약이 있다면,
            heappop(use_heapq)
        # heappush(use_heapq,b[1]+10) #앞서 말했듯 종료시각 +10분 추가
        heappush(use_heapq,heappop(book_time)[1]+10) #앞서 말했듯 종료시각 +10분 추가
        answer = max(answer, len(use_heapq)) 
    return answer