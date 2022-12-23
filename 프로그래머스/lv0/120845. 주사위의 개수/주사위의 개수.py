from math import prod
solution = lambda box, n : prod(map(lambda x: x//n, box))