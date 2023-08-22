import itertools
import random
from datetime import datetime, timedelta
import sys
import os
from colorama import init
from termcolor import colored
import time

init()


print(colored("Cargando...", 'yellow'))
time.sleep(1)
os.system('clear')


def subdominio():
	while True:
		print(colored("By Cañas", 'green', attrs=["bold"]))
		print(colored("Version - 1", 'green', attrs=["bold"]))
		print(colored("GoBuster-Auto", 'magenta', attrs=["bold"]))
		print(colored("------------------------------------------", "blue"))		
		subdo = input(colored("Sub-Dominio: ", 'green'))
		directorio = input(colored("Directorio: ", 'green'))
		os.system('clear')
		print(colored("Cargando datos...", 'yellow'))
		time.sleep(0.5)
		os.system('gobuster vhost -w ' + directorio + ' -u ' + subdo + ' --append-domain')
		print(colored('''--------------------''', 'yellow'))
		print(colored("[1]", 'magenta'), "Reiniciar")
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[r]", 'magenta'), "Regresar")
		print(colored("------------------------------------------", "blue"))
		opcion = input(colored("Seleccinoa una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			os.system('clear')
			subdominio()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "r":
			os.system('clear')
			menu()


def dominio():
	while True:
		print(colored("	By Cañas", 'green', attrs=["bold"]))
		print(colored("		Version - 1", 'green', attrs=["bold"]))
		print(colored("	GoBuster-Auto", 'magenta', attrs=["bold"]))
		print(colored("------------------------------------------", "blue"))		
		domi = input(colored("Dominio: ", 'green'))
		directorio = input(colored("Directorio: ", 'green'))
		os.system('clear')
		print(colored("Cargando datos...", 'yellow'))
		time.sleep(0.5)
		os.system('gobuster dir --url ' + domi + ' --wordlist ' + directorio)
		print(colored('''--------------------''', 'yellow'))
		print(colored("[1]", 'magenta'), "Reiniciar")
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[r]", 'magenta'), "Regresar")
		print(colored("------------------------------------------", "blue"))
		opcion = input(colored("Seleccinoa una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			os.system('clear')
			dominio()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "r":
			os.system('clear')
			menu()


def menu():
	while True:
		print(colored('''
  ____       ____          _    
 / ___| ___ | __ )        / \   
| |  _ / _ \|  _ \ _____ / _ \  
| |_| | (_) | |_) |_____/ ___ \ 
 \____|\___/|____/     /_/   \_\

''', 'cyan', attrs=["bold"]))
		print(colored("			By Cañas", 'green', attrs=["bold"]))
		print(colored("				Version - 1", 'green', attrs=["bold"]))
		print(colored("GoBuster-Auto", 'magenta', attrs=["bold"]))
		print(colored("------------------------------------------", "blue"))
		print(colored("[1]", 'yellow'), "Dominios")
		print(colored("[2]", 'yellow'), "SubDominios")
		print(colored('''--------------------''', 'yellow'))
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[0]", 'magenta'), "Salir")
		print(colored("------------------------------------------", "blue"))
		opcion = input(colored("Seleccinoa una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			os.system('clear')
			dominio()
		elif opcion == "2":
			os.system('clear')
			subdominio()
		elif opcion == "0":
			os.system('clear')
			print(colored("Saliendo...", 'yellow'))
			time.sleep(0.5)
			os.system('clear')
			sys.exit()
		else:
			os.system('clear')
			print(colored("Opción invalida...", 'red'))
			time.sleep(1.2)
			os.system('clear')
			menu()
			




if __name__ == '__main__':
    menu()
