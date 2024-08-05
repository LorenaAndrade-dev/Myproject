#Construir um programa que pergunte o melhor clube, enquanto não for respondido corretamente, fazer advertencias
#apos acertar, parabenizar

time = ""
while time != "Paissandu":
    print("Digite o melhor time do Brasil:")
    time = input()

    if time == "Paissandu":
        print("Está correto, parabéns!")
    else:
        print("Tente novamente")
        break

