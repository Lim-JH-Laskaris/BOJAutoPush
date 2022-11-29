def solution(order):
    order = str(order)
    return sum([order.count(str(i)) for i in [3,6,9]])