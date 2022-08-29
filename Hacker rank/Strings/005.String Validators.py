if __name__ == '__main__':
    s = raw_input()
    lista = list(s)
    num = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for i in range (len(s)):
        if lista[i].isalnum():
            num = True
        if lista[i].isalpha():
            alpha = True
        if lista[i].isdigit():
            digit = True
        if lista[i].islower():
            lower = True
        if lista[i].isupper():
            upper = True
    print num
    print alpha
    print digit
    print lower
    print upper
            
