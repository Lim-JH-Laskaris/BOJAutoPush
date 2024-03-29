### 힙 관련 내용
[프로그래머스-더맵게](../../../tree/main/프로그래머스/lv2/42626.%E2%80%85더%E2%80%85맵게)
* https://www.daleseo.com/python-heapq/
* https://hocheon.tistory.com/70


### 파이썬 리스트 요소삭제 방법들
* https://ponyozzang.tistory.com/587

### 문자열 포맷팅 
[백준-ACM 호텔](../../../tree/main/백준/Bronze/10250.%E2%80%85ACM%E2%80%85호텔)
* https://datascienceschool.net/01%20python/02.04%20파이썬의%20문자열%20형식화%20.html
* https://www.w3schools.com/python/ref_string_format.asp

### 백준 input 시간초과 -> sys.stdin.readline()
* https://hooongs.tistory.com/131

### exec 관련
* https://jvvp.tistory.com/1162

### itertools 공식문서
* https://docs.python.org/ko/3/library/itertools.html
* 순열 permutations(list_, n)
* 조합 combinations(list_, n)

### bisect 공식문서 
* https://docs.python.org/3.10/library/bisect.html

### collections 관련
* Counter : https://www.daleseo.com/python-collections-counter/
* defaultdict : https://dongdongfather.tistory.com/69
    - defaultdict는 주어진 객체의 기본값을 설정 가능. dfd = defaultdict(list) 처럼. https://dongdongfather.tistory.com/69
* deque과 기본리스트의 시간복잡도 비교 : https://wellsw.tistory.com/122
    - extend,extendleft : 여러개 추가 가능
    
### functools 관련 내용
[프로그래머스-숫자 카드 나누기](../../../tree/main/프로그래머스/unrated/135807.숫자 카드 나누기)
* 누계함수 reduce(집계 함수, 순회 가능한 데이터[, 초기값]) / from functools import reduce
    - [docs](https://docs.python.org/ko/3/library/functools.html#functools.reduce)
    - ex1) reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])는 다음과 같이 계산 ((((1+2)+3)+4)+5)
    - n개의 수에 대한 최대 공약수 : from math import gcd; reduce(gcd, nums_list)

### sys 관련
* 재귀 한계 재설정 : sys.setrecursionlimit(10**5)
