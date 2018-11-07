if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    first = -101
    second = -101

    for i in range(n):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif first > arr[i] > second:
            second = arr[i]

    second = first if second == -101 else second
    print(second)



