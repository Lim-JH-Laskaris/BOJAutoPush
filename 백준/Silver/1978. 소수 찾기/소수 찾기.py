def make_prime_number_list():
    number_list = list(range(2,1001))
    prime_number_list = []
    while number_list:
        n = number_list.pop(0)
        number_list = list(set(number_list) - set(range(n,1001,n)))
        number_list.sort()
        prime_number_list.append(n)
    return prime_number_list

def count_prime_numbers(number_list):
    return len(set(number_list)&set(make_prime_number_list()))

def main():
    m = int(input())
    number_list = list(map(int, input().split()))
    print(count_prime_numbers(number_list))

main()