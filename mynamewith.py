#Demostração do uso do for/range

print("Digite o valor máximo desejado:")
numero = int(input())
print("Segue os números desejados:")
for x in range (0, numero):
    print(x)



print(" Digite o nome desejado:")
nome = input()
print("Vamos soletrar cada letra?")
for x in nome:
    print(x)



print("Digite o valor máximo desejado:")
numero = int(input())
x = 0
print("Segue os números desejados:")
while x < numero:
    print(x)
    x = x + 1