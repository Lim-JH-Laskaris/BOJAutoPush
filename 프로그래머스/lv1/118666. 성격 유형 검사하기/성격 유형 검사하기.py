def solution(survey, choices):
    type_dict = {i:0 for i in 'RTCFJMAN'}
    for s,c in zip(survey, choices):
        type_dict[s[0]] += max(4-c,0) 
        type_dict[s[1]] += max(c-4,0) 
    type_list = [max('RTCFJMAN'[2*i],'RTCFJMAN'[2*i+1],key=lambda x:type_dict[x]) for i in range(4)]
    return ''.join(type_list)