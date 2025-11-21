import uuid

class Usuario:
    # Clase para representar cualquier usuario de la tienda
    
    def __init__(self, nombre: str, email: str):
        self.id: str = str(uuid.uuid4())  # Genera ID único automáticamente usando la librería uuid
        self.nombre: str = nombre  # Nombre completo del usuario
        self.email: str = email  # Correo electrónico del usuario
    
    def is_admin(self) -> bool:
    # Por defecto, un usuario no es administrador
        return False
    
    def __str__(self) -> str:
    # Devuelve una representación en texto del usuario
        return f"Usuario(id={self.id}, nombre={self.nombre}, email={self.email})"


class Cliente(Usuario):
    # Subclase de Usuario para clientes con dirección postal
    
    def __init__(self, nombre: str, email: str, direccion: str):
        super().__init__(nombre, email)  # Llama al constructor padre
        self.direccion: str = direccion  # Dirección postal del cliente
    
    def __str__(self) -> str:
    # Sobrescribe __str__ para incluir la dirección
        return f"Cliente(id={self.id}, nombre={self.nombre}, email={self.email}, direccion={self.direccion})"


class Administrador(Usuario):
    # Subclase de Usuario para administradores de la tienda
    
    def __init__(self, nombre: str, email: str):
        super().__init__(nombre, email)  # Llama al constructor padre
    
    def is_admin(self) -> bool:
    # Sobrescribe is_admin para indicar que es administrador al devolver True
        return True
    
    def __str__(self) -> str:
    # Sobrescribe __str__ para indicar que es administrador
        return f"Administrador(id={self.id}, nombre={self.nombre}, email={self.email})"
