# escribir en archivo
print("=== 1. Escribir en archivo ===")
archivo = open("datos.txt", "w")
archivo.write("Línea 1: Bienvenido al sistema educacional\n")
archivo.write("Línea 2: Alumno: Juan Pérez\n")
archivo.write("Línea 3: Asignatura: Matemáticas\n")
print(f"Nombre : {archivo.name}")
print(f"Modo   : {archivo.mode}")
print(f"Cerrado: {archivo.closed}")
archivo.close()
print(f"Cerrado: {archivo.closed}")


# leer datos en txt
print("\n=== 2. Leer archivo completo ===")
with open("datos.txt", "r") as f:
    contenido = f.read()
    print(contenido)


# leer archivo pero linea por linea
print("=== 3. Leer línea por línea ===")
with open("datos.txt", "r") as f:
    primera = f.readline()
    print(f"Primera línea: {primera}")
    print("Resto del archivo:")
    for linea in f:
        print(linea, end="")


# añadir con .append()
print("\n\n=== 4. Modo append ===")
with open("datos.txt", "a") as f:
    f.write("Línea 4: Nota agregada con append\n")
print("Línea agregada. Verificando contenido:")
with open("datos.txt", "r") as f:
    print(f.read())


# detalles de atributos del archivo guardado
print("=== 5. Atributos del archivo ===")
f = open("datos.txt", "r")
print(f"Nombre : {f.name}")
print(f"Modo   : {f.mode}")
print(f"Cerrado: {f.closed}")
f.close()
print(f"Cerrado: {f.closed}")
