'''I/p
abcde
2 k

o/p
abkde
'''

if __name__ == 'main':
    s = input()
    i, c = input.split()
    '''Process 1 to mutate'''
    sToL = list(s)
    sToL[i] = c
    mutatedStr1 = ''.join(sToL)

    '''Process 2 to mutate'''
    mutatedStr2 = s[:i] + c + s[i+1:]
