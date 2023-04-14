from Biblioteca import *
from Clases import *

registro = RegistroUsuarios()
login = Login(registro)

opcion = input("Ingrese 1 para registrar un usuario o 2 para iniciar sesión: ")
n=True
while n:
    match opcion:
        case "1":
            nombre = input("Ingrese su nombre: ")
            email = (input("Ingrese su email: "))
            while not validar_email(email):
                print("Email no válido.")
                email = input("Ingrese su email: ")
            email=email.lower()
            password = input("Ingrese su contraseña: ")
            codigoadmin=input("Ingrese el codigo de administrador: ")
            usuario = Usuario(nombre, email, password)
            registro.registrar_usuario(usuario)
            if validar_email(email) == 'sistema.com.ar' and codigoadmin == '1234':
                print('Bienvenido administrador')
                pass
            else:    
                print("Usuario registrado correctamente.")
        case "2":
            email = input("Ingrese su email: ")
            email=email.lower()
            password = input("Ingrese su contraseña: ")
            if login.iniciar_sesion(email, password):
                if validar_email(email)=='sistema.com.ar':
                    pass
                else:
                    print(f"Bienvenido {login.usuario_actual.nombre}")
                if input("¿Desea cerrar sesión? (s/n): ") == "s":
                    login.cerrar_sesion()
                    print("Sesión cerrada.")
                else:
                    print("Sesión no cerrada.")
            else:
                print("Email o contraseña incorrectos.")
            
        case _:
            print("Opción inválida.")

