print([x for x in range(10) if x % 2 == 0])

res = []
for x in range(10):
    if x % 2 == 0:
        res.append(x)

print(res)