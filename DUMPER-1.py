#UTF8 CODING
#OPEN SOURCE CODE FOR ALL
#AUTHOR HAMAYON KHAN
# I JUST NEED YOUR CREDIT WHILE U USING OR EDITING MY CODE
#AT LAEST ITS MY RIGHT BAECUZ BY WORKING HARD I HAVE MADE IT
# LONG TIME AFGHANISTAN🇦🇫

import os
import requests
import random

# clear terminal screen
os.system("clear")

# logo with fancy colors
def logo():
    logo=("""\033[1;92m
########  ##     ## ##     ## ########  ######## ########  
##     ## ##     ## ###   ### ##     ## ##       ##     ## 
##     ## ##     ## #### #### ##     ## ##       ##     ## 
##     ## ##     ## ## ### ## ########  ######   ########  
##     ## ##     ## ##     ## ##        ##       ##   ##   
##     ## ##     ## ##     ## ##        ##       ##    ##  
########   #######  ##     ## ##        ######## ##     ## 
\033[1;32m--------------------------------------------------
[+] AUTHOR   : HAMAYON KHAN
[+] GITHUB   : HLS706
[+] CODE     : RANDOM DUMP OPEN SOURCE
[+] VERSION  : DUMPER-1
\033[1;32m----------------------------------------------""")
    print(logo)
    print('\033[1;32m[1] DUMP UID NEW \n[2] DUMP UID OLD \n[3] OUR FB GROUP \n[4] EXIT PROGRAM')
# main function
def HLS():
    tanya = input("[+] SELECT OPTION: ")

    access_token = "YOUR_ACCESS_TOKEN_HERE" # Set your access token here

    if tanya == "1":
        output = input("\n[+] ENTER THE FILE NAME U WANT TO SAVE: ")
        id = int(input("[+] AMOUNT: "))
        random_numbers = ["100093" + str(random.randint(11111111111, 99999999999)) for i in range(id)]
        print ("[+] Total IDs:",len(random_numbers))

        with open(output, 'w') as file:
            for number in random_numbers:
                file.write(str(number) + '\n')
        print ("\n[+] SUCCESSFUL DUMPED...")
        print ("[+] IDs saved in:", output)

    elif tanya == "2":
        output = input("\n[+] ENTER THE NAME OF FILE U WANT TO SAVE: ")
        id = int(input("[+] Limit: "))
        random_numbers = ["10000" + str(random.randint(111111111, 999999999)) for i in range(id)]
        print ("[+] Total IDs:",len(random_numbers))

        with open(output, 'w') as file:
            for number in random_numbers:
                uid = str(number)
                r = requests.get(f"https://graph.facebook.com/{uid}?fields=name&access_token={access_token}")
                if "name" in r.json():
                    name = r.json()["name"]
                    file.write(f"{uid} ({name})" + '\n')
                else:
                    file.write(uid + '\n')
        print ("\n[+] SUCCESSFUL DUMPED...")
        print ("[+] IDS SAVED IN:", output)

    elif tanya == "4":
        exit()

    elif tanya == "3":
        os.system('xdg-open  https://facebook.com/groups/2526235434185264/')
    else:
        exit()
logo()
HLS()

