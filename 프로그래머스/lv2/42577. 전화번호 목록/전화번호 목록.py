def solution(phone_book):
    phone_book = sorted(phone_book, key=len,reverse=True)
    prefix = {}
    while phone_book :
        pop = phone_book.pop()
        for i in range(len(pop)):
            try : prefix[pop[:i+1]]
            except : pass
            else : return False
        prefix[pop] = True
    return True


"""속도는 개선되었으나 효율성 1,2,4 통과 못함"""
"""딕셔너리를 상속한 재미있는 클래스를 만들었는데, 통과 못해서 매우 아쉽다..."""
# class HashChain(dict):
#     """딕셔너리를 상속하는 클래스로, hash_chain['129']를 호출하면 hash_chain['1']['2']['9']가 호출된다.
#     이때 해당 대상이 존재하지 않으면, 존재하지 않은 모든 경로를 새롭게 만들고 hash_chain['1']['2']['9']에는 
#     HashChain의 빈 인스턴스를 할당한뒤, 이를 반환한다. 
#     """
#     def __getitem__(self, key):
#         if len(key)==1 : return super().__getitem__(key)
#         else : return self[key[0]][key[1:]]
            
#     def __missing__(self, key):
#         sub_hash_chain = HashChain()
#         if len(key)==1 : self[key] = sub_hash_chain
#         else : self[key[0]] = sub_hash_chain[key[1:]]        
#         return self[key]

# def solution(phone_book):
#     """phone_book을 길이순으로 정렬후, 긴 번호 부터 hash_chain로 호출한다.
#     중복되는 번호가 없으므로, 이후 호출된 짧은 번호가 최종적으로 새로운 경로를 만들지 않는다면,
#     (다시말해 빈 HashChain 인스턴스를 반환하지 않는다면) 이는 해당 번호가 무언가의 접두어라는 뜻이므로,
#     False를 최종적으로 반환한다. 만약 모든 번호를 호출했다면, 접두어 관계의 번호가 없다는 뜻이므로,
#     True를 반환한다.
#     """
#     phone_book = sorted(phone_book, key=len)
#     hash_chain = HashChain()
#     while phone_book:
#         if hash_chain[phone_book.pop()] :
#             return False
#     return True
        
    
    
    

"""아래 코드는 효율성 테스트를 통과하지 못함."""
"""첫 시도"""
# def match_prefix(num_str,longer_strs):
#     """특정문자와, 그보다 긴 문자열들을 원소로 같는 리스트에서, 특정문자를 포함하는 경우가 있는지를 찾는 재귀함수
    
#     Args : 
#         num_str (str) : 접두어 여부를 검색하고자 하는 문자열
#         longer_strs (list(str)) : num_str를 접두어로 포함하고 있는지를 검색하기 위한 후보 문자열들의 배열.
#                                   모든 문자열은 num_str보다 길이가 길거나 같다.
    
#     return :
#         True / False / match_prefix() :
#             longer_strs 원소 중 num_str의 첫글자를 접두어로 갖는 원소가 있다면, 그 첫글자를 떼고 새로운 배열인
#             longer_strs_matched_with_first_chr에 포함시킨다. 이 배열이 비어있으면 True 반환, 그렇지 않다면
#             num_str의 다음 글자들을 확인하기 위해 match_prefix를 재귀적으로 반환
#             만약 num_str가 ''이면 더이상 확인할 글자가 남지 않았다는 뜻이므로 False 반환
#     """
#     if len(num_str)==0 : return False
#     first_chr = num_str[0]
#     longer_strs_matched_with_first_chr = [i[1:] for i in longer_strs if first_chr == i[0]] 
#     if len(longer_strs_matched_with_first_chr) == 0 : return True
#     else : return match_prefix(num_str[1:],longer_strs_matched_with_first_chr)
    

# def solution(phone_book):
#     phone_book = sorted(phone_book, key=len,reverse=True)
#     while len(phone_book)>0 : 
#         num_str = phone_book.pop()
#         if match_prefix(num_str,phone_book) == False : return False
#     return True