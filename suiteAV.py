# -*- coding: utf-8 -*-

import os, sys, subprocess
import os.path
from colorama import Fore, Back, Style, init
import urllib.request, urllib.parse, urllib.error
import signal
import time
import gettext
import requests
import re
import ctypes

# Ottieni l'handle della console
kernel32 = ctypes.windll.kernel32
hWnd = kernel32.GetConsoleWindow()

# Importa user32.dll
user32 = ctypes.windll.user32

# Definisci le dimensioni desiderate (larghezza, altezza)
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=80))

translations = gettext.translation("main", localedir="locales", languages=["it"])
translations.install()


init(autoreset=True)


#sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=80))


subprocess.call("cls", shell=True)

url = "https://raw.githubusercontent.com/alexis-82/varius/master/check"

# Effettua una richiesta GET per ottenere il contenuto della pagina HTML
response = requests.get(url)

if response.status_code == 200:
    # Salva il contenuto del file in un file locale
    with open("check", "wb") as file:
        file.write(response.content)

check = os.path.exists("check")

url = "https://github.com/yt-dlp/yt-dlp/tags"

# Effettua una richiesta GET per ottenere il contenuto della pagina HTML
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    # Scrivi il contenuto HTML su un file di testo
    with open("tags", "w", encoding="utf-8") as file:
        file.write(html_content)

# Leggi il contenuto dal file "tags"
with open("tags", "r") as file:
    testo = file.read()

# Utilizziamo re.search per cercare la data nel testo
match = re.search(r'\d{4}\.\d{2}\.\d{2}', testo)

if match:
    data_trovata = match.group()

    # Scrivi la data su un file di test
    with open("update", "w") as file:
        file.write(data_trovata)

subprocess.call("del tags", shell=True)

print()
print((Fore.RED + "  @@@@@@ @@@  @@@ @@@ @@@@@@@ @@@@@@@@       @@@@@@  @@@  @@@ "))
print((Fore.RED + " !@@     @@!  @@@ @@!   @@!   @@!           @@!  @@@ @@!  @@@ "))
print((Fore.RED + "  !@@!!  @!@  !@! !!@   @!!   @!!!:!        @!@!@!@! @!@  !@! "))
print((Fore.RED + "     !:! !!:  !!! !!:   !!:   !!:           !!:  !!!  !: .:!  "))
print((Fore.RED + " ::.: :   :.:: :  :      :    : :: :::       :   : :    ::    "))
print((Fore.RESET))
print((Fore.GREEN + "                  suiteAV-3.0 Coded by Alexis               "))
print((Fore.GREEN + "                  ---------------------------               "))
print((Style.RESET_ALL))
print()

def checkyoutube():
	file1_path = 'update'
	file2_path = 'yt-ver'

	with open(file1_path, 'r', encoding='utf-8') as check1:
		file1 = check1.read()

	with open(file2_path, 'r', encoding='utf-8') as check2:
		file2 = check2.read()

	if file1 == file2:
		print("STATUS YOUTUBE-DL:",(Fore.BLACK + Back.GREEN + _(" NO UPDATE ")))
		print((Style.RESET_ALL))
		subprocess.call("del update*", shell=True)
	else:
		print("STATUS YOUTUBE-DL:",(Fore.BLACK + Back.RED + _(" UPDATE ")))
		print((Style.RESET_ALL))
		subprocess.call("del update*", shell=True)
checkyoutube()

def checksoftware():
	file1_path = 'check'
	file2_path = 'version'

	if check is True:
		with open(file1_path, 'r', encoding='utf-8') as checka:
			file1 = checka.read()

		with open(file2_path, 'r', encoding='utf-8') as checkb:
			file2 = checkb.read()
	
	if check is False:
		print("STATUS SUITEAV:",(Fore.BLACK + Back.CYAN + _(" SITE OFFLINE ")))
		print((Style.RESET_ALL))
	elif file1 == file2:
		print("STATUS SUITEAV:",(Fore.BLACK + Back.GREEN + _(" NO UPDATE ")))
		print((Style.RESET_ALL))
		subprocess.call("del check*", shell=True)
	else:
		print("STATUS SUITEAV:",(Fore.BLACK + Back.RED + _(" UPDATE ")))
		print((Style.RESET_ALL))
		subprocess.call("del check*", shell=True)
checksoftware()

print()
print()
print(_("*************"))
print(_("* Main Menu *"))
print(_("*************"))
print()
print()
print(_("[1] Updates"))
print()
print()
print("[2] YouTube")
print()
print()
print(_("[3] Downloads"))
print()
print()
print()
print(_("[0] Quit"))
print()
print()
print()
print()

try:
    select = eval(input(": "))
    if select >= 4:
        print()
        print(_("Option not found!"))
        input(_("Press ENTER to continue"))
        os.system("suiteAV.exe")
except NameError:
    print()
    print(_("Invalid command!"))
    input(_("Press ENTER to continue"))
    os.system("suiteAV.exe")
except SyntaxError:
    print()
    print(_("Invalid command!"))
    input(_("Press ENTER to continue"))
    os.system("suiteAV.exe")
except UnboundLocalError:
    print(_("System terminated"))

def update():
	if select == 1:
		subprocess.call("cls", shell=True)
		subprocess.call("python init\\update.py", shell=True)
update()

def youtube():
	if select == 2:
		subprocess.call("cls", shell=True)
		subprocess.call("python init\\youtube.py", shell=True)
youtube()

def downloads():
	if select == 3:
		#os.system("clear")
		subprocess.call("start Downloads\\", shell=True)
		time.sleep(0.5)
		os.system("cls")
		os.system("python suiteAV.py")
downloads()

def close():
	if select == 0:
		subprocess.call("cls", shell=True)
		#subprocess.call("del /f check*", shell=True)
		#os.kill(os.getppid(), signal.SIGHUP) # killa tutto il terminale
		os.system("exit")
		return
close()
