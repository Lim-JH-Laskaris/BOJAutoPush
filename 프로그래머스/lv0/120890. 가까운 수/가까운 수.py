solution = lambda array, n: min(sorted(array), key=lambda i: abs(i-n))