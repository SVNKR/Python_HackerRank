'''
https://www.hackerrank.com/challenges/find-a-string/problem
I/P:
ABCDCDC
CDC

O/P:
2

Alt soln: print(sum([1 for i in range(len(string) - len(sub_string) + 1) if string[i:i + len(sub_string)] == sub_string]))
'''


def count_substring(string, sub_string):
    len_to_traverse = len(string) - len(sub_string)
    count = 0
    i = 0
    while i < len_to_traverse+1:
        index = string.find(sub_string, i)
        if index > -1:
            count += 1
            i = index
        i += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
