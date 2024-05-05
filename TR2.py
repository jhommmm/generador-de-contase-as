import random
import string
from datetime import datetime
import webbrowser

def generar_contrasena(longitud, nivel):
    caracteres = string.digits + string.ascii_lowercase
    if nivel >= 2:
        caracteres += string.ascii_uppercase
    if nivel >= 3:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def guardar_contrasena(contrasena):
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    respuesta = input("¿Quieres guardar la contraseña? (si o no): ")
    if respuesta.lower() == "si":
        with open("contrasenas.txt", "a") as archivo:
            archivo.write(f"{contrasena} - {fecha_hora_actual}\n")
        print("Contraseña guardada correctamente en 'contrasenas.txt'.")
    else:
        print("Contraseña no guardada.")

def ver_contraseñas_guardadas():
    try:
        with open("contrasenas.txt", "r") as archivo:
            contenido = archivo.read()
            print("Contraseñas guardadas:")
            print(contenido)
    except FileNotFoundError:
        print("No hay contraseñas guardadas.")

def informacion_personal():
    print("Información innecesaria sobre el estudiante:")
    print("Whatsapp -----  https://wa.me/+51935035125?text=Hola%20podemos%20hablar?%20")
    print("Github ----- https://github.com/jhommmm")
    print("Youtube ----- https://www.youtube.com/@jhommjhomm4054/videos")
    abrir_enlaces()

def abrir_enlaces():
    enlaces = [
        "https://wa.me/+51935035125?text=Hola%20podemos%20hablar?%20",
        "https://github.com/jhommmm",
        "https://www.youtube.com/@jhommjhomm4054/videos"
    ]
    for enlace in enlaces:
        webbrowser.open(enlace)

def menu_principal():
    print("*************************************************")
    print("Alumno: JHONCARO JAMIE QUINCHO GALINDO")
    print("ID: 1480457")
    print("Direccion zonal: LUIS CACERES GRAZIANI")
    print("Docente: JHONATAN ANTONIO URQUIA MUSAYON")
    print("Carrera: INGENIERIA EN CIBERSEGURIDAD")
    print("Centro de estudios: SENATI")
    print("Semestre: IV")
    print("*************************************************")

    while True:
        print("\nMenú Principal:")
        print("1) Generar una nueva contraseña")
        print("2) Ver contraseñas guardadas")
        print("3) Información innecesaria sobre el estudiante")
        print("4) Salir del programa")

        opcion = obtener_entero_validado("Seleccione una opción (1-4): ", "Por favor, ingrese un número válido.")

        if opcion == 1:
            generar_contrasena_submenu()
        elif opcion == 2:
            ver_contraseñas_guardadas()
        elif opcion == 3:
            informacion_personal()
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo nuevamente.")

def generar_contrasena_submenu():
    print("\nGenerador de Contraseñas")
    longitud = obtener_entero_validado("Ingrese la cantidad de caracteres para la contraseña: ", "La longitud debe ser un número entero positivo.")
    print("\nNiveles de Seguridad:")
    print("1) Solo números y letras minúsculas")
    print("2) Números, letras mayúsculas y minúsculas")
    print("3) Números, letras mayúsculas y minúsculas, y caracteres especiales")
    nivel = obtener_nivel_validado("Seleccione un nivel de seguridad (1-3): ")

    contrasena_generada = generar_contrasena(longitud, nivel)
    print(f"\nContraseña generada: {contrasena_generada}")

    guardar_contrasena(contrasena_generada)

def obtener_entero_validado(mensaje, mensaje_error):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            print(mensaje_error)

def obtener_nivel_validado(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 1 or valor > 3:
                raise ValueError
            return valor
        except ValueError:
            print("El nivel de seguridad debe ser un número entre 1 y 3.")

if __name__ == "__main__":
    menu_principal()
