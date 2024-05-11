while True:
    N,L,D = map(int, input("").split(" "))
    if (1 <= N,L,D <= 10**4):
        break

d = D/1000


print(d*N)