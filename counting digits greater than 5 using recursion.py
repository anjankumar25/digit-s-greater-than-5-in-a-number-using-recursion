def aa(a,v=0):
    if a == 0:
        return 0
    e = a%10
    if e > 5:
        v=v+1
    return v + aa(a//10)
print(aa(6789))