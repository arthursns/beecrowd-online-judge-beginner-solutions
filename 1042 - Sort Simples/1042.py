x = input().split()

a, b, c = x
a = int(a)
b = int(b)
c = int(c)

if(a > b and a > c):
    o1 = a
    if(b > c):
        o2 = b
        o3 = c
    else:
        o2 = c
        o3 = b
if(b > a and b > c):
    o1 = b
    if(a > c):
        o2 = a
        o3 = c
    else:
        o2 = c
        o3 = a
if(c > a and c > b):
    o1 = c
    if(a > b):
        o2 = a
        o3 = b
    else:
        o2 = b
        o3 = a
print(o3)
print(o2)
print(o1)
print()
print(a)
print(b)
print(c)
