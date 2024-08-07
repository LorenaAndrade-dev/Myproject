#Coemntários
nome = "Fulano de tal"
print(f"Olá {nome}! Voltamos de férias")
ferias = int(input("Quantos dias ficou de férias?"))
print(f"Ficamos {ferias} dias de férias")

maisferias = int(input(" Quantos dias a mais que de férias?"))
maisferias = maisferias + ferias
print(f"Ok, a partir de agora, terá {maisferias} dias de férias!")


local = input("Qual foi o local que você viajou?")
if local == "Disney":
    print(" Então você levou as crianças!")
elif local == "Paris":
    print("Então foi um passeio romantico")
else:
    print(" Ok, não conheço esse lugar...")


    match local:
        case "Disney":
            print("Perfeito para levar crianças.")
        case "Paris":
            print("Lugar para passeios romanticos")
        case _:
            print("Não reconheço esse lugar")

            
