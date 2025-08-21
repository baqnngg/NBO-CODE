def dim(n,m):
    st = ''
    num = n
    while num != 0:
        st = str(num % m) + st
        num //= m
    print(st)

a = int(input())
for i in [2,3,4]: dim(a, i)