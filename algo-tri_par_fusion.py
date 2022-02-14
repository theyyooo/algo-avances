def tri(t):
    n=len(t)
    if n<2:
        return t
    else:
        m=n//2
        return fusion(tri(t[:m]),tri(t[m:]))

def fusion(t1,t2):
    i1,i2,n1,n2=0,0,len(t1),len(t2)
    t=[]
    while i1<n1 and i2<n2:
        if t1[i1]<t2[i2]:
            t.append(t1[i1])
            i1+=1
        else:
            t.append(t2[i2])
            i2+=1
    if i1==n1:
        t.extend(t2[i2:])
    else:
        t.extend(t1[i1:])
    return t