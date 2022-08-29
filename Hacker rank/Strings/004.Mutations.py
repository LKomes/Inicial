def mutate_string(string, position, character):
    s = list(string)
    s[position] = character
    nova = ''.join(s)  
    return nova

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
