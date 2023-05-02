#Clases Usuarios
# clase usuario general de esta se hereda administrador y cliente
class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.nombre} ({self.email})"

class cliente(Usuario):
    def __init__(self,nombre,email,password):
        super().__init__(nombre,email,password)
        self.compras=[]
    def registro_compras(self):
        self.compras.append(self.compras)
        with open(f'{self.email}.txt', 'a') as f:
            f.write(f'{self.tipo},{self.marca},{self.modelo},{self.precio}\n')
        f.close()

    def __str__(self):
        return super().__str__() + f", Compras: {self.compras}"

class administrador(Usuario):
    def __init__(self,nombre,email,password, es_admin):
        super().__init__(nombre,email,password)
        self.es_admin = None
    def es_administrador(self):
        if self.email == 'sistema.com.ar':
            self.es_admin = True
            return self.es_admin 
        else:
            self.es_admin = False
            return self.es_admin 
    def __str__(self):
        return super().__str__() + f", Ventas: {self.ventas}"


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
        f.close()

    def cargar_usuarios(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    nombre, email, password = linea.strip().split(",")
                    self.usuarios.append(Usuario(nombre, email, password))
            f.close()
        except FileNotFoundError:
            pass
    def buscar_usuario(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                print(f"El usuario {usuario.email} ya existe")
                return False
        return None
# Ver opcion sin clase
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

class cliente(Usuario):
    def __init__(self,nombre,email,password):
        super().__init__(nombre,email,password)
        self.compras=[self.email]
    def agregar_compra(self,compra):
        self.compras.append(compra)
    def guardar_compras(self):
        with open("compras.txt", "w") as f:
            for compra in self.compras:
                f.write(f"{compra}\n")
        f.close()
    def descargar_compras(self):
        try:
            with open("compras.txt", "r") as f:
                for linea in f:
                    self.compras.append(linea.strip())
            f.close()
        except FileNotFoundError:
            pass
    def __str__(self):
        return super().__str__() + f", Compras: {self.compras}"

class administrador(Usuario):
    def __init__(self,nombre,email,password):
        super().__init__(nombre,email,password)
    


    def __str__(self):
        return super().__str__() + f", Ventas: {self.ventas}"

class Vehiculo:
    def __init__(self, modelo, marca, precio,  autonomia, uso, id):
        self.modelo = modelo
        self.marca = marca
        self.precio = precio
        self.autonomia = autonomia
        self.uso = uso
        self.id = id
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: {self.precio},Autonomia: {self.autonomia}, Uso: {self.uso}"

class Utilitario(Vehiculo):
    def __init__(self, marca, modelo, precio, autonomia, uso, carga_maxima, id):
        super().__init__(modelo, marca, precio,autonomia, uso, id)
        self.carga_maxima = carga_maxima
    def __str__(self):
        return super().__str__() + f", Carga máxima: {self.carga_maxima}, ID: {self.id}"
        
class Deportivo(Vehiculo):
    def __init__(self, marca, modelo, precio, autonomia, uso, velocidad_maxima, id):
        super().__init__(modelo, marca, precio,autonomia, uso, id)
        self.velocidad_maxima = velocidad_maxima
    def __str__(self):
        return super().__str__() + f", Velocidad máxima: {self.velocidad_maxima}, ID: {self.id}"
        
class Electrico(Vehiculo):
    def __init__(self, marca, modelo, precio,autonomia, uso, tiempo_carga, id):
        super().__init__(modelo, marca, precio,autonomia, uso,  id)
        self.tiempo_carga = tiempo_carga
    def __str__(self):
        return super().__str__() + f", Tiempo de carga: {self.tiempo_carga}, ID: {self.id}"
        
class Van(Vehiculo):
    def __init__(self, marca, modelo, precio,autonomia, uso, asientos, id):
        super().__init__(modelo, marca, precio, autonomia, uso, id)
        self.asientos = asientos

    def __str__(self):
        return super().__str__() + f", Asientos: {self.asientos}, ID: {self.id}"
        
class Compacto(Vehiculo):
    def __init__(self, marca, modelo, precio, autonomia, uso,tamaño_baul, id):
        super().__init__(modelo, marca, precio,autonomia, uso, id)
        self.tamaño_baul = tamaño_baul
    def __str__(self):
        return super().__str__() + f", Tamaño del baul: {self.tamaño_baul}, ID: {self.id}"
    

class Nodo:
    def __init__(self, vehiculo):
        self.vehiculo = vehiculo
        self.siguiente = None

        

class ListaEnlazada:
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
    
    def eliminar(self, id):
        
        if self.cabeza is None:
            print("verga")
            return
        if self.cabeza.vehiculo.id == id:
            self.cabeza = self.cabeza.siguiente
            
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                print("vamos bien")
                print(id)
                print(actual.vehiculo.id)
                if actual.vehiculo.id == id:
                    print("vamos mejor")
                    
                    actual = actual.siguiente
                    print(f"El Vehiculo {self.vehiculo.marca} {self.vehiculo.modelo} ha sido eliminado con éxito")
                    return self
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
    def list(self):
        lista = []
        nodo = self.cabeza
        while nodo is not None:
            lista.append(nodo.vehiculo)
            nodo = nodo.siguiente
        return lista
    def ultimo_nodo(self):
        while self.cabeza.siguiente is not None:
            self.cabeza = self.cabeza.siguiente
        return self.cabeza

