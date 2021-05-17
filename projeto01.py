import subprocess
import os
import time
import sys
import logo as l1
import platform
import cliente as c1
import socket

so=platform.system()




class bcolors:
    
    ERRO = '\033[91m'
    OK = '\033[94m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    AZUL = '\033[1;44m '
os.system("clear")
print(bcolors.WARNING + "AVISO: DESEJA CONTINUAR?sim[1]nao[2]" + bcolors.RESET)
escolha = int(input(""))
menu = 99
if escolha == 2:
    print("vai ver peppa")
    print("aborting...")
    time.sleep(2)
else:

    
    while menu  == 99 :
       
        os.system('clear')
        
        l1.menu_inicial()
           
           

        print(bcolors.WARNING+"\n\n o que voce deseja fazer?"+bcolors.RESET)
        print("abrir ferramentas[1] abrir programas comuns[2] Instalar ferramentas[3]")
        escolha1 = int(input(""))
               
               
            #FERRAMENTAS
           
            
        if escolha1 ==1:
            
                       print(bcolors.OK+"Abrir metasploit[1] abrir nmap[2] abrir aircrackng[3] "+bcolors.RESET)
                       print(bcolors.ERRO+"Retornar ao menu[99]"+bcolors.RESET)
                       escolha2 = int(input(""))
                       if escolha2 == 99:
                               menu == 99
       
                       if escolha2 == 1:
                           print(bcolors.ERRO+"ATENCAO NAO NOS RESPONSABILISAMOS POR SEUS ATOS"+bcolors.RESET)
                           print(bcolors.WARNING+"O PROGRAMA A SEGUIR CONTEM ARQUIVOS PERIGOSOS ESTEJA CIENTE DISSO"+bcolors.RESET)
                           print(bcolors.OK+"ABRINDO MSFCONSOLE"+bcolors.RESET)
                           processo = subprocess.call(["msfconsole"], shell=True)
       
                       if escolha2 == 2:
                           menu = 0
                           print(bcolors.ERRO+"ATENCAO NAO NOS RESPONSABILISAMOS POR SEUS ATOS"+bcolors.RESET)
                           print(bcolors.WARNING+"O PROGRAMA A SEGUIR CONTEM CAPACIDADES PERIGOSOS ESTEJA CIENTE DISSO"+bcolors.RESET)
                           print(bcolors.OK+"ABRINDO NMAP"+bcolors.RESET)
                           processo = subprocess.call(["nmap"], shell=True)
                      
       
                       if escolha2 == 3:
                           menu = 0
                           print(bcolors.ERRO+"ATENCAO NAO NOS RESPONSABILISAMOS POR SEUS ATOS"+bcolors.RESET)
                           print(bcolors.WARNING+"O PROGRAMA A SEGUIR CONTEM CAPACIDADES PERIGOSOS ESTEJA CIENTE DISSO"+bcolors.RESET)
                           print(bcolors.OK+"ABRINDO MSFCONSOLE"+bcolors.RESET)
                           processo = subprocess.call(["aircrack-ng"], shell=True)
                           
            
        if escolha1 ==2:
            os.system("clear")
               
            print("em construcao")
            
            time.sleep(3)
            
            menu == 99
                       
            

               #baixar ferramentas
        if escolha1 ==3:
            os.system("clear")
            print("Qual programa voce deseja instalar em sua maquina?(as ferramentas serao salvas na pasta tools")
            print(bcolors.OK+"nmap[1] metasploit[2] aircrack-ng[3]"+bcolors.RESET)
            print(bcolors.ERRO+"Retornar ao menu[99]"+bcolors.RESET)
            escolha3 = int(input(""))
            if escolha3 == 99:                        
                    menu == 99
            if escolha3 ==1:
                processo = subprocess.call(["git clone https://github.com/nmap/nmap","mkdir tools"], shell=True)
            if escolha3 ==2:
                processo = subprocess.call(["git clone https://github.com/rapid7/metasploit-framework.git","mkdir tools"], shell=True)
            if escolha3 ==3:
                processo = subprocess.call(["git clone https://github.com/aircrack-ng/aircrack-ng.git","mkdir tools"], shell=True)
        if escolha1 ==4:
            menu =0
            os.system("clear")
            l1.caveira()
            print("SERVIDOR FEITO EM PYTHON[1] QUEBRA DE SENHA[2] SO do HOST[3]")  
            print("Retornar ao menu principal[99]")
            escolha5=int(input(""))
            if escolha5==99:
                menu=99
            if escolha5==1:
                print("abrir conexao[1] fechar conexao[2]")
                escolha6=int(input(""))
                
                if escolha6==1:
                    #mandar programa executar um comando no terminal q inicia o servidor
                        
                        HOST = '127.0.0.1'
                        PORT = 50000
        
                        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((HOST, PORT))
                        s.sendall(str.encode("bom dia"))
                        data = s.recv(1024)
                        
                        print("conexao bem sucedida")
                        print("retornar ao menu principal")
                        time.sleep(2)
                        menu=99
                if escolha6 ==2:
                        print('fechando conexao')
                        s.close()
                        menu=99
                        
                        
                
                    
                        
        
        
      
        
        
