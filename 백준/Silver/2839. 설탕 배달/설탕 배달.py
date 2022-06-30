def count_bag(kg , kg_per_3):
    kg_per_5 = kg - kg_per_3
    if kg in [1,2,4,7]: return -1
    if kg_per_5%5==0 and kg_per_3%3==0 : return kg_per_5//5 + kg_per_3//3
    else : return count_bag(kg , kg_per_3+1)

kg = int(input())
print(count_bag(kg, 0))

    