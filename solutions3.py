while True:
    A,B,C = map(int, input("").split(" "))
    if (A >= 1 and A <= 100) and (B >= 1 and B <= 100) and (C >= 1 and C <= 100):
        break

ovo = B//3
leite = A//2
farinha = C//5

L = [ovo, leite, farinha]

print(min(L))



