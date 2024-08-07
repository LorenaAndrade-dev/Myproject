#Digitar nome e cidade, se for rj, além do nome, escrever seja bem vindo, se não, apenas a cidade e nome.

def apresentacao ():
    print(" Meu nome é", nome )
    print( " Minha cidade é", cidade)
def conferir(x):
    if x == "Rio de Janeiro":
        print(" Bem vindo a cidade maravilhosa!")
    else:
        apresentacao
        

    

     
        


nome =str("Digite seu nome:")
cidade = str("Digite a sua cidade:")
conferir (cidade)