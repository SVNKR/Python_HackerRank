'''
https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
for item in list:
    for item2 in list2:
        if conditional:
            expression

is equivalent to

            [ expression for item in list for item2 in list2 if conditional ]
*result*  = [*transform*    *iteration*                        *filter*     ]

'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ar = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(ar)
