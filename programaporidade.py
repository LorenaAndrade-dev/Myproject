#Programa que de acordo com a idade, mostra programas infantis (<18), ou de carros e preços (>18)

idade = int(input("Digite a sua idade:"))

def conferir (x):
    if x <18:
        print("Segue uma lista com programas para sua idade: Hora de aventura, Teen titans go, Padrinhos Mágicos")
    else:
        print( " Segue modelos populares de carro e seus preços: Palio = R$: 340.000 ou Up = 432.000")


conferir (idade)