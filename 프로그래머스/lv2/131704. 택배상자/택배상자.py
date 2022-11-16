from collections import deque

def solution(order):
    queue_belt = deque(range(1,len(order)+1)) # 기본 벨트
    stack_belt = deque() # 보조 벨트
    truck = [] # 운송 트럭
    for i in range(len(order)): #순서 확인
        while True :
            if   len(queue_belt) and order[i] == queue_belt[0] : 
                # 기본 벨트가 비어있지 않고 기본벨트 첫번째 원소가 순서목록의 i원소와 일치하면
                truck.append(queue_belt.popleft()) #기본 벨트 해당 원소를 빼서 트럭에 추가
                break # 다음 순서 뽑기
            elif len(queue_belt) and order[i] > queue_belt[0] : 
                # 기본 벨트가 비어있지 않고 기본벨트 첫번째 원소가 순서목록의 i원소 보다 작으면
                stack_belt.append(queue_belt.popleft()) # 기본 벨트 해당 원소를 보조 벨트에 추가
                continue # 큐 새로 뽑기
            elif order[i] == stack_belt[-1] :
                # 기본 벨트가 비어있거나 기본 벨트 첫번째 원소가 순서목록 i원소보다 클 때, 
                # 이때 보조 벨트 마지막 원소(가장 최근에 추가된 원소)가 순서목록 i원소와 같으면
                truck.append(stack_belt.pop()) # 보조 벨트 해당 원소를 트럭에 추가
                break # 다음 순서 뽑기
            elif order[i] != stack_belt[-1] :
                # 기본 벨트가 비어있거나 기본 벨트 첫번째 원소가 순서목록 i원소보다 클 때, 
                # 이때 보조 벨트 마지막 원소(가장 최근에 추가된 원소)가 순서목록 i원소와 다르면
                return len(truck) # 모든 과정을 종료하고 지금까지 트럭에 실은 물건의 갯수 출력
    return len(truck) # 반복문의 루프를 모두 완료하였으므로 지금까지 트럭에 실은 물건의 갯수 출력


# ps. 테스트 1번에서 4,3 번 포기하고 1,2,5 번을 실으면 총 3개를 운송할 수 있게 되는것이 아닌가 싶다.
# ps. 물론 필자도 , 전체 order를 보고 최적화를 하는 것이 아니라 order가 들어오는 순서대로 알고리즘을 짰다..