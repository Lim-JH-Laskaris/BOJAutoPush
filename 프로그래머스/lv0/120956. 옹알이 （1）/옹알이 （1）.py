def is_ongalyi(str_):
    ongalyi2 = ["ye", "ma"]
    ongalyi3 = ["aya", "woo"]
    if   len(str_) == 0 : 
        return 1
    elif len(str_) == 1 : 
        return 0
    elif str_[:2] in ongalyi2 : 
        return is_ongalyi(str_[2:])
    elif len(str_)>=3 and str_[:3] in ongalyi3 : 
        return is_ongalyi(str_[3:])
    else : 
        return 0 

def solution(babbling):
    ongalyi_list = [is_ongalyi(i) for i in babbling]
    return sum(ongalyi_list)