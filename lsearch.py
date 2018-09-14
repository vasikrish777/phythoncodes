def lsearch(l,s):
    for i in range(len(l)):
        if l[i] == s:
            return ("the value is found",i)
    return("value not found") 
