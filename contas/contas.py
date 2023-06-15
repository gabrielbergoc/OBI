dinheiro = int(input())
contas = [int(input()) for _ in range(3)]

contas.sort()

count = 0
for conta in contas:
    if dinheiro >= conta:
        count += 1
    
    dinheiro -= conta
    
print(count)
