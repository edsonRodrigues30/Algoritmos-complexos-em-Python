#Importações
from colorama import Fore
import os
#DataBase
dinheiro = int()

#Apresentação
print(Fore.BLUE+"_"*9,"Seja bem vindo","_"*9)
#Interface
def inter():
	print(Fore.WHITE+"""(1)Depositar (2)Consultar (3)Sacar""")
def limpar():
	ok = input("_ ")
	os.system("clear")	
	
	
#Execução
while (1):
	inter()
	main = int(input("Digite:"))
	
	if main == 1:
		limpar()
		saldo = int(input("Digite o valor:"))
		dinheiro += saldo
		print((Fore.GREEN+"Depósito efectuado com sucesso✓"))
		limpar()
		
	elif main == 2:
		print("o seu saldo é de:")
		print(dinheiro,"Kz")
		limpar()
		
	elif main == 3:
		saque=int(input("Digite o valor de saque:"))
		dinheiro -= saque
		if saque>dinheiro:
			print(Fore.RED+"Não tem esse valor disponível na sua conta!")
		limpar()
		
	else:
		print(Fore.RED+"Opção inválida, tente novamente")
		
