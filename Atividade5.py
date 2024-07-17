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

