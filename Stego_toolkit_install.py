import os, sys, time
from pathlib import Path #PATH LIBRARY

menuselect = -1

while menuselect != 0:
    os.system('clear')

    print("<><><><><><><><><><><><><><><><><><><><><><><><><>", end="\n")
    print("Wellcome To Docker and Stego_Toolkit autoinstaller", end="\n")
    print("<><><><><><><><><><><><><><><><><><><><><><><><><>", end="\n \n")
    print("For Kali GNU/Linux Rolling - 64 bits - Kernel version 3.36.3", end="\n \n")
    print("<Script by Deckcard23>", end="\n \n")

    print("1.- Install Docker and Stego_Toolkits.", end="\n")
    print("2.- Start Stego_Toolkits.", end="\n")
    print("0.- Exit.", end="\n \n")


    if menuselect != (1, 2) : print("Choose any option:", end="\n \n")

    try:
        menuselect = int(input("--->"))
    except ValueError:
        print('PLease input a valid integer')

    if menuselect == 1:

        os.system('clear')

        print("<><><><><><><><><><><>", end="\n")
        print("STARTING INSTALLATION", end="\n")
        print("<><><><><><><><><><><>", end="\n \n")

        print("<><><><><><>", end="\n")
        print("UPDATING APT", end="\n")
        print("<><><><><><>", end="\n \n")
        os.system('sudo apt update -y')


        print("<><><><><><><><><>", end="\n")
        print("INSTALLING DOCKER", end="\n")
        print("<><><><><><><><><>", end="\n \n")
        os.system('sudo apt install -y docker.io')
        os.system('sudo systemctl enable docker --now')

        print("<><><><><><><><><><><><><>", end="\n")
        print("INSTALLING PYTHON3 OPENCV", end="\n")
        print("<><><><><><><><><><><><><>", end="\n \n")
        os.system('sudo pip3 install opencv')

        print("<><><><><><><><><><><><>", end="\n")
        print("INSTALLING STEGO-TOOLKIT", end="\n")
        print("<><><><><><><><><><><><>", end="\n \n")
        os.system('docker pull dominicbreuker/stego-toolkit')

        print("<><><><><><><><><><><><><><><><><><><><>", end="\n")
        print("CONGRATULATIONS, INSTALLATION COMPLETED", end="\n")
        print("<><><><><><><><><><><><><><><><><><><><>", end="\n \n")

        print("Follow me in Twitter @rickdekard23", end="\n")
        print("or in my website deckcard23.com", end="\n \n")
        input("Press any key to main menu.")

    if menuselect == 2:

        os.system('clear')
        print("TERMINAL COMMANDS", end="\n")
        print("-----------------", end="\n \n")
        print("1-). check_jpg imagename.jpg (fast stego report)", end="\n \n")
        print("2-). brute_jpg imagename.jpg wordlist.txt (try extract hidden data)", end="\n \n")
        print("3-). start_vnc.sh (connect container X11)", end="\n \n")
        print("4-). start_vnc.sh (connect Desktop container with your browser)", end="\n \n \n")
        print("INSTRUCTIONS TO WORK", end="\n")
        print("--------------------", end="\n \n")
        print("When you start docker a container named <Data> is created in your pwd")
        print("directory. You must move or copy the files that you want to analyze")
        print("with stego-toolkit inside <Data> folder. If you write <ls> in data ")
        print("container and appear the files you are ok.", end="\n \n")
        print("MORE INFORMATION AND HELP", end="\n")
        print("-------------------------", end="\n \n")
        print("https://github.com/DominicBreuker/stego-toolkit#tools (TOOLS INTALLER WITH STEGO_TOOLKIT)")
        print("https://github.com/DominicBreuker/stego-toolkit (OFFCIAL REPOSITORY).", end="\n \n")
        os.system('sudo docker run -it data')
        os.system('sudo docker run -it --rm -v $(pwd)/data:/data dominicbreuker/stego-toolkit /bin/bash')
        input("Press any key to main menu.")

    else:
        if menuselect > 2:
            print("Wrong.")

        else:
            os.system('clear')
            print("<><><><><>><><><><><><><><><><><><><><><>", end="\n")
            print("THANKS TO USE STEGO_TOOLKIT AUTOINSTALLER", end="\n")
            print("<><><><><>><><><><><><><><><><><><><><><>", end="\n \n")
            print("Follow me in Twitter @rickdekard23", end="\n")
            print("visit my website deckcard23.com", end="\n")
            print("created in 2020", end="\n \n")
