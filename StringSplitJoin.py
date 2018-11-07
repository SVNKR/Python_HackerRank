'''https://www.hackerrank.com/challenges/python-string-split-and-join/problem?h_r=next-challenge&h_v=zen'''

if __name__ == '__main__':
    strInput = input()
    strInput = strInput.split(" ")
    strInput = "-".join(strInput)
    print(strInput)
