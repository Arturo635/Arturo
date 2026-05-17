import os
import random
import string
import time

# Colores
A = "\033[1;36m"  # celeste
B = "\033[1;32m"  # verde
C = "\033[1;31m"  # rojo
D = "\033[1;33m"  # amarillo
E = "\033[0m"     # reset

FOLDER = "/storage/emulated/0/Fran"

def banner():
    print(A + r"""
███████╗██████╗  █████╗ ███╗   ██╗
██╔════╝██╔══██╗██╔══██╗████╗  ██║
█████╗  ██████╔╝███████║██╔██╗ ██║
██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║
██║     ██║  ██║██║  ██║██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
        FRAN GENERATOR
""" + E)

def crear_carpeta():
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)

def cargar_nombres(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            nombres = list(set([x.strip() for x in f.readlines() if x.strip()]))
        return nombres
    except:
        print(C + "Error al leer el archivo." + E)
        return []

def generar_combo(nombre):
    num = str(random.randint(0, 9999))
    letras = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    return f"{nombre}{num}{letras}"

def progreso(total):
    for i in range(total + 1):
        bar = "█" * int(i/2) + "-" * (50 - int(i/2))
        print(f"\r{D}[{bar}] {i*2}%", end="")
        time.sleep(0.02)
    print("\n")

def guardar(combos):
    crear_carpeta()
    file_path = os.path.join(FOLDER, "combos.txt")
    with open(file_path, "w") as f:
        for c in combos:
            f.write(c + "\n")
    print(B + f"\nGuardado en: {file_path}" + E)

def menu():
    while True:
        banner()
        print(A + "\n1. Generar combos")
        print("2. Eliminar duplicados de archivo")
        print("3. Salir" + E)

        op = input("\nOpción: ")

        if op == "1":
            ruta = input("Ruta del archivo de nombres: ")
            nombres = cargar_nombres(ruta)

            if not nombres:
                input("Enter para continuar...")
                continue

            try:
                cantidad = int(input("Cuantos combos generar: "))
            except:
                print(C + "Número inválido" + E)
                continue

            combos = []
            print(D + "\nGenerando..." + E)
            progreso(50)

            for _ in range(cantidad):
                n = random.choice(nombres)
                combos.append(generar_combo(n))

            guardar(combos)
            input("\nEnter para continuar...")

        elif op == "2":
            ruta = input("Archivo a limpiar duplicados: ")
            try:
                with open(ruta, "r") as f:
                    datos = list(set([x.strip() for x in f if x.strip()]))

                with open(ruta, "w") as f:
                    for d in datos:
                        f.write(d + "\n")

                print(B + "Duplicados eliminados." + E)
            except:
                print(C + "Error al procesar archivo." + E)

            input("\nEnter para continuar...")

        elif op == "3":
            print(C + "Saliendo..." + E)
            break
        else:
            print(C + "Opción inválida" + E)
            time.sleep(1)

if __name__ == "__main__":
    menu()