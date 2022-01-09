def insertion (lin):
    for i in range (1,len(lin)):
        while lin[i-1] > lin[i] and i>0:
            lin[i], lin[i-1] = lin[i-1], lin[i]
            i-=1
    return lin
print (insertion([1,2,3,4,5,6,0,9,8,7,6,5,4,3,2,1]))