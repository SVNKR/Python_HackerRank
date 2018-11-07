'''https://www.hackerrank.com/challenges/python-lists/problem'''

if __name__ == '__main__':
    N = int(input())
    operationList = []

    def insert(pos, value):
        operationList.insert(int(pos), int(value))

    def remove(val):
        operationList.remove(int(val))

    def append(val):
        operationList.append(int(val))

    switcher = {
        'insert': insert,
        'print': lambda: print(operationList),
        'remove': remove,
        'append': append,
        'sort': lambda: operationList.sort(),
        'pop': lambda:  operationList.pop() if len(operationList) > 0 else len(operationList),
        'reverse': lambda: operationList.reverse()
    }

    for _ in range(N):
        inputArray = input().split()
        func = switcher.get(inputArray[0])
        del inputArray[0]
        func(*inputArray)

