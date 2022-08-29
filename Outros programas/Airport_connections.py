#Challenge to calculate the minimun connections needed in order to connect every airport

def get_minimum_connections(matrix):
    conexlist = [] #connected list
    unconexlist = [] #unconnected list 
    newconex = 0 #new connections needed
    cc = 0 #column on matrix
    l = matrix[0] # line 0 - connections with a0
    for a in l:
        if cc>0 and a == True:
            conexlist.append(cc)
        if cc>0 and a == False:
            unconexlist.append(cc)
        cc += 1
    
    while len(unconexlist)>0:
        indirect = 0
        for j in unconexlist:
            for i in conexlist:
                m = matrix[j]
                #print (j, i, conexlist, unconexlist) 
                if m[i] == True:
                    indirect = 1
                    conexlist.append(j)
                    #print (j, i, conexlist, unconexlist) 
                    
        if indirect == 0:
            newconex += 1
            conexlist.append(j)
            #print (conexlist, unconexlist)
                    
        for n in conexlist:
            if n in unconexlist:
                unconexlist.remove(n)
                #print (conexlist, unconexlist) 

    return newconex

matrix = \
    [ 
        [False, True, False, False, True, False], 
        [True, False, False, False, False, False], 
        [False, False, False, True, False, False], 
        [False, False, True, False, False, True], 
        [True, False, False, False, False, True],
        [False, False, False, True, True, False]
    ]

print(get_minimum_connections(matrix)) # should print 1
