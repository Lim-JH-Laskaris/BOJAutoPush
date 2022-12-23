from math import factorial
solution = lambda balls, share : factorial(balls)//(factorial(balls-share)*factorial(share))
