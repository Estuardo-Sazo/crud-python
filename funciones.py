def listarProductos(productos):
    print("\nProductos:\n")
    contador=1
    for pro in productos:
        datos="{0}. Código: {1} | Nombre: {2} | Precio: Q{3}"
        print(datos.format(contador,pro[1], pro[2], pro[3]))
        contador=contador+1
    print(" ") 


def solicitarProducto():
    codigoCorrecto= False
    while (not codigoCorrecto):
        codigo=input("Ingrese Código: ")
        if len(codigo)>3:
            codigoCorrecto=True
        else:
            print("Código incorrecto: debe tener     4 dígitos. ")           
            
        
    nombre=input("Ingrese Nombre: ")

    precioCorrecto=False
    while(not precioCorrecto):
        precio=input("Ingrese Precio: Q")
        if precio.isnumeric():
            precioCorrecto= True
            precio=float(precio)
        else:
            print("Precio incorrecto: debe ser un número. ")       
    producto=(codigo,nombre,precio)
    return producto

def datosActualizar(productos):
    listarProductos(productos)
    existeCodigo=False
    codigoEditar=input("Ingrese el código: ")
    for pro in productos:
        if pro[1]== codigoEditar:
            existeCodigo= True
            break
        
    if existeCodigo:
        nombre=input("Ingrese Nuevo Nombre : ")

        precioCorrecto=False
        while(not precioCorrecto):
            precio=input("Ingrese Nuevo Precio: Q")
            if  precio.isnumeric():
                precioCorrecto= True
                precio=float(precio)
            else:
                print("Precio incorrecto: debe ser un número. ")       
        producto=(codigoEditar,nombre,precio)
    else:
        producto= None

    return producto    

def solicitarCodigoEliminar(productos):
    existeCodigo=False
    codigoEliminar=input("Ingrese el código: ")

    for pro in productos:
        if pro[1]== codigoEliminar:
            existeCodigo= True
            break

    if not existeCodigo:
            codigoEliminar=""

    return codigoEliminar    