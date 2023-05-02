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
                    salir = input("¿Desea salir del programa? (s/n): ")
                    salir = salir.lower()
                    if salir == "s":
                        exit()
                        
                    else:
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
                            # Funciona
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
                            # funciona
                            case "2":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                print(lista_entrelazada)
                                id = input("Ingrese el id del vehiculo a eliminar: ")
                                lista_entrelazada.eliminar(id)
                                print("-------------------------------- Stock actualizado --------------------------------")
                                print(lista_entrelazada)
                                guardar_stock(nombre_archivo, lista_entrelazada)
                            # Funciona
                            case "3":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                modificar_dato_vehiculo(lista_entrelazada)
                                guardar_stock(nombre_archivo, lista_entrelazada)
                            # Funciona
                            case "4":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                print(lista_entrelazada)
                            # Ver como implementar bien mathplotlib
                            case "5":
                                nombre_archivo = "ventas.txt"
                                descargar_lista_ventas_estadisticas(nombre_archivo)

                            # si esto no funciona estamo mal
                            case "6":
                                print("Gracias por usar el sistema.")
                                s = False
                            case _:
                                print("Opción inválida.")
                    else:
                        print(f'Bienvenido {usuario_actual.nombre}')
                        print('1. Ver stock')
                        print('2. Comprar vehiculo')
                        print('3. Ver mis compras')
                        print('4. Modificar mis datos')
                        print('5. Cerrar sesion')
                        opcion = input("Ingrese una opción (el numero): ")
                        match opcion:
                            # Funciona
                            case "1":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock_cliente(nombre_archivo)
                                print(lista_entrelazada)
                            # funciona?
                            case "2":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                comprar_vehiculo(buscar_vehiculo(lista_entrelazada), lista_entrelazada, usuario_actual)
                            # si, puede mejorar
                            case "3":
                                nombre_archivo = "ventas.txt"
                                lista = descargar_lista_ventas(nombre_archivo, usuario_actual)
                            # casiquesi
                            case "4":
                                nombre_archivo = "usuarios.txt"
                                lista_entrelazada = ListaEnlazada()
                                try:
                                    with open(nombre_archivo, "r") as archivo:
                                        lineas = archivo.readlines()
                                        for linea in lineas:
                                            campos = linea.strip().split(",")
                                            lista_entrelazada.agregar(campos)
                                    archivo.close()
                                except FileNotFoundError:
                                    print("No se encontró el archivo.")
                                lista_entrelazada = lista_entrelazada.list()
                                print("1. Modificar nombre")
                                print("2. Modificar contraseña")
                                opcion = input("Ingrese una opción (el numero): ")
                                match opcion:
                                    case "1":
                                        nombre = input("Ingrese nueva nombre: ")
                                        for i in range(len(lista_entrelazada)):
                                            if lista_entrelazada[i][1] == usuario_actual.email:
                                                lista_entrelazada[i][0] = nombre
                                    case "2":
                                        password = input("Ingrese su nueva contraseña: ")
                                        while not validar_password(password):
                                            print("Contraseña no válida.")
                                            password = input("Ingrese su contraseña: ")
                                        for i in range(len(lista_entrelazada)):
                                            if lista_entrelazada[i][1] == usuario_actual.email:
                                                lista_entrelazada[i][2] = password
                                    case _:
                                        print("Opción inválida.")
                                with open(nombre_archivo, "w") as archivo:
                                    for i in range(len(lista_entrelazada)): 
                                        archivo.write(f"{lista_entrelazada[i][0]},{lista_entrelazada[i][1]},{lista_entrelazada[i][2]}\n")
                                archivo.close()



                            
                            case "5":
                                print("Gracias por usar el sistema.")
                                s = False
                            case _:
                                print("Opción inválida.")
                                                        
        case "3":
            print("Gracias por usar el sistema.")
            exit()
        case _:
            print("Opción inválida.")


