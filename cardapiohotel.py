cafe = []
almoco =[]
jantar = []

print("Criando seu cardápio peronalizado")

print("Qual opção você deseja para o café da manhã?")
for x in range (0,3):
    cafe.append(input(f"Escolha o {x+1}º opção:"))
    if cafe[x] == "queijo" or cafe [x] == "leite":
        print(" Esse alimento não é recomendado para pessoas com intolerancia a lactose")
print("As opções escolhidas foram: ",cafe)

print("Qual opção você deseja para Almoço?")
for x in range (0,4):
    almoco.append(input(f"Escolha o {x+1}º opção:"))
    if almoco [x] == "Camarão" or almoco [x] == "Lagosta":
        print(" Esse alimento não é recomendado para pessoas com alergia a frutos do mar")
print("As opções escolhidas foram: ", almoco)

print("Qual opção você deseja de Jantar?")
for x in range(0,4):
    jantar.append(input(f"Escolha a {x+1}º opção:"))
    if jantar [x] == "Camarão" or jantar [x] == "Lagosta":
        print(" Esse alimento não é recomendado para pessoas com alergia a frutos do mar")
print("As opções escolhidas foram: ", jantar)


    
  
     
    