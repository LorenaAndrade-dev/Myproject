#Demonstração de oop em phyton:
from abc import ABC, abstractmethod

class cliente:
    @abstractmethod
    def __int__(self, titular, conta, saldo):
        self.titular = titular
        self.__conta = conta
        self.__saldo = saldo

    def APRESENTAR(self):
        print("Olá eu seu a classe-pai")
        pass


class clientefisico(cliente):
    def APRESENTAR(self):
        print("Olá! Eu sou:", self.titular)
        print("Minha conta é:", self.__conta)
        print("E quero saber o meu saldo.")
        return
    
#Para criar uma instancia baseada na classe Cliente
fulano = clientefisico("João", "423.050205-21", 25000)

#Executando o método da instancia criada
fulano.APRESENTAR()

#Acessando os atributos das instancias criadas
print("De fato, você realmente é", fulano.titular)
print("No momento, a sua conta possui R$", fulano.__saldo)