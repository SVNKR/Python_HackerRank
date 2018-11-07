from collections import Counter

if __name__ == '__main__':
    n = int(input())
    shoeCounter = Counter(map(int, input().split()))
    noOfCustomers = int(input())
    shoesReqdByCustomers = []
    for _ in range(noOfCustomers):
        shoesReqdByCustomers += list(map(int, input().split()))

    print(shoesReqdByCustomers)
