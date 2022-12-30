#!/usr/bin/env python3

import socket
import sys

logo = ('''\033[1;31m
                              __
                     /\    .-" /
                    /  ; .'  .' 
                   :   :/  .'   
                    \  ;-.'     
       .--""""--..__/     `.    
     .'           .'    `o  \   
    /                    `   ;  
   :                  \      :  
 .-;        -.         `.__.-'  
:  ;          \     ,   ;       
'._:           ;   :   (        
    \/  .__    ;    \   `-.     
     ;     "-,/_..--"`-..__)    
     '""--.._:                  
                   
                    By: Lagone
 
\033[1;31m''')


print(logo)
print("\033[49;35m Portscanner de protocolo TCP/IP\033[49;35m")
print("\033[49;96m Dominio ex: google.com \033[49;96m")
host = input("\033[49;90m dominio do site: \033[49;90m")

sys.argv[0]


ports = [80,443,22,25,465,21,23,53]

try:

  for port in ports:

      client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client.settimeout(2.0)
      conexao = client.connect_ex((host, port))
    
      if conexao == 0:
         print("\033[49;97m > ",port, "open \033[49;97m ")
      

except socket.gaierror:
  print("\033[1;31m                        Host Invalido\033[1;31m")
  exit()

except KeyboardInterrupt:
  print("\033[1;31m Saindo\033[1;31m ")
  exit()
