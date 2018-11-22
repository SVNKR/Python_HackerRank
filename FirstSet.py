'''
https://www.hackerrank.com/challenges/symmetric-difference/problem
^ symbol can also be used to compute the symmetric difference of two sets.
# Enter your code here. Read input from STDIN. Print output to STDOU
M = raw_input();m = raw_input().split()
N = raw_input();n = raw_input().split()

print "\n".join(sorted(list(set(m) ^ set(n)),key=int))
'''


a,b = [set(input().split()) for _ in range(4)][1::2]
print(*sorted(a^b, key=int), sep='\n')
