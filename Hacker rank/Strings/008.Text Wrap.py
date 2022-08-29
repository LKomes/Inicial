#https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
import textwrap

def wrap(string, max_width):
    saida = textwrap.wrap(string,max_width)
    saida = "\n".join(saida)
    return saida

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
