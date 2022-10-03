X = int(input())
N = 0

while 2 ** N <= X:
    N += 1

N -= 1

print(N, 2 ** N)
