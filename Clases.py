class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.nombre} ({self.email})"

class RegistroUsuarios:
    def __init__(self):
        self.usuarios = []
        self.archivo = "usuarios.txt"
        self.cargar_usuarios()

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        self.guardar_usuarios()

    def guardar_usuarios(self):
        with open(self.archivo, "w") as f:
            for usuario in self.usuarios:
                f.write(f"{usuario.nombre},{usuario.email},{usuario.password}\n")

    def cargar_usuarios(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    nombre, email, password = linea.strip().split(",")
                    self.usuarios.append(Usuario(nombre, email, password))
        except FileNotFoundError:
            pass

class Login:
    def __init__(self, registro_usuarios):
        self.registro_usuarios = registro_usuarios
        self.usuario_actual = None

    def iniciar_sesion(self, email, password):
        for usuario in self.registro_usuarios.usuarios:
            if usuario.email == email and usuario.password == password:
                self.usuario_actual = usuario
                return True
        return False

    def cerrar_sesion(self):
        self.usuario_actual = None

class Vehiculo:
    def __init__(self, modelo, marca, autonomia, uso, precio):
        self.modelo = modelo
        self.marca = marca
        self.autonomia = autonomia
        self.uso = uso
        self.precio = precio
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Autonomia: {self.autonomia}, Uso: {self.uso}, Precio: {self.precio}"

class Utilitario(Vehiculo):
    def __init__(self, marca, modelo, autonomia, uso, precio, carga_maxima):
        super().__init__(modelo, marca, autonomia, uso, precio)
        self.carga_maxima = carga_maxima
    def __str__(self):
        return super().__str__() + f", Carga máxima: {self.carga_maxima}"
        
class Deportivo(Vehiculo):
    def __init__(self, marca, modelo, autonomia, uso, precio, velocidad_maxima):
        super().__init__(modelo, marca, autonomia, uso, precio)
        self.velocidad_maxima = velocidad_maxima
    def __str__(self):
        return super().__str__() + f", Velocidad máxima: {self.velocidad_maxima}"
        
class Electrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia, uso, precio, tiempo_carga):
        super().__init__(modelo, marca, autonomia, uso, precio)
        self.tiempo_carga = tiempo_carga
    def __str__(self):
        return super().__str__() + f", Tiempo de carga: {self.tiempo_carga}"
        
class Van(Vehiculo):
    def __init__(self, marca, modelo, autonomia, uso, precio, asientos):
        super().__init__(modelo, marca, autonomia, uso, precio)
        self.asientos = asientos
    def __str__(self):
        return super().__str__() + f", Asientos: {self.asientos}"
        
class Compacto(Vehiculo):
    def __init__(self, marca, modelo, autonomia, uso, precio, tamaño_baul):
        super().__init__(modelo, marca, autonomia, uso, precio)
        self.tamaño_baul = tamaño_baul
    def __str__(self):
        return super().__str__() + f", Tamaño del baul: {self.tamaño_baul}"
    

class Nodo:
    def __init__(self, vehiculo):
        self.vehiculo = vehiculo
        self.siguiente = None

class Stock(Nodo):
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, vehiculo):
        nuevo_nodo = Nodo(vehiculo)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def eliminar(self, vehiculo):
        if self.cabeza is None:
            return
        if self.cabeza.vehiculo == vehiculo:
            self.cabeza = self.cabeza.siguiente
            del vehiculo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                if actual.siguiente.vehiculo == vehiculo:
                    actual.siguiente = actual.siguiente.siguiente
                    del vehiculo
                    return
                actual = actual.siguiente
    
    def __str__(self):
        if self.cabeza is None:
            return "La lista está vacía"
        else:
            actual = self.cabeza
            resultado = str(actual.vehiculo)
            while actual.siguiente is not None:
                actual = actual.siguiente
                resultado += f"\n{str(actual.vehiculo)}"
            return resultado
