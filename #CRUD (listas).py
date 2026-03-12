#CRUD (listas)
lista = []
productos =[]
ordenes = []

#CRUD PARA CLIENTES
def agregar_usuario(id, name, email):
    usuario = {
        "id": id, 
        "name": name,
        "email": email}
    
    lista.append(usuario)

def listar_clientes():
    if not lista:
        print("No existen clientes.")
        return
    for i in lista:
        print(f"ID: {i['id']} | Nombre: {i['name']} | Email: {i['email']}")

def buscar_cliente(id_b):
    for usuario in lista:
        if usuario ['id'] == id_b:
            return usuario
    return None

def editar_cliente():
    id_e = (input("Ingrese el ID a editar: "))
    cliente_encontrado = buscar_cliente(id_e)

    if cliente_encontrado:
        print(f"Editando al cliente: {cliente_encontrado['name']} {cliente_encontrado['email']}")
        print("--INGRESE LOS NUEVOS DATOS--")
        nname = (input("Nuevo nombre: "))
        nemail = (input("Nuevo email: "))

        cliente_encontrado['name'] = nname
        cliente_encontrado['email'] = nemail
        print("Cliente actualizado con éxito.")

    else: 
        print("Cliente no encontrado.")

def eliminar_cliente():
    id_el = input("Ingrese el ID que desea eliminar: ")
    cliente_encontrado = buscar_cliente(id_el)
    
    if cliente_encontrado:
        lista.remove(cliente_encontrado)
        print(f"Cliente: {cliente_encontrado['name']} eliminado con exito.")
    else:
        print("Cliente no encontrado.")

#CRUD PARA PRODUCTOS
def agregar_producto(id, name, precio, stock):
    producto ={
        "id" : id,
        "name": name,
        "precio": precio,
        "stock": stock
    }
    productos.append(producto)
    
def listar_productos():
    if not productos:
        print("No hay productos.")
        
    print("--LISTA DE PRODUCTOS--")
    for i in productos:
        print(f"ID: {i['id']} | Producto: {i['name']} | Precio: {i['precio']} | Stock: {i['stock']}")

def buscar_producto(id_b):
    for producto in productos:
        if producto['id'] == id_b:
            return producto
    return None

def editar_producto():
    id_b = input("Ingrese el producto a editar: ")
    producto_encontrado = buscar_producto(id_b)

    if producto_encontrado:
        print(f"Editando el producto: {producto_encontrado['name']}")
        print("--INGRESE LOS NUEVOS DATOS--")
        nname = (input("Nuevo nombre: "))
        nprecio = (input("Nuevo precio: "))
        nstock = (input("Nuevo stock: "))

        producto_encontrado['name'] = nname
        producto_encontrado['precio'] = nprecio
        producto_encontrado['stock'] = nstock
        print("Producto actualizado con éxito.")

    else: 
        print("Producto no encontrado.")

def eliminar_producto():
    print("--ELIMINAR PRODUCTO--")
    id_el = input("Ingrese el ID del producto que desea elminar: ")
    producto_encontrado = buscar_producto(id_el)

    if producto_encontrado:
        productos.remove(producto_encontrado)
        print(f"Producto: {producto_encontrado['name']} ha sido eliminado con exito.")
    else:
        print("Producto no encontrado.")
        
#AQUI COMIENZA LA PARTE DE ORDENES

def agregar_orden():
    print("--NUEVA ORDEN DE COMPRA--")
    id_or = input("Ingrese el ID de la orden: ")

    #verificar que el cliente existe 
    id_cliente = input("Ingrese el id del cliente que va a realizar la compra ")
    cliente_encontrado = buscar_cliente(id_cliente)

    if not cliente_encontrado:
        print("El cliente no existe, debe registrarlo.")
        return 
    
    productos_comprados = []
    total = 0.0

    print("--AGREGANDO PRODUCTOS--")
    print("Ingrese 0 cuando termine de agregar productos")

    while True:
        id_prod = input("Ingrese el ID del producto a agregar: ")
        if id_prod == "0": 
            break 
        
        producto_encontrado = buscar_producto(id_prod)
        if producto_encontrado:
            productos_comprados.append(producto_encontrado['id'])
            total += producto_encontrado['precio']
            print(f"El producto: {producto_encontrado['name']} | Precio: {producto_encontrado['precio']}")
            print("Fue agregado a la orden")
        else:
            print("Producto no encontrado.")

        if not productos_comprados:
            print("Debe al menos agregar un producto")

        else:
            orden = {
                "id_or": id_or,
                "id_cliente": id_cliente,
                "productos": productos_comprados, 
                "total": total
            }   
            ordenes.append(orden)
            print("Orden registrada con exito")
            print(f"--TOTAL A PAGAR ${total}\n")

def listar_ordenes():
    if not ordenes:
        print("No hay ordenes registradas.")
        return 
    for i in ordenes:
        print(f"ID de la orden: {i['id_or']} | ID del cliente: {i['id_cliente']} | Productos: {i['productos']} | Total: {i['total']}")  

def menu():
    while True:
        print("----MENÚ----")
        print("--USUARIOS--")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Editar cliente")
        print("4. Eliminar cliente")
        print("\n")
        print("--PRODUCTOS--")
        print("5. Agregar producto")
        print("6. Listar productos")
        print("7. Editar producto")
        print("8. Eliminar producto")
        print("\n")
        print("--ORDENES--")
        print("9. Agregar orden")   
        print("10. Listar ordenes")
        print("\n")
        print("11. Salir")

        opcion = int(input("Ingrese una opción: "))
        match (opcion):
            case 1:
                id = input("Ingrese el ID: ")
                name = input("Ingrese el nombre: ")
                email = input("Ingrese el email: ")
                agregar_usuario(id, name, email)

            case 2:
                listar_clientes()

            case 3:
                editar_cliente()

            case 4:
                eliminar_cliente()

            case 5:
                id = input("Ingrese el ID del producto: ")
                name = str(input(("Ingrese el nombre del producto: ")))
                precio = float(input(("Ingrese el precio del producto: ")))
                stock = int(input(("Ingrese el stock: ")))
                agregar_producto(id, name, precio, stock)
                
            case 6:
                listar_productos()

            case 7:
                editar_producto()
            
            case 8:
                eliminar_producto()
            
            case 9:
                agregar_orden()

            case 10:
                listar_ordenes()

            case 11:
                print("Saliendo del programa...")
                break

if __name__ == "__main__":
    menu()