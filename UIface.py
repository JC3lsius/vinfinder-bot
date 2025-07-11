from datetime import datetime, timezone
from time import sleep
import platform
import requests
import psutil
import sys
import os



def mostrar_menu(hilos_activos=[]):

    print("""\n 
       ..-+**************************+-..
     .+**********************************+.
    :+*************************************:
    =**************++*********+::**********=.
    +***********.     -*****+.  +**********+.
    +***********      :*****:  :***********+.
    +***********.     :****=   -***********+.
    +***********.     .****   .+***********+.
    +***********-     .+**:   -************+.
    +***********=      +*+.   *************+.
    +***********+.     =*-   -*************+.
    +************:     -+.  .+*************+.
    +************+     ..  .=***************.
    +*************:        =****************.
    +**************:    :+*****************+.
    :**************************************:
     .+**********************************+.
       .:=****************************=:.""")

    if(len(hilos_activos) > 0):
            imprimirHilos(hilos_activos)

    print(
        f"\n--- Menú de opciones ---\n"
        f"1. Ver información del Programa y del Sistema\n"
        f"2. Cargar configuración\n"
        f"3. Iniciar\n"
        f"4. Salir\n"
    )
    return input("Seleccione una opción: ")



def imprimirHilos(hilos_activos):
    printed = "[ "
    for hilo in hilos_activos:
        if(hilo.is_alive):
            if(len(hilos_activos) > 1): 
                printed += " , "
            printed +=  "*"
            print("EL HILO ES: " + hilo.name)

    print(printed + " ]")



def imprimirDatos(item1):
    print(
        f"Nombre: {item1.title}\n"
        f"id: {item1.id}\n"
        f"Hora Item: {datetime.fromtimestamp(item1.raw_timestamp, tz=timezone.utc).strftime('%Y-%m-%d_%H-%M-%S')}\n"
        f"Precio: {item1.price}\n"
        f"Marca: {item1.brand_title}\n"
        f"Foto: {item1.photo}\n"
        f"Link: {item1.url}\n"
    )    



def borrarPantalla():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')
    else:
        print("\nSistema no reconocido, comando no ejecutado...\n")



def checkParams(idle=True):

    if platform.system() not in ["Windows", "Linux"]:
        print(f"Sistema {platform.system()} no compatible, puede que el programa no funcione correctamente...\n")

    if(idle): print("\n")

    print(f"Sistema operativo: {platform.system()}"
          f"\nVersión: {platform.version()}"
          f"\nDetalles del sistema: {platform.platform()}"
          f"\nVersion de Python: {sys.version}"
          f"\n\nUsuario actual: {os.getlogin()}"
          f"\nID del proceso actual: {os.getpid()}"
          f"\nID del proceso padre: {os.getppid()}"
          f"\nUso de memoria: {psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024):.2f} MB"
          f"\n\nDirectorio actual: {os.getcwd()}"
          f"\nIPv6 Pública: {requests.get("https://api64.ipify.org?format=text").text}"
          f"\nIPv4 Pública: {requests.get("https://api4.ipify.org?format=text").text}\n\n"
    )

    if(idle):
        print(
            f" ______________________________________________\n"
            f"|                                              |\n"
            f"|          Pulse INTRO para iniciar...         |\n"
            f"|______________________________________________|\n"
        )
        input()
    else:
        print(f"Pulse INTRO para salir...\n")
        input()

    borrarPantalla()
    return



def endProgram(hilosActivos):
    print("\nSaliendo del programa... \n")
    sleep(2)
    borrarPantalla()