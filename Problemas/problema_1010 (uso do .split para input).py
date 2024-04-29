a, qnt_a, valor_a = input().split()
b, qnt_b, valor_b = input().split()

a = int(a)
qnt_a = int(qnt_a)
valor_a = float(valor_a)
b = int(b)
qnt_b = int(qnt_b)
valor_b = float(valor_b)

total = qnt_a * valor_a + qnt_b * valor_b
print(f'VALOR A PAGAR: R$ {total:.2f}')