#https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    int_list = map(int, raw_input().split())
    t = tuple(int_list)
    x = hash(t)
    print(x)
