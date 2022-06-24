from rich import *
from rich.progress import track
from time import sleep
import string 
import random
from rich import style
import copy
from rich import print




def banner():

 print(""" [blue]

      ::::::::  ::::    ::: :::::::::: :::::::::: ::::::::: 
    :+:    :+: :+:+:   :+: :+:        :+:             :+:   
   +:+        :+:+:+  +:+ +:+        +:+            +:+     
  +#++:++#++ +#+ +:+ +#+ +#++:++#   +#++:++#      +#+       
        +#+ +#+  +#+#+# +#+        +#+          +#+         
#+#    #+# #+#   #+#+# #+#        #+#         #+#           
########  ###    #### ########## ########## #########       

[/blue]    
""")
 print("""[red] RANDOM PASSWD GENERATOR *[/red]""")


banner()



def process_data():
    sleep(0.01)


for _ in track(range(100), description='[green]Processing '):
    process_data()




alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters_count = list(string.ascii_letters + string.digits + "!@#$%^&*()_")

def generate_random_password():
	global generate_random_password
	length = int(input("Enter password length >> "))
	print()

	print("[#9D00FF]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[/#9D00FF]")


	alphabets_count =int(input("Enter alphabets count in password: ")) 
	print()


	print("[#9D00FF]===============================================================================================[/#9D00FF]")
	digits_count = int(input("Enter digits count in password: "))
	print()


	print("[#9D00FF]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[/#9D00FF]")

	special_characters_count = int(input("Enter special characters count in password: "))

	print()


	print("[#9D00FF]==================================================================================================[/#9D00FF]")

	characters_count = alphabets_count + digits_count + special_characters_count

	if characters_count > length:
		print("Characters total count is greater than the password length")
		return

	password = []
	
	
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))


	for i in range(digits_count):
		password.append(random.choice(digits))


	for i in range(special_characters_count):
		password.append(random.choice(special_characters))

	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))


	random.shuffle(password)
	print("[#F433FF]YOUR GEN PASSWD IS >>>[/#F433FF]")
	print()



	print()
	
	print("[#00FFFF]""".join(password))
	print()


	print("[#6AFB92]#########################################################################################################[/#6AFB92]")

           




generate_random_password()
# print("[green][+][/green] Password generated and copied to clipboard ":check:"")
print("[green][+][/green] [bold magenta]Password generated ![/bold magenta]!", ":white_check_mark:")
print("[#6AFB92]#########################################################################################################[/#6AFB92]")
