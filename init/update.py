
# Importazione

import os, sys, subprocess
import time
from colorama import Fore, Back, Style, init
import decimal
import signal
import gettext
import requests
import zipfile

translations = gettext.translation("update", localedir="locales", languages=["it"])
translations.install()
_ = translations.gettext  # Definisci '_' qui


init(autoreset=True)

subprocess.call("cls", shell=True)

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=80))

# Start program


print()
print((Fore.RED + "  @@@@@@ @@@  @@@ @@@ @@@@@@@ @@@@@@@@       @@@@@@  @@@  @@@ "))
print((Fore.RED + " !@@     @@!  @@@ @@!   @@!   @@!           @@!  @@@ @@!  @@@ "))
print((Fore.RED + "  !@@!!  @!@  !@! !!@   @!!   @!!!:!        @!@!@!@! @!@  !@! "))
print((Fore.RED + "     !:! !!:  !!! !!:   !!:   !!:           !!:  !!!  !: .:!  "))
print((Fore.RED + " ::.: :   :.:: :  :      :    : :: :::       :   : :    ::    "))
print((Fore.RESET))
print((Fore.GREEN + "                  suiteAV-3.2 Coded by Alexis               "))
print((Fore.GREEN + "                  ---------------------------               "))
print((Fore.RESET))
print()
print()
print()
print(_("***************"))
print(_("* Update Menu *"))
print(_("***************"))
print()
print()
print(_("[1] Update suiteAV"))
print(_("[2] Update Youtube software"))
print()
print()
print()
print()
print(_("[0] Back"))
print()
print()
print()
print()


try:
	select = eval(input(": "))
	if select >= 3:
		print(_("Option not found!"))
		input(_("Press ENTER to continue"))
		os.system("python init\\update.py")
except NameError:
	print(_("Invalid command!"))
	input(_("Press ENTER to continue"))
	os.system("python init\\update.py")
except SyntaxError:
	print()
	print(_("Invalid command!"))
	input(_("Press ENTER to continue"))
	os.system("python init\\update.py")
except UnboundLocalError:
	print(_("System terminated"))


if select == 0:
	subprocess.call("cls", shell=True)
	subprocess.call("python suiteAV.py", shell=True)

def suiteAV():
	if select == 1:
		time.sleep(1)
		print()
		print(_("Updating..."))
		print()
		url = "https://github.com/alexis-82/suiteAV-win/archive/refs/heads/main.zip"
		response = requests.get(url)
		if response.status_code == 200:
		# Salva il file sul tuo computer
			with open("suiteAV.zip", "wb") as f:
				f.write(response.content)
		with zipfile.ZipFile("suiteAv.zip") as z:
			z.extractall()
		#subprocess.call("move suiteAV-win-main\\* .\\", shell=True)
		subprocess.call("xcopy suiteAV-win-main\\* .\\ /E /H /C /I", shell=True)
		subprocess.call("del /f suiteAV.zip", shell=True)
		subprocess.call("rmdir /q /s suiteAV-win-main", shell=True)
		time.sleep(3)
		print()
		print(_("SuiteAV update completed, restart the program!"))
		print()
		time.sleep(3)
		print()
		input(_("Press ENTER to continue"))
		subprocess.call("cls", shell=True)
		os.system("exit")
		return
suiteAV()

def yt_dl():
	if select == 2:
		time.sleep(1)
		print()
		print(_("Updating..."))
		print()
		# subprocess.call("yt-dlp.exe -U", shell=True)
		subprocess.call("pip install --upgrade yt-dlp", shell=True)
		subprocess.call("yt-dlp --version > yt-dlp", shell=True)
		with open("yt-dlp", "r") as file:
			lines = file.readlines()
			# Rimuovi le righe vuote
		lines = [line.strip() for line in lines if line.strip()]
		with open("yt-ver", "w") as file:
			file.write("\n".join(lines))
		subprocess.call("del yt-dlp", shell=True)
		subprocess.call("move /Y yt-ver ..\\", shell=True)
		time.sleep(3)
		time.sleep(3)
		print()
		print(_("Update completed!"))
		print()
		time.sleep(3)
		print()
		input(_("Press ENTER to continue"))
		subprocess.call("python suiteAV.py", shell=True)
yt_dl()
