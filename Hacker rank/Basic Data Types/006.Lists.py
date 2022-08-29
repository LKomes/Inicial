if __name__ == '__main__':
    N = int(input())
    lista = []
    for i in range(N):
        tmp = list(raw_input().split())
        if(tmp[0]== 'insert'):
            lista.insert(int(tmp[1]), int(tmp[2]))
        elif( tmp[0]== 'print'):
            print(lista)
        elif( tmp[0] == 'remove'):
            lista.remove(int(tmp[1]))
        elif( tmp[0] == 'append'):
            lista.append(int(tmp[1]))
        elif( tmp[0] == 'sort'):
            lista.sort()
        elif( tmp[0] == 'pop'):
            lista.pop()
        elif( tmp[0] ==  'reverse'):
            lista.reverse()
