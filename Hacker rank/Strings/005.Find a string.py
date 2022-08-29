#https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
def count_substring(string, sub_string):
    a = 0
    for i in range (len (string) - len(sub_string) + 1):
        teste = 0
        for n in range (len (sub_string)):
            if string[i+n] == sub_string[n]:
                teste += 1
        if teste == len (sub_string):
            a += 1        
    return a

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
