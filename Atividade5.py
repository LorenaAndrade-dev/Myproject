#Conversor de temperatura

#Celsius
temp = int(input("Digite a temperatura em Celsius:"))
kelvin = temp + 273
fah = 1,8 * temp + 32
print(f"A conversão de Celsius para Kelvin é:{kelvin}")
print(f"A conversão de Celsius para Fahrenheit é{fah}")

#Kelvin
temp = int(input("Digite a temperatura em Kelvin:"))
celsius = temp - 273
fah = (temp - 273) * 1,8 + 32
print(f"O valor convertido de Kelvin para Celsius é: {celsius}")
print(f"O valor convertido de Kelvin para Fahrenheit é de: {fah}")

#Fahrenheit
temp = int(input("Digite a temperatura em Fahrenheit:"))
celsius = (temp-32)/1,8
kelvin = (temp-32)*5/9+273
print(f"O valor convertido de Fahrenheit para celsius é de : {celsius}")
print(f"O valor convertido de Fahrenheit para Kelvin é de {kelvin}")


# Refinamento do código


print("Qual conversão você deseja fazer?")
escala = int(input("1. Celsius / 2. Kelvin / 3.Fahrenheit" ))
temp= int(input("Digite o valor da temperatura:"))

match escala:
    case 1:
        kelvin = temp + 273
        fah = 1,8 * temp +32
        print(f"O resultado da coversão de Celsius para Kelvin é de {kelvin} e para Fahrenheit é de {fah}")
    case 2:
        celsius = temp -273
        fah =(temp-273) * 1,8 + 32
        print(f"O resultado da conversão de Kelvin para Celsius é de {celsius} e para Fahrenheit é de {fah}")
    case 3:
        celsius = (temp - 32) * 1,8
        kelvin = (temp -32) / 1,8 + 273
        print(f" O resultado da conversão de Fahrenheit para Celsiu é {celsius} e para Kelvin é de {kelvin}")
    case _:
        print("Opção inválida")

