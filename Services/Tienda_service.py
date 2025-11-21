from typing import List, Optional, Dict
from Models.Producto import Producto, ProductoElectronico, ProductoRopa
from Models.Usuario import Usuario, Cliente, Administrador
from Models.Pedido import Pedido

class TiendaService:
    
    def __init__(self):
        self.productos: List[Producto] = []  # Lista de todos los productos
        self.usuarios: List[Usuario] = []  # Lista de todos los usuarios
        self.pedidos: List[Pedido] = []  # Lista de todos los pedidos
    
    def registrar_usuario(self, tipo: str, nombre: str, email: str, direccion: str = "") -> Usuario:
    # Registra un nuevo usuario según su tipo (cliente o administrador)
        if tipo.lower() == "cliente":
            # Crea un cliente con dirección
            nuevo_usuario = Cliente(nombre, email, direccion)
        elif tipo.lower() == "administrador":
            # Crea un administrador
            nuevo_usuario = Administrador(nombre, email)
        else:
            # Tipo no válido
            print("Usuario no válido")
            return None

        # Añade el usuario a la lista
        self.usuarios.append(nuevo_usuario)
        return nuevo_usuario
    
    def anadir_producto(self, categoria: str, nombre: str, precio: float, stock: int, **kwargs) -> Producto:
    # Añade un producto al inventario según su categoría
        if categoria.lower() == "electronico":
            # Producto electrónico con garantía (por defecto 12 meses)
            garantia = kwargs.get("garantia", 12)
            nuevo_producto = ProductoElectronico(nombre, precio, stock, garantia)
        elif categoria.lower() == "ropa":
            # Producto de ropa con talla y color
            talla = kwargs.get("talla", "M")
            color = kwargs.get("color", "Blanco")
            nuevo_producto = ProductoRopa(nombre, precio, stock, talla, color)
        else:
            # Producto genérico
            nuevo_producto = Producto(nombre, precio, stock)
        
        # Añade el producto a la lista
        self.productos.append(nuevo_producto)
        return nuevo_producto
    
    def eliminar_producto(self, producto_id: str) -> bool:
    # Elimina un producto del inventario por su ID
        for producto in self.productos:
            if producto.id == producto_id:
                # Encuentra y elimina el producto
                self.productos.remove(producto)
                return True
        # Si no se encontró el producto
        return False
    
    def listar_productos(self) -> List[Producto]:
        # Devuelve la lista de productos disponibles
        return self.productos
    
    def buscar_usuario(self, usuario_id: str) -> Optional[Usuario]:
        # Busca un usuario por su ID
        for usuario in self.usuarios:
            if usuario.id == usuario_id:
                return usuario
        # No se encontró el usuario
        return None
    
    def buscar_producto(self, producto_id: str) -> Optional[Producto]:
        # Busca un producto por su ID
        for producto in self.productos:
            if producto.id == producto_id:
                return producto
        # No se encontró el producto
        return None
    
    def realizar_pedido(self, cliente_id: str, productos_cantidades: Dict[str, int]) -> Optional[Pedido]:
        # Realiza un pedido verificando usuario y stock
        # Busca el cliente
        cliente = self.buscar_usuario(cliente_id)
        if cliente is None:
            print(f"Error: Cliente con ID {cliente_id} no encontrado")
            return None
        
        # Verifica que sea un cliente (no administrador)
        if not isinstance(cliente, Cliente):
            print("Error: El usuario debe ser un cliente para realizar pedidos")
            return None
        
        # Crea el pedido
        pedido = Pedido(cliente)
        
        # Procesa cada producto solicitado
        for producto_id, cantidad in productos_cantidades.items():
            # Busca el producto
            producto = self.buscar_producto(producto_id)
            if producto is None:
                print(f"Producto con ID {producto_id} no encontrado")
                continue
            
            # Verifica el stock
            if not producto.hay_stock(cantidad):
                print(f"Error: No hay suficiente stock de {producto.nombre}. Disponible: {producto.stock}, solicitado: {cantidad}")
                continue
            
            # Actualiza el stock y añade al pedido
            producto.actualizar_stock(cantidad)
            pedido.anadir_producto(producto, cantidad)
        
        # Guarda el pedido si tiene productos
        if len(pedido.productos) > 0:
            self.pedidos.append(pedido)
            return pedido
        else:
            print("Error: El pedido no contiene productos válidos")
            return None
    
    def listar_pedidos_usuario(self, usuario_id: str) -> List[Pedido]:
        # Lista todos los pedidos de un usuario ordenados por fecha
        pedidos_usuario = []
        
        # Filtra pedidos del usuario específico
        for pedido in self.pedidos:
            if pedido.cliente.id == usuario_id:
                pedidos_usuario.append(pedido)
        
        # Ordena por fecha (más antiguos primero)
        pedidos_ordenados = sorted(pedidos_usuario, key=lambda p: p.fecha)
        return pedidos_ordenados