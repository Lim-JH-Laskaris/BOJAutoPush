def coin_change(price,money=1000,coin_list=[500,100,50,10,5,1]):
    change_coins = 0
    change_money = money-price
    for i in coin_list:
        if change_money==0: break
        change_money, change_coins = change_money%i, change_coins+change_money//i
    return change_coins

print(coin_change(int(input())))
        
       
        
    