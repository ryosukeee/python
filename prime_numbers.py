MAX = 10001
p = list(range(2,MAX))
q = list(range(2,MAX))

for i in p:
    for j in range(2, i):
        if (i%j == 0) and (i in q):
            q.remove(i)
            break

print(q)
