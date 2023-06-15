M, N = (int(x) for x in input().split())

estoque = [[int(x) for x in input().split()] for _ in range(M)]

P = int(input())
pedidos = ((int(x) for x in input().split()) for _ in range(P))

count = 0
for i, j in pedidos:
    if estoque[i - 1][j - 1] > 0:
        count += 1
        estoque[i - 1][j - 1] -= 1

print(count)
