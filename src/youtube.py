
# Import

import os
import sys
import subprocess
import time
from colorama import Fore, Back, Style, init
import decimal
import string
from simple_colors import *
import gettext


translations = gettext.translation("youtube", localedir="locales", languages=["it"])
translations.install()

init(autoreset=True)

subprocess.call("cls", shell=True)

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=80))

# Start program

ytdl = "yt-dlp.exe"
string1 = "tmp/%(title)s.%(ext)s"
string2 = "%(title)s.%(ext)s"
#string3 = "chapter:%(section_title)s.%(ext)s"


print()
print((Fore.RED + "  @@@@@@ @@@  @@@ @@@ @@@@@@@ @@@@@@@@       @@@@@@  @@@  @@@ "))
print((Fore.RED + " !@@     @@!  @@@ @@!   @@!   @@!           @@!  @@@ @@!  @@@ "))
print((Fore.RED + "  !@@!!  @!@  !@! !!@   @!!   @!!!:!        @!@!@!@! @!@  !@! "))
print((Fore.RED + "     !:! !!:  !!! !!:   !!:   !!:           !!:  !!!  !: .:!  "))
print((Fore.RED + " ::.: :   :.:: :  :      :    : :: :::       :   : :    ::    "))
print((Fore.RESET))
print((Fore.GREEN + "                  suiteAV-3.0 Coded by Alexis                "))
print((Fore.GREEN + "                  ---------------------------                "))
print((Fore.RESET))
print()
print()
print()
print("*****************")
print("*-   YouTube   -*")
print("*****************")
print()
print(_("[1] What resolution can I download?"))
print(_("[2] Download in manual mode"))
print()
print()
print(_("[3] Download from 360p link"))
print(_("[4] Download from 480p link"))
print(_("[5] Download from link to 720p"))
print(_("[6] Download from link to better quality"))
print(_("[7] Download from link to best quality with split*"))
print(_("[8] Download from best quality link with metadata*"))
print()
print()
print(_("[9] Downloading Playlist via file"))
print()
print()
print()
print("Youtube or SoundCloud")
print("---------------------")
print()
print(_("[10] Download to MP3 HQ"))
print(_("[11] Download album to MP3 HQ with split*"))
print()
print(_("[12] Download MP3 via file"))
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
	youtube = eval(input(": "))
	if youtube >= (14):
		print()
		print(_("Option not found!"))
		input(_("Press ENTER to continue"))
		os.system("init\\youtube.exe")
except NameError:
	print()
	print(_("Invalid command!"))
	input(_("Press ENTER to continue"))
	os.system("init\\youtube.exe")
except SyntaxError:
    print()
    print(_("Invalid command!"))
    input(_("Press ENTER to continue"))
    os.system("init\\youtube.exe")

