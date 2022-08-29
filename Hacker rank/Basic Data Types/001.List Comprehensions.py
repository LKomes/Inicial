#https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
ite = []
for i in range (x+1):
    for j in range (y+1):
        for k in range (z+1):
            if (i+j+k!=n):
                ite = ite +[[i,j,k]]
print ite
