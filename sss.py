def addpoly(p1, p2):

    for i in range(len(p1)):
        for item in p2:
            if p1[i][1] == item[1]:
                p1[i] = ((p1[i][0] + item[0]), p1[i][1])
                p2.remove(item)
    p3 = p1 + p2
    for item in (p3):
        if item[0] == 0:
            p3.remove(item)
    return sorted(p3)

def multpoly(p1, p2):
        for i in range(len(p1)):
            for item in p2:
                p1[i] = ((p1[i][0] * item[0]), (p1[i][1] + item[1]))
                p2.remove(item)
        return p1

