def transpose(lst):
    newlist = []
    i = 0
    while i < len(lst[0]):
        j = 0
        colvec = []
        while j < len(lst):
            colvec.append(lst[j][i])
            j = j + 1
        newlist.append(colvec)
        i = i + 1
    return newlist
