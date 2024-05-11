while True:
    M = int(input(""))
    A = int(input(""))
    B = int(input(""))

    if (M >= 40 and M <= 110) and (A >= 1 and A < M) and (B >= 1 and B < M) and (A != B):
        break

C = M - (A+B)

l = [A, B ,C]

print(max(l))