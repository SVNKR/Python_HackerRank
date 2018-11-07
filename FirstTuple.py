'''
Sample Input
2
1 2

Sample output
Hash of tuple(1,2) = 3713081631934410656
'''

if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    integer_tuple = tuple(integer_list)
    print(hash(integer_tuple))
    print(integer_list)
