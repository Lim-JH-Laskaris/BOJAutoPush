from heapq import heapify, heappush, heappop

def solution(jobs): 
    """대기중인 작업(현재시각 전에 요청된 작업) 중 소요시간이 가장 적은 작업부터 처리하면
    요청부터 처리완료까지 걸린 평균 시간이 최소가 된다. 이 기준으로 요청을 처리하고 
    기록 후, 평균을 구해 반환하는 함수"""
    heapify(jobs)   # jobs 배열을 요청시간 기준의 힙으로 변환
    t = 0           # 현재시각
    working = []    # 작업 배열, 현재시각 이전에 들어온 요청을 담음
    answer  = []    # 요청부터 처리완료까지 걸린 시간을 기록할 배열
    while jobs or working: 
        while jobs and jobs[0][0] < t :     # 현재시각 이전에 요청이 왔다면
            a,b = heappop(jobs)             # jobs에서 working으로 옮겨담음
            heappush(working,[b,a])         # 소요시간을 기준으로 하기 위해 뒤집어 추가
        if not working :                    # 워킹 힙이 비어있다면
            a,b = heappop(jobs)
            heappush(working,[b,a])         # 가장 먼저 요청된 작업을 추가하고
            t = a                           # 그 작업의 요청시각을 현재시각으로 설정 
        b,a = heappop(working)  # 시작할 작업을 뽑음 
        t += b                  # 해당 작업의 소요시간 만큼 현재 시각에 더함
        answer.append(t-a)      # 요청으로부터 종료까지 걸린 시간을 기록
    return int(sum(answer)/len(answer))     # 평균 처리 소요시간(소수점버림)을 반환.