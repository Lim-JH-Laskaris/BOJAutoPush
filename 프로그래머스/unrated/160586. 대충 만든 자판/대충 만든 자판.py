def solution(keymap, targets):
    key_set     = set(list(''.join(keymap))) # 입력 가능 키
    key_dict    = {k:min([i.find(k) for i in keymap if i.find(k)!=-1],
                         default=99)+1 # 입력불가능한 키는 100으로 기록된다. 
                   for k in list(key_set)} #{키:최소입력수}
    answer      = [sum(map(lambda x:key_dict[x], list(t)))
                   if all([x in key_set for x in t]) else -1
                   for t in targets]
    return answer
