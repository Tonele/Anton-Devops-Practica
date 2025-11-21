import uuid
from datetime import datetime
from typing import Dict
from Models.Usuario import Cliente  # Importa la clase Cliente
from Models.Producto import Producto  # Importa la clase Producto

class Pedido:
    
    def __init__(self, cliente: Cliente):
        self.id: str = str(uuid.uuid4())  # Genera ID único automáticamente
        self.cliente: Cliente = cliente  # Cliente que realiza el pedido
        self.fecha: datetime = datetime.now()  # Esto es para poner la fecha y hora del pedido
        self.productos: Dict[Producto, int] = {}  # Diccionario producto significa la cantidad
    
    def anadir_producto(self, producto: Producto, cantidad: int) -> None:
        # Añade un producto con su cantidad al pedido
        if producto in self.productos:
            # Si el producto ya existe, suma la cantidad
            self.productos[producto] = self.productos[producto] + cantidad
        else:
            # Si es nuevo, lo añade con la cantidad especificada
            self.productos[producto] = cantidad
    
    def calcular_total(self) -> float:
        # Calcula el importe total del pedido
        total = 0.0
        for producto, cantidad in self.productos.items():
            # Multiplica precio por cantidad y suma al total
            total = total + (producto.precio * cantidad)
        return total
    
    def __str__(self) -> str:
        # Devuelve un resumen del pedido
        lineas_pedido = []
        for producto, cantidad in self.productos.items():
            # Calcula el subtotal de cada línea
            subtotal = producto.precio * cantidad
            lineas_pedido.append(f"  - {producto.nombre} x{cantidad} = {subtotal:.2f}€")
        
        # Une todas las líneas en un solo texto
        detalle_productos = "\n".join(lineas_pedido)
        total = self.calcular_total()
        
        return f"Pedido {self.id}\nCliente: {self.cliente.nombre}\nFecha: {self.fecha.strftime('%Y-%m-%d %H:%M')}\nProductos:\n{detalle_productos}\nTotal: {total:.2f}€"