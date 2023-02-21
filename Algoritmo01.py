from colorama import Fore
import os

def inter():
	print(Fore.WHITE+"(1)Pagina inicial (2)Postar (3)Eliminar")
	
def limpar():
	ok = input("_ ")
	os.system("clear")
	
def bordas():
	print("="*60)

b = int(0)
posts = []	

while(1):
	inter()
	main = int(input("_"))

	if main == 1:
		limpar()	
		for i in range(b):
			bordas()
			print(posts[i],"\nID:",i)
			bordas()
		limpar()
		
	elif main == 2:
		limpar()
		a = str(input("Digite:"))
		list(a)
		posts.append(a)
		b += 1
		limpar()
	elif main == 3:
		limpar()
		rem = int(input("Digite o ID:"))
		del(posts[rem])
		b -=1
		print(Fore.GREEN+"Post ",rem,"  eliminado!")
		limpar()