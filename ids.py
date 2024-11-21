import random
for _ in range(20):
    id_cliente = "".join(str(random.randint(1,9)) for _ in range(5))
    id_cartao = "".join(str(random.randint(1,9)) for _ in range(10))
    id_chip = "".join(str(random.randint(1,9)) for _ in range(6))
    print(id_cliente, id_cartao, id_chip)

# codigo utilizado para gerar aleatoriamente o id do cliente, do cartao e do chip