import itertools

class ScoreDict(dict):
    """총 24가지 경우의 조건에 해당하는 점수를 각각 모으고 높은 점수 순으로 정렬한 딕셔너리"""
    def __init__(self, list_info):
        self.search_space = [
            ['cpp', 'java', 'python'],  
            ['backend', 'frontend'],
            ['junior', 'senior'],
            ['chicken', 'pizza']
        ]
        for i in itertools.product(*self.search_space):
            self['_'.join(i)] = []
        for i in range(len(list_info)):
            self['_'.join(list_info[i][:-1])].append(list_info[i][-1])
        for i in itertools.product(*self.search_space):
            self['_'.join(i)].sort(reverse=True)
        
    def run_query(self, one_query):
        """하나의 쿼리에 대해 쿼리의 결과를 출력하는 메소드"""
        search_space = [[one_query[i]] if one_query[i]!='-' else self.search_space[i] for i in range(4)]
        search_space = ['_'.join(i) for i in itertools.product(*search_space)]
        return sum([binary_compare_count(self[i], one_query[4]) for i in search_space])   

def binary_compare_count(reverse_sorted_list, number):
    """이진 탐색 방식으로, 역정렬된 리스트에서 특정 숫자보다 큰 숫자의 개수를 찾는 함수"""
    a,b = 0, len(reverse_sorted_list)
    while a<b:
        mid = (a+b) // 2
        if reverse_sorted_list[mid] >= number:
            a = mid + 1
        else:
            b = mid
    return a
        
def split_and_int(str_, a=' '):
    list_ = str_.split(a)
    list_[-1] = int(list_[-1])
    return list_

def replace(str_, a=' and ' ,b=' '):
    return str_.replace(a,b)

def solution(info, query):
    list_info = list(map(split_and_int,info))
    list_query = list(map(split_and_int,map(replace,query))) 
    score_dict = ScoreDict(list_info)
    answer = [score_dict.run_query(one_query) for one_query in list_query]
    return answer