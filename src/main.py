from Services.Tienda_service import TiendaService

def main():
    
    print("=== SISTEMA DE TIENDA ONLINE ===")
    print("Iniciando el sistema...\n")
    
    # Crear instancia del servicio de tienda
    tienda = TiendaService()
    
    # 1. Registro de los usuarios (3 clientes + 1 administrador)
    print("--- REGISTRO USUARIOS ---")
    cliente1 = tienda.registrar_usuario("cliente", "Ana García", "ana@gmail.com", "Avenida finisterre 12")
    cliente2 = tienda.registrar_usuario("cliente", "José Bordalás", "Bordalas@gmail.com", "Plaza pontevedra 4")
    cliente3 = tienda.registrar_usuario("cliente", "María López", "maria@gmail.com", "San pedro mezonzo 78")
    admin = tienda.registrar_usuario("administrador", "Admin Principal", "admin@tienda.com")
    
    print(f"Registrados {len(tienda.usuarios)} usuarios:")
    for usuario in tienda.usuarios:
        print(usuario)
    print()
    
    # 2. Crear 5 productos de diferentes categorías
    producto1 = tienda.anadir_producto("electronico", "Movil Samsung", 699.99, 15, garantia=24)
    producto2 = tienda.anadir_producto("electronico", "Portátil HP", 899.50, 8, garantia=12)
    producto3 = tienda.anadir_producto("ropa", "Camiseta Básica", 19.95, 50, talla="L", color="Azul")
    producto4 = tienda.anadir_producto("ropa", "Pantalón Vaquero", 45.00, 25, talla="M", color="Negro")
    producto5 = tienda.anadir_producto("generico", "Libro Python", 29.99, 20)
    
    # 3. Listar productos para verificar inventario
    print("--- INVENTARIO ACTUAL ---")
    productos = tienda.listar_productos()
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto}")
    print()
    
    # 4. Realizar 3 pedidos de distintos clientes
    print("--- PEDIDOS ---")
    
    # Pedido 1: Ana compra 2 moviles y 1 camiseta
    print("Pedido 1 - Ana García:")
    pedido1 = tienda.realizar_pedido(cliente1.id, {
        producto1.id: 2,  # 2 moviles
        producto3.id: 1   # 1 camiseta
    })
    if pedido1:
        print(pedido1)
    print()
    
    # Pedido 2: José compra 1 portátil y 2 pantalones
    print("Pedido 2 - José Bordalás:")
    pedido2 = tienda.realizar_pedido(cliente2.id, {
        producto2.id: 1,  # 1 portátil
        producto4.id: 2   # 2 pantalones
    })
    if pedido2:
        print(pedido2)
    print()
    
    # Pedido 3: María compra 3 libros y 1 camiseta
    print("Pedido 3 - María López:")
    pedido3 = tienda.realizar_pedido(cliente3.id, {
        producto5.id: 3,  # 3 libros
        producto3.id: 1   # 1 camiseta
    })
    if pedido3:
        print(pedido3)
    print()
    
    # 5. Mostrar stock actualizado después de los pedidos
    print("--- STOCK ACTUALIZADO DESPUÉS DE PEDIDOS ---")
    productos_actualizados = tienda.listar_productos()
    for i, producto in enumerate(productos_actualizados, 1):
        print(f"{i}. {producto}")
    print()
    
    # 6. Comprobar histórico de pedidos de un cliente
    print("--- HISTÓRICO DE PEDIDOS DE MARÍA LÓPEZ ---")
    pedidos_maria = tienda.listar_pedidos_usuario(cliente3.id)
    if pedidos_maria:
        print(f"María ha realizado {len(pedidos_maria)} pedido(s):")
        for pedido in pedidos_maria:
            print(pedido)
    else:
        print("El cliente no ha realizado ningún pedido")
    print()
    
    print("=== FIN DE LA DEMOSTRACIÓN ===")

# Punto de entrada del programa
if __name__ == "__main__":
    main()