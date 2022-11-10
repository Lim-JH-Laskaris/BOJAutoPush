def solution(elements):
    cumulative_sum = [sum(elements[:i+1]) for i in range(len(elements))]
    elements_sum = sum(elements)
    subsequence_sum = set(cumulative_sum)
    for i in range(len(elements)):
        pop_num = cumulative_sum.pop(0)
        cumulative_sum = [i-pop_num for i in cumulative_sum]
        subsequence_sum = subsequence_sum.union(set(cumulative_sum))
        cumulative_sum.append(elements_sum)
    return len(subsequence_sum)

"""
테스트1을 예시로 우선 7부터 마지막 수인 4까지의 누적합 수열을 구합니다.
[7,  16,  17,  18,  22] 이 수열은 7로 시작하는 부분수열의 합들입니다.
여기에서 첫 수인 7을 뽑아내고, 나머지 수에 모두 7을 빼준다음 맨뒤에 전체합인 22를 추가하면(큐)
[9,  10,  11,  15,  22] 이 수열은 9로 시작하는 부분수열의 합들입니다.
이러한 과정을 전체 수열의 원소 수만큼 반복해주면, 각각의 원소로 시작하는 부분수열의 합이 모두 구해지므로,
이를 set자료형으로 합집합을 구하여 그 크기를 함수가 출력하게끔 합니다.
"""