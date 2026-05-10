# OBJ: Menu interactivo
# Hice un sistema CRUD con persistencia en JSON

import json
Archivo = "usuarios.json"

# --- UTILIDADES ---
def cargar_usuarios():
    try:
        with open(Archivo, "r") as archivo:
            return json.load(archivo)
    
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def buscar_usuarios(usuarios):
    nombre_buscado = input("Nombre a buscar: ").lower().strip()
    encontrado = False

    if not nombre_buscado:
        print("Busqueda vacia")
        return
    
    for i, usuario in enumerate(usuarios, start=1):
        if nombre_buscado in usuario["nombre"].lower():
            print(f"Id: {i}. {usuario['nombre']} - {usuario['edad']} años.")
            encontrado = True

    if not encontrado:
        print("Usuario no encontrado")

# ensure_ascii=False = Guarda el texto normal: Jose
# encoding="utf-8" = permite guardar caracteres especiales
def guardar_usuarios(usuarios):
    with open (Archivo, "w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
    
# --- CRUD ---
def registrar_usuario(usuarios):
    name = input("\nNombre del usuario: ").strip().title()

    if not name:
        print("El nombre no puede estar vacío")
        return

    # Si no todas las palabras del nombre están formadas solo por letras
    if not all(palabra.isalpha() for palabra in name.split()):
        print("Nombre invalido")
        return

    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("Opcion invalida")
        return
    
    if edad < 0:
        print("Edad invalida")
        return

    for usuario in usuarios:
        if usuario["nombre"].lower() == name.lower() and usuario["edad"] == edad:
            print("Usuario ya existente (mismo nombre y edad).")
            return

    usuarios.append({"nombre": name, "edad": edad})
    print (f"Usuario registrado: {name}")
    guardar_usuarios(usuarios)

def mostrar_usuarios(usuarios):
    print("\nLISTA DE USUARIOS:")

    if not usuarios:
        print("No hay usuario registrados")
    else:
         for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario['nombre']} - {usuario['edad']} años.")
    
def editar_usuario(usuarios):
    mostrar_usuarios(usuarios)

    try:
        editar = int(input("Numero de usuario a editar: "))
    except ValueError:
        print("Opcion invalida")
        return
    
    if 1 <= editar <= len(usuarios):
        indice = editar - 1

        nuevo_nombre = input("Nuevo nombre: ").strip().title()
        
        if not nuevo_nombre:
            print("No hay usuarios registrados")
            return

        if not all(palabra.isalpha() for palabra in nuevo_nombre.split()):
            print("Nombre invalido. Solo letras y espacios.")
            return

        try:
            nuevo_edad = int(input("Nueva edad: "))
        except ValueError:
            print("Edad invalida")
            return
        
        if nuevo_edad < 0:
            print("Edad invalida")
            return
        
        for u in usuarios:
            if u["nombre"].lower() == nuevo_nombre.lower() and u["edad"] == nuevo_edad:
                print("Usuario existente") 
                return

        usuarios[indice]["nombre"] = nuevo_nombre
        usuarios[indice]["edad"] = nuevo_edad

        print("\nUSUARIO ACTUALIZADO\n")
        guardar_usuarios(usuarios)
    else:
        print("Fuera de rango")

def eliminar_usuario(usuarios):
    mostrar_usuarios(usuarios)

    try:
        eliminar = int(input("Numero de usuario a eliminar: "))
    except ValueError:
        print("Opcion invalida (Numero del usuario)")
        return

    if 1 <= eliminar <= len(usuarios):
            indice = eliminar - 1
            nombre = usuarios[indice]["nombre"]

            confirmar = input(f"¿seguro que quieres eliminar al usuario {eliminar}. {nombre}? (Si/No): ").lower()
            if confirmar != "si":
                print ("Cancelado")
                return

            usuarios.pop(indice)
            print(f"Usuario eliminado: {nombre}")
            guardar_usuarios(usuarios)

    else:
        print("Fuera de rango")
        return
    
# --- main ---  Cargar los usuarios guardados al iniciar el programa. (De la ultima vez)
def main():
    usuarios = cargar_usuarios()      
    if usuarios:
        print(f"\n\033[1mSistema iniciado.\033[0m {len(usuarios)} usuarios cargados.")
    else:
        print("\nSistema iniciado. No hay usuarios registrados.")
     
    while True:
        print("\nMENU INTERACTIVO:")
        print("1. Registrar usuario.")
        print("2. Ver usuarios.")
        print("3. Buscar usuario.")
        print("4. Editar usuario.")
        print("5. Eliminar usuario.")
        print("6. Salir")

        opcion = input("\nElige una opcion: ").lower().strip()

        if opcion in ["1", "registrar", "registrar usuarios"]:
            registrar_usuario(usuarios) 

        elif opcion in ["2", "ver", "usuarios", "ver usuarios","ver usuario"]:
            mostrar_usuarios(usuarios)

        elif opcion in ["3", "buscar", "buscar usuario"]:
            buscar_usuarios(usuarios)

        elif opcion in ["4","editar","editar usuario"]:
            editar_usuario(usuarios)

        elif opcion in ["5", "eliminar", "eliminar usuario"]:
            eliminar_usuario(usuarios)

        elif opcion in ["6", "salir"]:
            print("Saliendo..")
            break 

        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()