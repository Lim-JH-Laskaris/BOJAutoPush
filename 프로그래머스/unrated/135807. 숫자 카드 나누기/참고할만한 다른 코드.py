from functools import reduce
from math import gcd

def solution(nums1, nums2):
    gcd1, gcd2 = reduce(gcd, nums1), reduce(gcd, nums2)
    answer = []
    if all(each % gcd2 for each in nums1):
        answer.append(gcd2)
    if all(each % gcd1 for each in nums2):
        answer.append(gcd1)
    return max(answer) if answer else 0
