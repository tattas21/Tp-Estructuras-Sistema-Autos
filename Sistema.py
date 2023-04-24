from Biblioteca import *
from Clases import *

registro = RegistroUsuarios()
login = Login(registro)
usuario_actual = None

while True:
    print("1. Registro")
    print("2. Inicio de sesión")
    print("3. Salir")
    opcion = input("Ingrese una opción (el numero): ")
    match opcion:
        # Agregar validaciones
        case "1":
            nombre = input("Ingrese su nombre: ")
            while validar_nombre(nombre) == False:
                print("Nombre no válido.")
                nombre = input("Ingrese su nombre: ")
            email = (input("Ingrese su email: "))
            while not validar_email(email) or registro.buscar_usuario(email) == False:
                print("Email no válido.")
                email = input("Ingrese su email: ")
            email=email.lower()
            password = input("Ingrese su contraseña: ")
            while not validar_password(password):
                print("Contraseña no válida.")
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
            es_admin=False
            n = True
            while n == True:
                if login.iniciar_sesion(email, password):
                    if validar_email(email)=='sistema.com.ar':
                        es_admin=True
                        print(f"Bienvenido {login.usuario_actual.nombre}")
                        usuario_actual = login.usuario_actual
                        n = False
                    else:
                        print(f"Bienvenido {login.usuario_actual.nombre}")
                        usuario_actual = login.usuario_actual
                        n = False
                else:
                    print("Email o contraseña incorrectos.")
                    email = input("Ingrese su email: ")
                    email=email.lower()
                    password = input("Ingrese su contraseña: ")
                    n = True
            s = True
            while s == True:
                if usuario_actual is not None:
                    if es_admin:
                        print('1. Agregar vehiculo')
                        print('2. Eliminar vehiculo')
                        print('3. Modificar vehiculo')
                        print('4. ver stcok')
                        print('5. ver ventas')
                        print('6. cerrar sesion')
                        opcion = input("Ingrese una opción (el numero): ")
                        match opcion:
                            # Funciona, me gustaria agregar un id para cada vehiculo facilitaria mucho la busqueda
                            case "1":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                n=True
                                while n==True:
                                    agregar_vehiculo_tipo(n, lista_entrelazada)

                                    if input("¿Desea agregar otro vehículo? (s/n): ") == "s":
                                        n=True
                                    else:
                                        n=False
                                guardar_stock(nombre_archivo, lista_entrelazada)
                            # seguir trabajando en esta opcion  
                            case "2":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                lista_entrelazada.eliminar()
                                guardar_stock(nombre_archivo, lista_entrelazada)
                            # seguir trabajando en esta opcion
                            case "3":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                modificar_vehiculo(lista_entrelazada)
                            # funciona
                            case "4":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                print(lista_entrelazada)
                            # ver como implementar bien mathplotlib
                            case "5":
                                nombre_archivo = "ventas.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                print(lista_entrelazada)
                            # si esto no funciona estamo mal
                            case "6":
                                print("Gracias por usar el sistema.")
                                s = False
                            case _:
                                print("Opción inválida.")
                    else:
                        print('1. Ver stock')
                        print('2. Comprar vehiculo')
                        print('3. Ver mis compras')
                        print('4. Modificar mis datos')
                        print('5. Cerrar sesion')
                        opcion = input("Ingrese una opción (el numero): ")
                        match opcion:
                            # funciona
                            case "1":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                print(lista_entrelazada)
                            # funciona?
                            case "2":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                comprar_vehiculo(buscar_vehiculo(lista_entrelazada), lista_entrelazada, usuario_actual)
                            # ver
                            case "3":
                                nombre_archivo = "ventas.txt"
                                lista = descargar_lista_ventas(nombre_archivo)
                                for i in lista:
                                    print(i)
                                    if i[0] == usuario_actual.email:
                                        print(i)
                            
                            case "4":
                                print(usuario_actual)
                                nombre_archivo = "usuarios.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                modificar_datos(lista_entrelazada, usuario_actual)
                            


                            
        case "3":
            print("Gracias por usar el sistema.")
            break
        case _:
            print("Opción inválida.")

