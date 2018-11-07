# Sample input
'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
'''
#Sample output
'''
Berry
Harry
'''

if __name__ == '__main__':
    parentList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        childList = []
        childList.append(name)
        childList.append(score)
        parentList.append(childList)

    resultList = []
    first = 101
    second = 101
    for student in parentList:
        if student[1] < first:
            second = first
            first = student[1]
        elif second > student[1] > first:
            second = student[1]
    for student in parentList:
        if second == student[1]:
            resultList.append(student[0])

    resultList.sort()
    print(*resultList, sep='\n')


