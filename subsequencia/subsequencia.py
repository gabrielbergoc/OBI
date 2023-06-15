A, B = (int(x) for x in input().split())

seqA = [int(x) for x in input().split()]
seqB = [int(x) for x in input().split()]

i = 0   # iterar seqA
j = 0   # iterar seqB
while i < A and j < B:
    if seqA[i] == seqB[j]:
        j += 1
    i += 1

print("S" if j == B else "N")