def main():

	if youtube == 1:
		link = input("Copy video link: ")
		convert = "%s --list-formats %s"
		os.system(convert % (ytdl, link))
		print()
		input("Press ENTER to continue")
		subprocess.call("init\\youtube.exe", shell=True)
	if youtube == 2:
		link = input("Copy video or playlist link: ")
		convert = "%s --list-formats %s"
		os.system(convert % (ytdl, link))
		time.sleep(4)
		print()
		print()
		number = input(_("Enter quality code, e.g.245+91 (video+audio): "))
		convert = "%s -f %s -o %s %'"
		os.system(convert % (ytdl, number, string1, link))
		subprocess.call("@move tmp\\*.mp4 .\\Downloads\\Video\\ || @move tmp\\*.mkv .\\Downloads\\Video\\ || @move tmp\\*.webm .\\Downloads\\Video\\", shell=True)
		#subprocess.call("rm nohup.out", shell=True)
		print()
		print(_("Operation completed!"))
		print()
		time.sleep(3)
		print()
		input(_("Press ENTER to continue"))
		subprocess.call("init\\youtube.exe", shell=True)
	if youtube == 3:
		link = input(_("Copy video or playlist link: "))
		convert = "%s -f 18 -add-meta -o %s %s"
		os.system(convert % (ytdl, string1, link))
		subprocess.call("@move tmp\\*.mp4 .\\Downloads\\Video\\ || @move tmp\\*.mkv .\\Downloads\\Video\\ || @move tmp\\*.webm .\\Downloads\\Video\\", shell=True)
		#subprocess.call("rm nohup.out", shell=True)
		print()
		print(_("Operation completed!"))
		print()
		time.sleep(3)
		print()
		input(_("Press ENTER to continue"))
		subprocess.call("init\\youtube.exe", shell=True)
	if youtube == 4:
		link = input(_("Copy video or playlist link: "))
		convert = "%s -f 1.5.1 -add-meta -o %s %s"
		os.system(convert % (ytdl, string1, link))
		subprocess.call("@move tmp\\*.mp4 .\\Downloads\\Video\\ || @move tmp\\*.mkv .\\Downloads\\Video\\ || @move tmp\\*.webm .\\Downloads\\Video\\", shell=True)
		#subprocess.call("rm nohup.out", shell=True)
		print()
		print(_("Operation completed!"))
		print()
		time.sleep(3)
		print()
		input(_("Press ENTER to continue"))
		subprocess.call("init\\youtube.exe", shell=True)
	if youtube == 5:
		link = input(_("Copy video or playlist link: "))
		convert = "%s -f 22 -add-meta  -o %s %s"
		os.system(convert % (ytdl, string1, link))
		subprocess.call("@move tmp\\*.mp4 .\\Downloads\\Video\\ || @move tmp\\*.mkv .\\Downloads\\Video\\ || @move tmp\\*.webm .\\Downloads\\Video\\", shell=True)
		#subprocess.call("rm nohup.out", shell=True)
		print()
		print(_("Operation completed!"))
		print()
		time.sleep(3)
		print()
		input(_("Press ENTER to continue"))
		subprocess.call("init\\youtube.exe", shell=True)
	if youtube == 6:
		link = input(_("Copy video or playlist link: "))
		convert = "%s -f bestvideo+bestaudio/best -o %s %s"
		os.system(convert % (ytdl, string1, link))
		subprocess.call("@move tmp\\*.mp4 .\\Downloads\\Video\\ || @move tmp\\*.mkv .\\Downloads\\Video\\ || @move tmp\\*.webm .\\Downloads\\Video\\", shell=True)
		#subprocess.call("rm nohup.out", shell=True)
		print()
		print(_("Operation completed!"))
		print()
		time.sleep(3)
		print()
		input(_("Press ENTER to continue"))
		subprocess.call("init\\youtube.exe", shell=True)
	if youtube == 7:
		print()
		print((Fore.RED + _("*The split function only works if metadata is present in the video!")))
		print((Style.RESET_ALL))
		link = input(_("Copy video or playlist link: "))
		convert = "%s -f bestvideo+bestaudio/best --split-chapters -o %s -P tmp %s"
		os.system(convert % (ytdl, string2, link))
		subprocess.call("@move tmp\\*.mp4 .\\Downloads\\Video\\ || @move tmp\\*.mkv .\\Downloads\\Video\\ || @move tmp\\*.webm .\\Downloads\\Video\\", shell=True)
		#subprocess.call("rm nohup.out", shell=True)
		print()
		print(_("Operation completed!"))
		print()
		time.sleep(3)
		print()
		input(_("Press ENTER to continue"))
		subprocess.call("init\\youtube.exe", shell=True)
	if youtube == 8:
		print()
		print((Fore.RED + _("*The metadata function only works if metadata is present in the video!")))
		print((Style.RESET_ALL))
		link = input(_("Copy video or playlist link: "))
		convert = "%s -f bestvideo+bestaudio/best -add-meta  -o %s %'"
		os.system(convert % (ytdl, string1, link))
		subprocess.call("@move tmp\\*.mp4 .\\Downloads\\Video\\ || @move tmp\\*.mkv .\\Downloads\\Video\\ || @move tmp\\*.webm .\\Downloads\\Video\\", shell=True)
		#subprocess.call("rm nohup.out", shell=True)
		print()
		print(_("Operation completed!"))
		print()
		time.sleep(3)
		print()
		input(_("Press ENTER to continue"))
		subprocess.call("init\\youtube.exe", shell=True)

	if youtube == 9:
		subprocess.call("init\\playlist.exe", shell=True)

	if youtube == 10:
		link = input(_("Copy video or playlist link: "))
		convert = "%s -x --audio-format mp3 --audio-quality 0 --embed-thumbnail --convert-thumbnails jpg -o %s %s"
		os.system(convert % (ytdl, string1, link))
		subprocess.call("move tmp\\*.mp3 .\\Downloads\\Audio\\", shell=True)
		#subprocess.call("rm nohup.out", shell=True)
		print()
		print(_("Operation completed!"))
		print()
		time.sleep(3)
		print()
		input(_("Press ENTER to continue"))
		subprocess.call("init\\youtube.exe", shell=True)
	if youtube == 11:
		print()
		print((Fore.RED + _("*The split function only works if metadata is present in the video!")))
		print((Style.RESET_ALL))
		link = input(_("Copy video or playlist link: "))
		convert = "%s -x --audio-format mp3 --audio-quality 0 --yes-playlist --embed-thumbnail --convert-thumbnails jpg --split-chapters -P tmp -o %s %s"
		os.system(convert % (ytdl, string2, link))
		subprocess.call("move tmp\\*.mp3 .\\Downloads\\Audio\\", shell=True)
		#subprocess.call("rm nohup.out", shell=True)
		print()
		print(_("Operation completed!"))
		print()
		time.sleep(3)
		print()
		input(_("Press ENTER to continue"))
		subprocess.call("init\\youtube.exe", shell=True)
	if youtube == 12:
		link = input(_("Enter playlist file name: "))
		convert = "%s -x --audio-format mp3 --audio-quality 0 -o %s -a %s"
		os.system(convert % (ytdl, string1, link))
		subprocess.call("move tmp\\*.mp3 .\\Downloads\\Audio\\", shell=True)
		#subprocess.call("rm nohup.out", shell=True)
		print()
		print(_("Operation completed!"))
		print()
		time.sleep(3)
		print()
		input(_("Press ENTER to continue"))
		subprocess.call("init\\youtube.exe", shell=True)

	if youtube == 0:
		subprocess.call("cls", shell=True)
		subprocess.call("suiteAV.exe", shell=True)
main()
