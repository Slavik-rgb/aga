p = int(input())
q = int(input())

n = p * q
u = (p - 1) * (q - 1)

lst = []
k = 0
for i in range(2, u + 1):
    for j in range(2, i + 1):
        if i % j == 0 and i != j:
            k += 1
    if k == 0:
        lst.append(i)
    else:
        k = 0
print(lst)
vz = []
for c in range(2, u):
    if u % c == 0:
         if c in lst:
             vz.append(c)
res = []
for f in lst:
    if f not in vz:
        res.append(f)
print(res)
e = res[0]
d = 0
q = 0
while q == 0:
    d += 1
    if d != e and (d * e) % u == 1:
        q = 1
print("n = ", n, " e = ", e, " d = ", d)

s = int(input())
a = s ** e % n
b = a ** d % n

print('itog = ', b)
