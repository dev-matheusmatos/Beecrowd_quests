a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

print(f'''TRIANGULO: {(a * c) / 2:.3f}
CIRCULO: {3.14159 * c ** 2:.3f}
TRAPEZIO: {((a + b) * c) / 2:.3f}
QUADRADO: {b ** 2:.3f}
RETANGULO: {a * b:.3f}''')


