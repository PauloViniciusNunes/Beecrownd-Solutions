T = int(input(""))
lf = []
rf = []
for i in range(1, T + 1):

    #verificação do N
    while True:
        N = int(input(""))
        if N >= 0 and N <= 60:
            lf.append(N)
            break
        else:
            continue
    
    R = (((1 + 5**0.5)/2)**N - ((1 - 5**0.5)/2)**N)/(5**0.5)
    rf.append(R)


for item in range(0, len(lf)):
    print(f"Fib({lf[item]}) = {int(rf[item])}")


# 0
# (((1 + R(5))/2)**N - ((1 - R(5))/2)**N)/R(5)


