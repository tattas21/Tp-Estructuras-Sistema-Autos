from Clases import *

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

def cargar_stock(nombre_archivo):
    lista_entrelazada = Stock()
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            vehiculo=1
            for linea in lineas:
                campos = linea.strip().split(",")
                if campos[0] == "utilitario":
                    vehiculo = Utilitario(campos[1], campos[2], int(campos[3]), campos[4], int(campos[5]), int(campos[6]))
                elif campos[0] == "deportivo":
                    vehiculo = Deportivo(campos[1], campos[2], int(campos[3]), campos[4], int(campos[5]), int(campos[6]))
                elif campos[0] == "elictrico":
                    vehiculo = Electrico(campos[1], campos[2], int(campos[3]), campos[4], int(campos[5]), int(campos[6]))
                elif campos[0] == "van":
                    vehiculo = Van(campos[1], campos[2], int(campos[3]), campos[4], int(campos[5]), int(campos[6]))
                elif campos[0] == "compacto":
                    vehiculo = Compacto(campos[1], campos[2], int(campos[3]), campos[4], int(campos[5]), int(campos[6]))

                lista_entrelazada.agregar(vehiculo)
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
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.precio},{actual.vehiculo.carga_maxima}\n"
                elif isinstance(actual.vehiculo, Deportivo):
                    tipo = "deportivo"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.precio},{actual.vehiculo.velocidad_maxima}\n"
                elif isinstance(actual.vehiculo, Electrico):
                    tipo = "elictrico"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.precio},{actual.vehiculo.tiempo_carga}\n"
                elif isinstance(actual.vehiculo, Van):
                    tipo = "van"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.precio},{actual.vehiculo.asientos}\n"
                elif isinstance(actual.vehiculo, Compacto):
                    tipo = "Compacto"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.precio},{actual.vehiculo.tamaño_baul}\n"
                archivo.write(f"{tipo},{datos}")
                actual = actual.siguiente
    print(f"Stock guardado en el archivo {nombre_archivo}")

def agregar_vehiculo_tipo(n, lista_entrelazada):
        tipo= input("Ingrese el tipo de vehículo que desea agregar: ")
        tipo=tipo.lower()
        match tipo:
            case "utilitario":
                nuevo_auto = Utilitario(input("Ingrese la marca del vehículo: "), input("Ingrese el modelo del vehículo: "), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la carga máxima del vehículo: ")))
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                return n
            case "deportivo":
                nuevo_auto = Deportivo(input("Ingrese la marca del vehículo: "), input("Ingrese el modelo del vehículo: "), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la velocidad máxima del vehículo: ")))
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                return n
            case "electrico":
                nuevo_auto = Electrico(input("Ingrese la marca del vehículo: "), input("Ingrese el modelo del vehículo: "), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese el tiempo de carga del vehículo: ")))
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                return n
            case "van":
                nuevo_auto = Van(input("Ingrese la marca del vehículo: "), input("Ingrese el modelo del vehículo: "), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la cantidad de asientos del vehículo: ")))
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                return n
            case "compacto":
                nuevo_auto = Compacto(input("Ingrese la marca del vehículo: "), input("Ingrese el modelo del vehículo: "), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese el tamaño del baul del vehículo: ")))
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                return n
            case _:
                print("Tipo de vehículo no válido")
                n=True
                return n