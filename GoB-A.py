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
		print(colored("Version - 1.2", 'green', attrs=["bold"]))
		print(colored("GoBuster-Auto", 'magenta', attrs=["bold"]))
		print(colored("------------------------------------------", "blue"))	
		print(colored("[m]", 'yellow'), "Menú")
		print(" ")			
		subdo = input(colored("Dominio: ", 'green'))

		if subdo == "m":
			os.system('clear')
			menu()

		directorio = "banco/DNS/subdomains-top1million-5000.txt"
		print("Directorio:", directorio)
		time.sleep(1)
		print(colored("Cargando datos...", 'yellow'))
		time.sleep(0.5)
		os.system('gobuster vhost -w ' + directorio + ' -u ' + subdo + ' --append-domain')
		print(colored('''--------------------''', 'yellow'))
		print(colored("[r]", 'magenta'), "Reiniciar")
		print(colored("[m]", 'magenta'), "Menú")
		print(colored("------------------------------------------", "blue"))
		opcion = input(colored("Seleccinoa una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "r":
			os.system('clear')
			subdominio()
		elif opcion == "m":
			os.system('clear')
			menu()


def dominio():
	while True:
		print(colored("	By Cañas", 'green', attrs=["bold"]))
		print(colored("		Version - 1.2", 'green', attrs=["bold"]))
		print(colored("	GoBuster-Auto", 'magenta', attrs=["bold"]))
		print(colored("------------------------------------------", "blue"))
		print(colored("[m]", 'yellow'), "Menú")
		print(" ")		
		domi = input(colored("Dominio: ", 'green'))

		if domi == "m":
			os.system('clear')
			menu()

		directorio = "banco/dirbuster/directory-list-2.3-small.txt"
		print("Directorio:", directorio)
		time.sleep(1)
		print(colored("Cargando datos...", 'yellow'))
		time.sleep(0.5)
		os.system('gobuster dir --url ' + domi + ' --wordlist ' + directorio)
		print(colored('''--------------------''', 'yellow'))
		print(colored("[r]", 'magenta'), "Reiniciar")
		print(colored("[m]", 'magenta'), "Menú")
		print(colored("------------------------------------------", "blue"))
		opcion = input(colored("Seleccinoa una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "r":
			os.system('clear')
			dominio()
		elif opcion == "m":
			os.system('clear')
			menu()

def dirsearchF():
	while True:
		print(colored("	By Cañas", 'green', attrs=["bold"]))
		print(colored("		Version - 1.2", 'green', attrs=["bold"]))
		print(colored("Ejemplo: http://google.com"))
		print(colored("------------------------------------------", "blue"))
		print(colored("[m]", 'yellow'), "Menú")
		print(" ")
		dominio = input(colored("Objetivo: ", 'green'))

		if dominio == "m":
			os.system('clear')
			menu()

		time.sleep(1)
		print(colored("Cargando datos...", 'yellow'))
		time.sleep(0.5)
		os.system('clear')
		print(colored("------------------------------------------", "blue"))
		os.system('dirsearch -u ' + dominio)
		print(colored("------------------------------------------", "blue"))
		print(colored("------------------------------------------", "blue"))
		print(colored("[m]", 'yellow'), "Menú")
		print(" ")

		opcion = input(colored("Seleccinoa una opción: ", 'green'))

		if opcion =="m":
			os.system('clear')
			menu()
		else:
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
		print(colored("				Version - 1.2", 'green', attrs=["bold"]))
		print(colored("GoBuster-Auto", 'magenta', attrs=["bold"]))
		print(colored("------------------------------------------", "blue"))
		print(colored("[1]", 'yellow'), "Dominios")
		print(colored("[2]", 'yellow'), "SubDominios")
		print(colored("[3]", 'yellow'), "Dirsearch")
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
		elif opcion == "3":
			os.system('clear')
			dirsearchF()
		elif opcion == "c":
			os.system('clear')
			menu()
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
