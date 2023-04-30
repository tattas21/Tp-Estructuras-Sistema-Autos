from Clases import *
from datetime import *
from random import *
# validaciones
def lista_a_lista_listaentrelazada(lista, Nodo):
    if not lista:
        return None
    head = Nodo(lista[0])
    current = head
    for i in range(1, len(lista)):
        current.next = Nodo(lista[i])
        current = current.next
    return head



def validar_email(email):
    partes = email.split('@')
    if len(partes) != 2:
        return False
    usuario = partes[0]
    dominio = partes[1]
    if not usuario or not dominio:
        return False
    if '.' not in dominio:
        return False
    if usuario[-1] == '.':
        return False
    if '..' in usuario or '..' in dominio:
        return False
    if dominio == 'sistema.com.ar':
        return dominio
    return True

def validar_password(password):
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.isalpha() for c in password):
        return False
    return True

def validar_nombre(nombre):
    if  any(c.isdigit() for c in nombre):
        return False
    return True

def descargar_stock(nombre_archivo):
    lista_entrelazada = Stock()
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            vehiculo=None
            for linea in lineas:
                campos = linea.strip().split(",")
                if campos[0] == "utilitario":
                    vehiculo = Utilitario(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                elif campos[0] == "deportivo":
                    vehiculo = Deportivo(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                elif campos[0] == "elictrico":
                    vehiculo = Electrico(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                elif campos[0] == "van":
                    vehiculo = Van(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                elif campos[0] == "compacto":
                    vehiculo = Compacto(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))

                lista_entrelazada.agregar(vehiculo)
            archivo.close()

    except FileNotFoundError:
        print("El archivo no existe")
    return lista_entrelazada

def guardar_stock(nombre_archivo, lista_entrelazada):
    with open(nombre_archivo, "w") as archivo:
        if lista_entrelazada.cabeza is not None:
            actual = lista_entrelazada.cabeza
            tipo= None
            datos=None
            while actual is not None:
                if isinstance(actual.vehiculo, Utilitario):
                    tipo = "utilitario"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.carga_maxima},{actual.vehiculo.id}\n"
                elif isinstance(actual.vehiculo, Deportivo):
                    tipo = "deportivo"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.velocidad_maxima},{actual.vehiculo.id}\n"
                elif isinstance(actual.vehiculo, Electrico):
                    tipo = "elictrico"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.tiempo_carga},{actual.vehiculo.id}\n"
                elif isinstance(actual.vehiculo, Van):
                    tipo = "van"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso}, {actual.vehiculo.asientos},{actual.vehiculo.id}\n"
                elif isinstance(actual.vehiculo, Compacto):
                    tipo = "Compacto"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.tamaño_baul},{actual.vehiculo.id}\n"
                archivo.write(f"{tipo},{datos}")
                actual = actual.siguiente
    archivo.close()
    print(f"Stock guardado en el archivo {nombre_archivo}")

