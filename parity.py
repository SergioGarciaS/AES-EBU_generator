a = [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
b = [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def parity (i):
    len = 0

    for j in i:
        if j == 1:
            len +=1

    if  len %2 == 0:
        parity = 1
    else:
        parity = 0

    return parity

print(parity(a))
print(parity(b))
