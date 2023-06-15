S, T = (int(x) for x in input().split())

mapa = [[False for _ in range(S + 1)] for _ in range(S + 1)]

for _ in range(T):
    i, j = (int(x) for x in input().split())
    mapa[i][j] = True
    mapa[j][i] = True

# print(mapa)

P = int(input())
passeios = [[int(x) for x in input().split()] for _ in range(P)]

# print(passeios)

count = 0
for passeio in passeios:
    possivel = True
    atual = passeio[1]
    for salao in passeio[2:]:
        if not mapa[atual][salao]:
            possivel = False
            break

        atual = salao
    
    if possivel:
        count += 1

print(count)
