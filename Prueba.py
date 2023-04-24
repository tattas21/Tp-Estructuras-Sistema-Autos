from Biblioteca import *
from Clases import *
from datetime import *

print(datetime.now())


# Cargar el stock de vehículos del archivo "stock.txt"
nombre_archivo = "stock.txt"
lista_entrelazada = descargar_stock(nombre_archivo)

# Agregar un nuevo vehículo
n=True
while n==True:
    agregar_vehiculo_tipo(n, lista_entrelazada)
    if input("¿Desea agregar otro vehículo? (s/n): ") == "s":
        n=True
    else:
        n=False

# Mostrar el stock de vehículos actualizado
print("Stock actualizado:")
print(lista_entrelazada)

# Guardar el stock de vehículos en el archivo "stock.txt"
guardar_stock(nombre_archivo, lista_entrelazada)

#filtro
print(filtro(lista_entrelazada.vehiculo))


# Pedir el nombre de un vehículo para comprar
marca_vehiculo_comprado = input("Ingrese la marca del vehículo que desea comprar: ")
modelo_vehiculo_comprado = input("Ingrese el modelo del vehículo que desea comprar: ")
vehiculo_comprado = None
actual = lista_entrelazada.cabeza 
while actual is not None:
    print(str(actual))
    if str(actual.vehiculo.marca) == marca_vehiculo_comprado and str(actual.vehiculo.modelo) == modelo_vehiculo_comprado:
        vehiculo_comprado = actual.vehiculo
        lista_entrelazada.eliminar(vehiculo_comprado)
        print(f"Se compró el vehículo {marca_vehiculo_comprado}' '{modelo_vehiculo_comprado}")
        break
    actual = actual.siguiente
if vehiculo_comprado is None:
    print(f"No se encontró el vehículo {marca_vehiculo_comprado}' '{modelo_vehiculo_comprado} en el stock")
else:
    # Mostrar el vehículo comprado y su precio
    print("Detalle del vehículo comprado:")
    print(vehiculo_comprado)
    print(f"Precio: {vehiculo_comprado.precio}")

    # Guardar el stock de vehículos en el archivo "stock.txt"
    guardar_stock(nombre_archivo, lista_entrelazada)