def agregar_vehiculo_tipo(n, lista_entrelazada):
        try:
            i = lista_entrelazada.ultimo_nodo().vehiculo.id
            i = i.split("_")[1]
            i=int(i) + 1
            i = str(i)
        except AttributeError:
            i = 0
            i = str(i)
        tipo= input("Ingrese el tipo de vehículo que desea agregar: ")
        tipo=tipo.lower()
        match tipo:
            case "utilitario":
                marca= input("Ingrese la marca del vehículo: ")
                modelo= input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                nuevo_auto = Utilitario(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: ").lower(),int(input("Ingrese la carga máxima del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case "deportivo":
                marca= input("Ingrese la marca del vehículo: ")
                modelo= input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].lower()+ "_" + i
                nuevo_auto = Deportivo(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: ").lower(), int(input("Ingrese la velocidad máxima del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case "electrico":
                marca= input("Ingrese la marca del vehículo: ")
                modelo= input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                nuevo_auto = Electrico(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el tiempo de carga del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case "van":
                marca= input("Ingrese la marca del vehículo: ")
                modelo= input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                nuevo_auto = Van(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese la cantidad de asientos del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case "compacto":
                marca= input("Ingrese la marca del vehículo: ")
                modelo= input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                nuevo_auto = Compacto(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el tamaño del baul del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case _:
                print("Tipo de vehículo no válido")
                n=True
                return n

def eliminar_vehiculo(lista_entrelazada):
    lista=lista_entrelazada.list()
    print(lista)
    n=False
    while n==False:
        marca=input("Ingrese la marca del vehículo que desea eliminar: ")
        modelo=input("Ingrese el modelo del vehículo que desea eliminar: ")
        for i in lista:
            if i.marca==marca and i.modelo==modelo:
                lista_entrelazada.eliminar(i)
                print(f"Se eliminó el vehículo {str(i)} del stock")
                n=True
            else:
                print("Vehículo no encontrado")
                n=True
def modificar_dato_vehiculo(lista_entrelazada):
    lista=lista_entrelazada.list()
    print("Stock de vehículos:")
    print(lista_entrelazada)
    n=False
    while n==False:
        id = input("Ingrese el id del vehículo que desea modificar: ")
        for i in lista:
            if i.id == id:
                print(f"Vehículo encontrado: {str(i)}")
                n=True
                m=False
                while m==False:
                    dato=input("Ingrese el dato que desea modificar: ")
                    dato=dato.lower()
                    match dato:
                        case "marca":
                            i.marca=input("Ingrese la nueva marca: ")
                            m=True
                        case "modelo":
                            i.modelo=input("Ingrese el nuevo modelo: ")
                            m=True
                        case "precio":
                            i.precio=int(input("Ingrese el nuevo precio: "))
                            m=True
                        case "autonomia":
                            i.autonomia=int(input("Ingrese la nueva autonomía: "))
                            m=True
                        case "uso":
                            i.uso=input("Ingrese el nuevo uso: ")
                            m=True
                        case "carga":
                            i.carga=int(input("Ingrese la nueva carga: "))
                            m=True
                        case "velocidad":
                            i.velocidad=int(input("Ingrese la nueva velocidad: "))
                            m=True
                        case "asientos":
                            i.asientos=int(input("Ingrese la nueva cantidad de asientos: "))
                            m=True
                        case "tamaño":
                            i.tamaño=int(input("Ingrese el nuevo tamaño: "))
                            m=True
                        case _:
                            print("Dato no válido")
                            m=True
                    print(f"Se modificó el vehículo {str(i)}")
            else:
                print("Vehículo no encontrado")
                n=True

def buscar_vehiculo(lista_vehiculos, marca=None, modelo=None, precio=None, autonomia=None, uso=None):
    lista_vehiculos = lista_vehiculos.list()
    n = False
    while n==False:
        print("Filtros disponibles: marca\n modelo\n precio\n autonomia\n uso\n nota: si no desea utilizar un filtro, ingrese 'no'")
        filtro=input("Ingrese el filtro que desea utilizar: ")
        
        filtro=filtro.lower()
        match filtro:
            case "marca":
                marca=input("Ingrese la marca que desea buscar: ")
            case "modelo":
                modelo=input("Ingrese el modelo que desea buscar: ")
            case "uso":
                uso=input("Ingrese el uso que desea buscar: ")
            case "precio":
                precio=int(input("Ingrese el precio que desea buscar: "))
            case "autonomia":
                autonomia=int(input("Ingrese la autonomía que desea buscar: "))
            case "no":
                n=True
            case _:
                print("Filtro no válido")    
        for vehiculo in lista_vehiculos:
            if marca is not None and vehiculo.marca != marca:
                lista_vehiculos.remove(vehiculo)
            if modelo is not None and vehiculo.modelo != modelo:
                lista_vehiculos.remove(vehiculo)
            if precio is not None and vehiculo.precio > precio:
                lista_vehiculos.remove(vehiculo)
            if autonomia is not None and vehiculo.autonomia < autonomia:
                lista_vehiculos.remove(vehiculo)
            if uso is not None and vehiculo.uso != uso:
                lista_vehiculos.remove(vehiculo)
            
        m=(input("Desea agregar otro filtro? (s/n): "))
        m=m.lower()
        if m=="s":
            n=False
        else: 
            n=True
    print("Vehículos encontrados:")
    for vehiculo in lista_vehiculos:
        print(vehiculo)
    return (lista_vehiculos)

def comprar_vehiculo(vehiculos_filtrados, lista, usuario):
    n=False
    archivo=open("ventas.txt", "a")
    fecha_hora = datetime.now()
    while n==False:
        marca_vehiculo=input("Ingrese la marca del vehículo que desea comprar: ")
        modelo_vehiculo=input("Ingrese el modelo del vehículo que desea comprar: ")
        vehiculo_comprado = None
        for i in vehiculos_filtrados:
            if i.marca==marca_vehiculo and i.modelo==modelo_vehiculo:
                print("Detalle de la compra:")
                print(f"Vehículo: {marca_vehiculo} {modelo_vehiculo}")
                print(f"Precio: ${i.precio}")
                print(f"Transferir ${i.precio} a la siguiente cuenta:")
                print("Nombre del banco: HSBC")
                print("CBU: 0873776281914709007725")
                print("CUIT: 30-12345678-2")
                print("Razon social: ITBA CAR S.R.L")
                print("Mail: ventas@itbacar.org.ar")
                print("Cuenta: CC U$S 105-435261/0 ")
                print(f"Fecha y hora de la compra: {fecha_hora}")
                m = False
                b = True
                while m == False:
                    confirmacion = input("¿Confirma que ha realizado la transferencia? (s/n) ")
                    confirmacion = confirmacion.lower()
                    if confirmacion == "s":
                        print("Compra realizada con éxito")
                        m = True
                        listaventas = [usuario.email, fecha_hora]
                        continue
                    elif confirmacion == "n":
                        print("Compra cancelada")
                        m = True
                        b = False
                        n = True
                    else:
                        print("Opción no válida")
                # nuevo
                while b == True:
                    print(f"Se compró el vehículo {marca_vehiculo} {modelo_vehiculo}")
                    actual = lista.cabeza 
                    while actual is not None:
                        if str(actual.vehiculo.marca) == marca_vehiculo and str(actual.vehiculo.modelo) == modelo_vehiculo:
                            vehiculo_comprado = actual.vehiculo
                            id = vehiculo_comprado.id
                            lista.eliminar(id)
                            dato = f"{usuario.email},{fecha_hora},{vehiculo_comprado.marca},{vehiculo_comprado.modelo},{vehiculo_comprado.precio}\n"
                            archivo.write(f'{dato}')
                            archivo.close()
                            break
                        actual = actual.siguiente
                    guardar_stock("stock.txt",lista)
                    n=True
                    b=False
            else:
                print("Vehículo no encontrado")
                n=True

    return vehiculos_filtrados

def descargar_lista_ventas(nombre_archivo, usuario_actual):
    lista_entrelazada = Stock()
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            compra = None
            contador = 0
            total = 0
            for linea in lineas:
                campos = linea.strip().split(",")
                if campos[0] == usuario_actual.email:
                    compra = (f"Mail: {campos[0]}, Fecha: {campos[1]}, Marca: {campos[2]}, Modelo: {campos[3]}, Precio: ${campos[4]}")
                    contador += 1
                    total += int(campos[4])
                    lista_entrelazada.agregar(compra)   
            print(f"Usted ha realizado {contador} compra/s")
            print(f"El total gastado es de ${total}")
            print("Detalle de las compras:")
            print(lista_entrelazada)
            archivo.close()
    except:
        print("No ha realizado ninguna compra")
    
def modificar_datos(lista, usuario):
    registro=RegistroUsuarios()
    n=False
    while n==False:
        dato=input("Ingrese el dato que desea modificar: ")
        dato=dato.lower()
        match dato:
            case "nombre":
                
                usuario.nombre=input("Ingrese el nuevo nombre: ")
                n=True
            case "email":
                usuario.email=input("Ingrese el nuevo email: ")
                n=True
            case "contraseña":
                usuario.contraseña=input("Ingrese la nueva contraseña: ")
                n=True
            case _:
                print("Dato no válido")
                n=True
    registro.cargar_usuarios(usuario)

def saque_todos_int(string):
    id = ""
    for i in string:
        try:
            int(i)
            id += i
        except:
            if i == "_":
                id = id[::-1]
                return id 
            pass

def descargar_stock_cliente(nombre_archivo):
    lista_entrelazada = Stock()
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            vehiculo=None
            for linea in lineas:
                campos = linea.strip().split(",")
                if campos[0] == "utilitario":
                    vehiculo = Utilitario(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                elif campos[0] == "deportivo":
                    vehiculo = Deportivo(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                elif campos[0] == "elictrico":
                    vehiculo = Electrico(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                elif campos[0] == "van":
                    vehiculo = Van(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                elif campos[0] == "compacto":
                    vehiculo = Compacto(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                lista_entrelazada.agregar(vehiculo)
                
            archivo.close()

    except FileNotFoundError:
        print("El archivo no existe")
    return lista_entrelazada

def descargar_lista_ventas_estadisticas(nombre_archivo):
    lista_entrelazada = Stock()
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            compra = None
            recaudacion = 0
            contador = 0
            for linea in lineas:
                campos = linea.strip().split(",")
                compra = (f"Mail: {campos[0]}, Fecha: {campos[1]}, Marca: {campos[2]}, Modelo: {campos[3]}, Precio: ${campos[4]}")
                lista_entrelazada.agregar(compra)
                recaudacion += int(campos[4])
                contador += 1
        print(f"Se han realizado {contador} venta/s")
        print(f"La facturación total es de: ${recaudacion}")
        print("Detalle de las ventas:")
        print(lista_entrelazada)
    except:
        print("No ha realizado ninguna compra")