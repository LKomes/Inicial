#https://www.hackerrank.com/contests/pythonist/challenges/validating-the-phone-number
import re
if __name__=="__main__":
    s = int(raw_input()) 
for i in range (s):
    numero_test = raw_input()
    teste = re.findall(r"[\D]",numero_test)
    if teste != []:
        print ("NO")
    else:
        if len(numero_test) == 10:
            if (numero_test[0]) in ["7", "8", "9"]:
                print ("YES")
            else:
                print ("NO")
        else:
            print ("NO")
