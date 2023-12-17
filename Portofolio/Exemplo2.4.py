A = 10
ident = id(A)
print(ident)

B = A

ident1 = id(B)
print(ident1)

B = 50 
ident2 = id(B)

print(ident2)

L = [12,24,36]

ident3 = id(L)

print(ident3)

M = L 

ident4 = id(M)

print(ident4)
print(M)