#-----------------------------------------
# scripted by samay 
# design credits : Vaimpier ritik 
# Python3 database expert 
# Vaim - Samay Projects 
# Copy This script does makes you coder 
#------------------------------------------

#----------- imports 

from os import system
from time import sleep
import random
import sys

#----------- Colors

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"

#------------ Banner 

logo = """\033[1;37m

\033[1;37m[!] \033[1;31mThis is use for File Editing, You can Unlimitedly Edit !!! BYE :_)
\033[1;37m
┌-=============================   -   
=      \033[1;31m . ┌──────── \033[1;37mVaim-Samay    -   
=  \033[1;31m .┌───  \033[1;37mB-Hat VaimSamay        -   \033[34m[✔]     https://github.com/samay825        [✔]
\033[1;37m=    FileEditor - Pro             -   \033[34m[✔]            Version 2.0                 [✔]
\033[1;37m= \033[1;31m . └──── \033[1;37mBY Samay               -   \033[91m[X] Please Don't Use For illegal Activity  [X]
\033[1;37m= \033[1;31m .     └─── \033[1;37mVERSION 2.0         -
\033[1;37m└-=============================   -

\033[1;31m    
Disclaimer: \033[1;32mthis tool is designed for Prank
	    testing in an authorized simulated cyberattack
	    Attacking targets without prior mutual consent
            is illegal!                                                               
\033[1;37m                                    
\033[97m """

#--------------------------------------------------------------------------
# func of banner , space , about me 

def banner():
    print(logo)

def deprint():
    print("\n")

def bye():
	os.system("clear")
	banner()
	string = """ 
	\033[1;37mDeveloper  \033[1;34m: \033[1;31mVAIM-SAMAY

	\033[1;37mGithub     \033[1;34m: \033[1;31msamay825

	\033[1;37mInstagram  \033[1;34m: \033[1;31mvaimpier_ritik

	\033[1;37mE-mail     \033[1;34m: \033[1;31mcybokhackers@gmail.com
	"""
	for letter in string:
	  sleep(0.01) 
	  sys.stdout.write(letter)
	  sys.stdout.flush()
	print("\n")



#------------------------------------------------------------------------------
#-------------------------V-A-I-M-P-I-E-R-----S-A-M-A-Y------------------------
#------------------------------------------------------------------------------

class Banner:
    handle = "Bannering_indexbanner"
    def __init__(self):
        system('clear')
        banner()
class Main_second:
    handle_2 = "Options"
    def samay_main(self):
        super().__init__()
        print(r+"└─"+w+"\033[1;37m[ 1 ] Replace : ")
        print(r+"└─"+w+"\033[1;37m[ 2 ] Capital : ")
        print(r+"└─"+w+"\033[1;37m[ 3 ] Lower : ")
        print(r+"└─"+w+"\033[1;37m[ 4 ] Remove : ")
        print(r+"└─"+w+"\033[1;37m[ 5 ] About us : ")
        print(r+"└─"+w+"\033[1;37m[ 6 ] Exit : ")
        deprint()
class Main:
    handle = "Main_func"  
    def Options(self):
        opp=int(input(r+"└─"+w+"\033[1;37mEnter Desire Option: "+r))
        if opp==1:
            Main_part_1 = Main()
            Main_part_1.samay_main_part_1()
        elif opp==2:
            Main_part_2 = Main()
            Main_part_2.samay_main_part_2()
        elif opp==3:
            Main_part_3 = Main()
            Main_part_3.samay_main_part_3()
        elif opp==4:
            Main_part_4 = Main()
            Main_part_4.samay_main_part_4()
        elif opp==5:
            bye()
        elif opp==6:
            banner()
            deprint()
            print(r+"..└─"+w+"\033[1;37mExiting Wait !  "+r)
            deprint()
            sleep(3.0)
            sys.exit()
