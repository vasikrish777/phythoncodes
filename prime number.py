def prime(k):
    t=[]
    for i in range(1,k):
        if k%i == 0:
            t.append(i)
    if t[-1] == 1:
        print(k,": is a prime number")
    else:
        print(k,": is not a prime number")
