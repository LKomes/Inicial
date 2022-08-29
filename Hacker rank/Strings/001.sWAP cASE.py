def swap_case(s):
    saida=''
    for i in s:
        if i.isupper():
            saida += i.lower()
        elif i.islower():
            saida += i.upper()
        else:
            saida += i

    return saida

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
