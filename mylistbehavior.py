#Demostração de comportamento das listas
print("Vou almocar em um restaurante a quilo!")

original = ["arroz", "feijão", "batata", "alface", "frango"]
print("Eis a minha comida:", original)
derivada = original
print("Meu amigo irá comer também:", derivada)

print("Vou alterar as opções sem ele ver")
original.remove("arroz")
original.remove("feijão")
original.remove("alface")
original.append("picanha")
original.append("linguiça")

print("Me mostre o que vai comer?")
print("Claro! Dá uma conferida", derivada)
