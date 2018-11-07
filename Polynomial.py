#Sample Input
'''
1.1 2 3
0
'''
#Sample output
'''
3
'''


def power(x_arg, pow_arg):
    value = 1
    for _ in range(1, pow_arg+1):
        value = value * x_arg
    return value


P = input().split()
x = int(input())
n = P.__len__()
result = 0.0
pow = 0
for i in range(-1, -n-1, -1):

    result = result + float(P[i])*power(x, pow)
    pow += 1
print(result)
