matriz = []
for x in range (0, 2):
    for y in range(0,2):
        matriz [x][y]= int(input(f"Digite o primeiro número:{x+1}"),
                                 (f"e o segundo número:{y+1}:"))

for x in range (0, 2):
    for y in range (0,2):
     soma = matriz[x][y] + matriz [x][y]
    
    
print(soma)
media = soma / 4
print(media)
