def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
  
#stack =[]으로 바꾸고 for num in number: 로 바꾸어도 동일
"""
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.14ms, 10.3MB)
테스트 5 〉	통과 (0.38ms, 10.1MB)
테스트 6 〉	통과 (3.78ms, 10.2MB)
테스트 7 〉	통과 (12.42ms, 10.5MB)
테스트 8 〉	통과 (28.52ms, 10.6MB)
테스트 9 〉	통과 (48.15ms, 13.1MB)
테스트 10 〉통과 (124.08ms, 13.5MB)
테스트 11 〉통과 (0.00ms, 10.1MB)
테스트 12 〉통과 (0.00ms, 10.1MB)
"""
