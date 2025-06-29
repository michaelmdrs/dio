carrinho = []
total = 0.0
n = int(input('Quantidade de produtos: ').strip())

for i in range(n):
    item = input('Digite o nome do produto: ').strip()
    preco = float(input('Digite o preço do produto: ').strip())
    carrinho.append((item, preco))
    total += preco
    # print(f"Subtotal até agora: R$ {total:.2f}")

for item, preco in carrinho:
    print(f"{item}: R$ {preco:.2f}")
print(f"Total: R$ {total:.2f}")
