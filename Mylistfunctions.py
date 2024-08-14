#Demostração de funções em listas
numeros = [7, 2, 6, 5, 0, 3, 8, 1, 4]
palavras = ["olá", "alô", "Hey", "uau", "ops"]

print("Quantas variáveis possui:")
print("Números:", len(numeros))
print("Palavras:", len(palavras))

print("Vamos reordenar as listas")
print(sorted(numeros))
print(sorted(palavras))

print("O somatório de números:", sum(numeros))
print("Qual é o maior valor?", max(numeros))
print("Qual a  primeira palavra?", min(palavras))