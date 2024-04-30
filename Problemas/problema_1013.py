a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

maior = (a + b + abs(a - b)) / 2

if c > maior:
    maior = c

print(f'{int(maior)} eh o maior')