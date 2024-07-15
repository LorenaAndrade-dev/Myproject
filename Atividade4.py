# exercicio 1, soma de números
#2  quadrado de um número
#3 quatro operações básicas
#4 quantos anos em 2040
#5 cubo do valor

#Exercício 1
x = int(input("Digite o valor 1: "))
y = int(input("Digite o valor 2: "))
soma = x + y
print(f" A soma é de:{soma}")

#Exercicio 2
x = int(input("Digite o número aqui:"))
quadrado = x**2
print( f" O quadrado do número é:{quadrado}")

#Exercicio 3
x = int(input("Digite o valor 1: "))
y = int(input("Digite o valor 2: "))
soma = x + y
subtracao = x - y
multi = x * y
divi = x / y
print(f" O resultado da soma é {soma}")
print(f"O resultado da subtração é {subtracao}")
print(f"O resultado da multiplicação é {multi}")
print (f"O resultado da divisão é:{divi}")

#Exercicio 4
ano = int(input(" Digite o ano em que você nasceu:"))
idade = 2040 - ano
print(f" Você terá {idade} em 2040!")

#Exercicio 5
x = int(input("Digite o valor aqui:"))
cubo = x**3
print(f"O cubo é: {cubo}")
        