#Demonstração de OOP
from abc import ABC, abstractmethod

class cliente:
    @abstractmethod
    def __init__(self,titular,conta,saldo):
        self.titular = titular
        self.__conta = conta
        self.__saldo = saldo

    def apresentar(self):
        print("Olá, eu sou a classe-pai!")
        pass

class cliente_fisico(cliente):
    def apresentar (self):
        print("Olá! Eu sou:", self.titular)
        print("Minha conta é:", self.__conta)
        print("E quero saber meu saldo.")
        return
    
#Para criar uma instancia baseada na classe cliente
fulano = cliente_fisico("João", "423.050205-21", 25000.00)

#executando o método vda instancia criada
fulano.apresentar()

#acessando os atributos das instancias criadas
print("De fato, você realmente é:" , fulano.titular)
print("No momento, a sua conta possui R$", fulano.__saldo)