#--------------------------------------------------------------------------------------
    def returnfunc_1(self):
        samay_main_return = input(r+"..└─"+w+"\033[1;37mRepeat This  [ y / n ]: "+r)
        if samay_main_return=="y" or samay_main_return=="Y":
            Main_part_return_part_1 = Main()
            while True:    
               Main_part_return_part_1.samay_main_part_1()
        else:
            system('python3 Filepro.py')
    def returnfunc_2(self):
        samay_main_return = input(r+"..└─"+w+"\033[1;37mRepeat This  [ y / n ]: "+r)
        if samay_main_return=="y" or samay_main_return=="Y":
            Main_part_return_part_2 = Main()
            while True:    
               Main_part_return_part_2.samay_main_part_2()
        else:
            system('python3 Filepro.py')
    def returnfunc_3(self):
        samay_main_return = input(r+"..└─"+w+"\033[1;37mRepeat This  [ y / n ]: "+r)
        if samay_main_return=="y" or samay_main_return=="Y":
            Main_part_return_part_3 = Main()
            while True:    
               Main_part_return_part_3.samay_main_part_3()
        else:
            system('python3 Filepro.py')
    def returnfunc_4(self):
        samay_main_return = input(r+"..└─"+w+"\033[1;37mRepeat This  [ y / n ]: "+r)
        if samay_main_return=="y" or samay_main_return=="Y":
            Main_part_return_part_4 = Main()
            while True:    
               Main_part_return_part_4.samay_main_part_4()
        else:
            system('python3 Filepro.py')
#-------------------------------------------------------------------------------------
    def samay_main_part_1(self):
        system('clear')
        banner()
        deprint()
        samay_conf = input(r+"└─"+w+"\033[1;37mEnter name of File [With .extension]: "+r)
        deprint()
        with open(f'{samay_conf}','r') as f:
            data = f.read()
        samay_conf_2 = input(r+"└─"+w+"\033[1;37mReplace : "+r)
        deprint()
        samay_conf_3 = input(r+"└─"+w+"\033[1;37mTo : "+r)
        deprint()
        with open(f'{samay_conf}','w') as f:
            data = data.replace(samay_conf_2, samay_conf_3)
            f.write(data)
        print(g+f"└─ File named : {samay_conf} Replaced ---> {samay_conf_2} to ---> {samay_conf_3} !")
        deprint()
        samay_return = Main()
        samay_return.returnfunc_1()      
#-----------------------------------------------------------------------------------------
    def samay_main_part_2(self):
        system('clear')
        banner()
        deprint()
        samay_conf = input(r+"└─"+w+"\033[1;37mEnter name of File [With .extension]: "+r)
        deprint()
        with open(f'{samay_conf}','r') as f:
            data = f.read()
        with open(f'{samay_conf}','w') as f:
            data = data.upper()
            f.write(data)
        print(g+f"└─ File named : {samay_conf} Capitalized Successfully ! ")
        deprint()
        samay_return_2 = Main()
        samay_return_2.returnfunc_2()
#------------------------------------------------------------------------------------------
    def samay_main_part_3(self):
        system('clear')
        banner()
        deprint()
        samay_conf = input(r+"└─"+w+"\033[1;37mEnter name of File [With .extension]: "+r)
        deprint()
        with open(f'{samay_conf}','r') as f:
            data = f.read()
        with open(f'{samay_conf}','w') as f:
            data = data.lower()
            f.write(data)
        print(g+f"└─ File named : {samay_conf} Lowered Successfully ! ")
        deprint()
        samay_return_3 = Main()
        samay_return_3.returnfunc_3()
#--------------------------------------------------------------------------------------------
    def samay_main_part_4(self):
        system('clear')
        banner()
        deprint()
        samay_conf = input(r+"└─"+w+"\033[1;37mEnter name of File [With .extension]: "+r)
        deprint()
        samay_conf_2 = input(r+"└─"+w+"\033[1;37mEnter word/text to Remove : "+r)
        deprint()
        with open(f'{samay_conf}','r') as f:
            data = f.read()
        with open(f'{samay_conf}','w') as f:
            data = data.replace(samay_conf_2,"")
            f.write(data)
        print(g+f"└─ File named : {samay_conf} --- {samay_conf_2} removed  Successfully ! ")
        deprint()
        samay_return_4 = Main()
        samay_return_4.returnfunc_4()
#---------------------------------------------------------------------------------------------
samay = Banner()
samay2 = Main_second()
samay2.samay_main()
samay3 = Main()
samay3.Options()



