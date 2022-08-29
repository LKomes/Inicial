#https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

lista = ""
for a in range (n):
    b = str(a+1)
    lista = lista+b
print (lista)
