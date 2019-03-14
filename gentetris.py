for j in range(4):
    for i in range(10):
        print(f'P{i}{j}', end=' ')

print()

# x
# x
# x
# x
for i in range(10):
    print(' '.join(f'P{i}{j}' for j in range(4)))

print()

# xxxx
for j in range(4):
    for i in range(10 - 3):
        print(' '.join(f'P{i+p}{j}' for p in range(4)))
