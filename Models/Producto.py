import uuid
from typing import Optional

class Producto:
    # Clase base para representar un producto de la tienda
    
    def __init__(self, nombre: str, precio: float, stock: int):
        self.id: str = str(uuid.uuid4())  # Genera ID único automáticamente usando la librería uuid
        self.nombre: str = nombre  # Nombre del producto
        self.precio: float = precio  # Precio del producto
        self.stock: int = stock  # Cantidad disponible en inventario
    
    def hay_stock(self, cantidad):
    # Verifica si hay suficiente stock para la cantidad solicitada
        if self.stock >= cantidad:
            return True
        else:
            return False
    
    def actualizar_stock(self, cantidad):
    # Resta la cantidad del stock si hay suficiente disponible
        if self.hay_stock(cantidad):
            self.stock = self.stock - cantidad
        else:
            print("No hay suficiente stock")
    
    def __str__(self) -> str:
    # Devuelve una explicacion del producto
        return f"Producto(id={self.id}, nombre={self.nombre}, precio={self.precio}€, stock={self.stock})"


class ProductoElectronico(Producto):
    # Subclase de Producto para productos electrónicos con garantía
    
    def __init__(self, nombre: str, precio: float, stock: int, garantia: int = 12):
        super().__init__(nombre, precio, stock)  # Llama al constructor padre
        self.garantia: int = garantia  # Meses de garantía
    
    def __str__(self) -> str:
    # Sobrescribe __str__ para incluir información de garantía
        return f"ProductoElectronico(id={self.id}, nombre={self.nombre}, precio={self.precio}€, stock={self.stock}, garantia={self.garantia} meses)"


class ProductoRopa(Producto):
    # Subclase de Producto para ropa con talla y color
    
    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str):
        super().__init__(nombre, precio, stock)  # Llama al constructor padre
        self.talla: str = talla  # Talla de la ropa
        self.color: str = color  # Color de la ropa
    
    def __str__(self) -> str:
    # Sobrescribe __str__ para incluir talla y color
        return f"ProductoRopa(id={self.id}, nombre={self.nombre}, precio={self.precio}€, stock={self.stock}, talla={self.talla}, color={self.color})"