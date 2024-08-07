#Construa um programa onde um usuário digitará um valor e o programa mostará na tela, a tabuada de multiplicação desse números. 
#Se possivel,promova uma impressão que possibilite visualizar da melhor maneira possivel.

numero = int(input("Digite um número para verificar a tabuada:"))
for i in range (1, 11):
    resultado = numero * i
    print(resultado)


