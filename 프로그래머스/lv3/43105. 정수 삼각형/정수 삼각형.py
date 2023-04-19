def solution(triangle):
    """아래에서부터 역으로 경로를 선택하며 올라가는 방식.
    n번째 줄의 각 숫자들에서 n+1번째 줄로 가는 경로를 선택할 때,
    n-1 이하의 줄들의 숫자가 무엇이었는지는 영향을 미치지 못한다. 이를 이용.
    """
    lower_numbers = triangle.pop()
    while triangle:
        upper_numbers = triangle.pop()
        for i in range(len(upper_numbers)):
            next_root = max(lower_numbers[i:i+2])
            upper_numbers[i] += next_root
        lower_numbers = upper_numbers
    return lower_numbers[0]