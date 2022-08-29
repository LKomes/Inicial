#https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
height, lenght = input().split()
height = int(height)
lenght = int(lenght)
meio = int((height-1)/2)
c = '.|.'

#Top Cone
for i in range(meio):
    print((c*(1+(i*2))).center(lenght,"-"))

#Welcome
print ("WELCOME".center(lenght,"-"))


#Bottom Cone
for i in range(meio):
    print((c*(((meio-i)*2)-1)).center(lenght,"-"))
