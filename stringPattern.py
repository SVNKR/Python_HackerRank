'''
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
I/P
5

O/P
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''



def print_rangoli(size):
    # your code goes here
    final_string = ''
    char_val = 0
    val = 0
    if size == 1:
        final_string = 'a'
        return final_string

    for i in range(1, size):
        val = (size - i)*2 - 1
        string = ''
        char_val = 0
        for j in range(0, i):
            char_val = 97+size - 1 - j
            string += '-' + chr(char_val)
        string += '-'
        for j in range(1, i):
            char_val = char_val + 1
            string += chr(char_val) + '-'
        final_string += ''.rjust(val, '-') + string + ''.ljust(val, '-') + '\n'

    string = ''
    for i in range(0, size):
        string += chr(char_val) + '-'
        char_val -= 1

    char_val += 1
    string = string[:len(string) - 1]
    for i in range(1, size):
        char_val += 1
        string += '-' + chr(char_val)

    final_string += string + '\n'

    val += 1
    for i in range(1, size):
        value = len(string)//2 - 1
        string = string[:value] + string[value+4:]
        final_string += ''.rjust(val, '-') + string + ''.ljust(val, '-') + '\n'
        val += 2

    return final_string

if __name__ == '__main__':
    n = int(input())
    print(print_rangoli(n))