solution = lambda price: int(price*0.80) if price>=5*10**5 else (
    int(price*0.90) if price>=3*10**5 else(
    int(price*0.95) if price>=1*10**5 else price)) 