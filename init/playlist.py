#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import

import os
import sys
import subprocess
import time
from colorama import Fore, Back, Style, init
import decimal
import string
import gettext

translations = gettext.translation("playlist", localedir="locales", languages=["it"])
translations.install()
_ = translations.gettext  # Definisci '_' qui


init(autoreset=True)

subprocess.call("cls", shell=True)

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=80))

# Start program

ytdl = "yt-dlp"
string1 = "%(title)s.%(ext)s"
string2 = "chapter:%(section_title)s.%(ext)s"
string3 = "%(autonumber)s-%(title)s.%(ext)s"
string4 = "%(chapter_number)s-%(chapter)s.%(ext)s"


subprocess.call("cls", shell=True)
print()
print((Fore.RED + "  @@@@@@ @@@  @@@ @@@ @@@@@@@ @@@@@@@@       @@@@@@  @@@  @@@ "))
print((Fore.RED + " !@@     @@!  @@@ @@!   @@!   @@!           @@!  @@@ @@!  @@@ "))
print((Fore.RED + "  !@@!!  @!@  !@! !!@   @!!   @!!!:!        @!@!@!@! @!@  !@! "))
print((Fore.RED + "     !:! !!:  !!! !!:   !!:   !!:           !!:  !!!  !: .:!  "))
print((Fore.RED + " ::.: :   :.:: :  :      :    : :: :::       :   : :    ::    "))
print((Fore.RESET))
print((Fore.GREEN + "                  suiteAV-3.2 Coded by Alexis                "))
print((Fore.GREEN + "                  ---------------------------                "))
print((Fore.RESET))
print()
print()
print()
print("**************************")
print("*-   YouTube Playlist   -*")
print("**************************")
print()
print(_("[1] Download playlist with meta via file"))
print(_("[2] Download playlist by file with split"))
print(_("[3] Download playlist with chapter numbering"))
#print(("[5] Download playlist with chapter numbering"))
print()
print()
print(_("[4] Download playlist by file"))
print()
print()
print(_("[0] Back"))
print()
print()
print()
print()

try:
    youtube = eval(input(": "))
    if youtube >= (6):
        print()
        print(_("Option not found!"))
        input(_("Press ENTER to continue"))
        os.system("python python init\\playlist.py")
except NameError:
    print()
    print(_("Invalid command!"))
    input(_("Press ENTER to continue"))
    os.system("python python init\\playlist.py")
except SyntaxError:
    print()
    print(_("Invalid command!"))
    input(_("Press ENTER to continue"))
    os.system("python python init\\playlist.py")

def main():
    if youtube == 1:
        file = input(_("Enter playlist file name: "))
        convert ='%s -f bestvideo+bestaudio/best --add-meta -o "%s" -P tmp -a "%s"'
        os.system(convert % (ytdl, string1, file))
        subprocess.call("@move tmp\\*.mp4 .\\Downloads\\Video\\ || @move tmp\\*.mkv .\\Downloads\\Video\\ || @move tmp\\*.webm .\\Downloads\\Video\\", shell=True)
        #subprocess.call("rm nohup.out", shell=True)
        print()
        print(_("Operation completed!"))
        print()
        #subprocess.call("notify-send 'suiteAV' 'Download completato!' -i /usr/share/icons/suiteAV.png", shell=True)
        time.sleep(3)
        print()
        input(_("Press ENTER to continue"))
        subprocess.call("python init\\playlist.py", shell=True)
    if youtube == 2:
        link = input(_("Enter playlist file name: "))
        convert = '%s -f bestvideo+bestaudio/best --split-chapters -o "%s" -P tmp -a "%s"'
        os.system(convert % (ytdl, string2, link))
        subprocess.call("@move tmp\\*.mp4 .\\Downloads\\Video\\ || @move tmp\\*.mkv .\\Downloads\\Video\\ || @move tmp\\*.webm .\\Downloads\\Video\\", shell=True)
        #subprocess.call("rm nohup.out", shell=True)
        print()
        print(_("Operation completed!"))
        print()
        #subprocess.call("notify-send 'suiteAV' 'Download completato!' -i /usr/share/icons/suiteAV.png", shell=True)
        time.sleep(3)
        print()
        input(_("Press ENTER to continue"))
        subprocess.call("python init\\playlist.py", shell=True)
    if youtube == 3:
        link = input(_("Enter playlist file name: "))
        convert = '%s -f bestvideo+bestaudio/best -cio "%s" -P tmp -a "%s"'
        os.system(convert % (ytdl, string3, link))
        subprocess.call("@move tmp\\*.mp4 .\\Downloads\\Video\\ || @move tmp\\*.mkv .\\Downloads\\Video\\ || @move tmp\\*.webm .\\Downloads\\Video\\", shell=True)
        #subprocess.call("rm nohup.out", shell=True)
        print()
        print(_("Operation completed!"))
        print()
        #subprocess.call("notify-send 'suiteAV' 'Download completato!' -i /usr/share/icons/suiteAV.png", shell=True)
        time.sleep(3)
        print()
        input(_("Press ENTER to continue"))
        subprocess.call("python init\\playlist.py", shell=True)
    if youtube == 4:
        file = input(_("Enter playlist file name: "))
        convert ='%s -f bestvideo+bestaudio/best -o "%s" -P tmp -a "%s"'
        os.system(convert % (ytdl, string1, file))
        subprocess.call("@move tmp\\*.mp4 .\\Downloads\\Video\\ || @move tmp\\*.mkv .\\Downloads\\Video\\ || @move tmp\\*.webm .\\Downloads\\Video\\", shell=True)
        #subprocess.call("rm nohup.out", shell=True)
        print()
        print(_("Operation completed!"))
        print()
        #subprocess.call("notify-send 'suiteAV' 'Download completato!' -i /usr/share/icons/suiteAV.png", shell=True)
        time.sleep(3)
        print()
        input(_("Press ENTER to continue"))
        subprocess.call("python init\\playlist.py", shell=True)
    if youtube == 5:
        link = input(_("Enter playlist file name: "))
        convert = '%s --split-chapters -f bestvideo+bestaudio/best --add-meta -o "%s" -P tmp -a "%s"'
        os.system(convert % (ytdl, string4, link))
        subprocess.call("@move tmp\\*.mp4 .\\Downloads\\Video\\ || @move tmp\\*.mkv .\\Downloads\\Video\\ || @move tmp\\*.webm .\\Downloads\\Video\\", shell=True)
        #subprocess.call("rm nohup.out", shell=True)
        print()
        print(_("Operation completed!"))
        print()
        #subprocess.call("notify-send 'suiteAV' 'Download completato!' -i /usr/share/icons/suiteAV.png", shell=True)
        time.sleep(3)
        print()
        input(_("Press ENTER to continue"))
        subprocess.call("python init\\playlist.py", shell=True)

    if youtube == 0:
        subprocess.call("cls", shell=True)
        subprocess.call("python init\\youtube.py", shell=True)
main()