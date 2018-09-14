def find(l,v):
    k=0
    for i in range(0,len(l)):
        if l[i] == v:
            k=i
            return(k)
    if k == 0:
        return("pos not found")

