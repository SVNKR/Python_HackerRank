'''
https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
Set Operations
'''



n = int(input())
s = set(map(int, input().split()))
no_of_commands = int(input())

def removeSet(arg):
    s.remove(arg)

def discardSet(arg):
    s.discard(arg)

def popSet(arg):
    s.pop()

def processInput():
    list_obj = input().split()
    command = list_obj[0]
    entry = list_obj[1] if len(list_obj) > 1 else None
    switchObj.get(command)(int(0 if entry is None else entry))

switchObj = {
    'remove' : removeSet,
    'discard' : discardSet,
    'pop' : popSet
}

for _ in range(no_of_commands):
    processInput()

print(sum(s))



