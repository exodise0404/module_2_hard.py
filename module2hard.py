def find_pairs(n):
    pairs = []
    for a in range(1, n):
        for b in range(1, n):
            if n % (a + b) == 0:
                pairs.append((a, b))
    return pairs

N = 12
result = find_pairs(N)
print("Подходящие пары чисел:")
for pair in result:
    print(pair)

