A = "`1234567890-=QWERTYUIOP[]\ASDFGHJKL;ZXCVBNM,./"

while True:
    T = str(input(""))
    if T.isupper():
        break
    else:
        continue

NewT = ''
#NewT += A[position - 1]
for position in range(0, len(T)):
    if T[position] in A and T[position] != 'Q' and T[position] != 'A' and T[position] != 'Z' and T[position] != '`':
        NewT += A[int(A.find(T[position])) - 1]
    elif T[position] == ' ':
        NewT += ' '

print(NewT)