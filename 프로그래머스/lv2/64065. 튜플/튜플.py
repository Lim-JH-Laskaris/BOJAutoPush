def set_list_parser(string):
    string_list = string[2:-2].split('},{')
    set_list = [set(map(int,i.split(','))) for i in string_list]
    set_list.sort(key=len)
    return set_list

def solution(s):
    set_list = set_list_parser(s)
    n_tuple = []
    e1 = set()
    while set_list :
        e2 = set_list.pop(0)
        n_tuple.append((e2-e1).pop())
        e1 = e2
    return n_tuple