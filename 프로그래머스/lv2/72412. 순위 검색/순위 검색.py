
import itertools

class ScoreDict(dict):
    def __init__(self, list_info):
        self.search_space = [
            ['cpp', 'java', 'python'],  
            ['backend', 'frontend'],
            ['junior', 'senior'],
            ['chicken', 'pizza'],
        ]
        for i in itertools.product(*self.search_space):
            self['_'.join(i)] = []
        for i in range(len(list_info)):
            a, b, c, d, e = list_info[i]
            self[f'{a}_{b}_{c}_{d}'].append(e)
        for i in itertools.product(*self.search_space):
            self['_'.join(i)].sort(reverse=True)
        
    def run_query(self, one_query):
        search_space = [[one_query[i]] if one_query[i]!='-' else self.search_space[i] for i in range(4)]
        search_space = ['_'.join(i) for i in itertools.product(*search_space)]
        sum_ = 0
        for i in search_space:
            sum_ += binary_compare_count(self[i], one_query[4])         
        return sum_

def binary_compare_count(reverse_sorted_list, number):
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
    
    answer = []
    for one_query in list_query:
        answer.append(score_dict.run_query(one_query))
    return answer