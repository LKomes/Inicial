#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
res = arr [0]
sec = -100
for a in range (n):
    if arr[a]>res:
        sec = res
        res = arr[a]
    elif arr[a]>sec and arr[a] != res:
        sec = arr[a]
print sec  
