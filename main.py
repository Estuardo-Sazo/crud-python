from db.conection import DAO
import funciones
def menuPirncipal():
    contnuar=True
    while(contnuar):
        opcionCorrecta=False
        while(not opcionCorrecta):
            print("=============== MENÚ PRINCIPAL ==============")
            print("1.-  Ver Productos")
            print("2.-  Crear Producto")
            print("3.-  Modificar Producto")
            print("4.-  Eliminar Producto")
            print("5.-  Salir")
            print("=============================================")
            opcion=int(input("Selecciona una opción: "))

            if opcion <1 or opcion>5:
                print("Opción incorrecta,ingresa nuevamente...")
            elif opcion==5:
                contnuar=False
                print("Gracias por usar nuestro sistema")
                break
            else:
                opcionCorrecta=True
                ejecutarOpcion(opcion)    

def ejecutarOpcion(opcion):
    dao=DAO()

    if opcion ==1:
        try:
          productos= dao.listarProductos()
          if len(productos)>0:
              funciones.listarProductos(productos)
          else:
               print("No se encontraron registros...")   
        except:
          print("Ocurrio un error")
    elif opcion ==2:
        producto= funciones.solicitarProducto()
        try:
          dao.crearProducto(producto)
        except:
          print("Ocurrio un error")
    elif opcion ==3:
        try:
          productos= dao.listarProductos()
          if len(productos)>0:
                producto= funciones.datosActualizar(productos)
                if producto:
                    dao.actualizar(producto)
                else:
                    print("Código de curso a actualizar no encontrado...\n")    
          else:
               print("No se encontraron registros...\n")   
        except:
          print("Ocurrio un error")  
    elif opcion ==4:
        try:
          productos= dao.listarProductos()
          if len(productos)>0:
              codigoEliminar=funciones.solicitarCodigoEliminar(productos)
              if not(codigoEliminar==""):
                  dao.eliminarProducto(codigoEliminar)
              else:
               print("Código de producto no encontrado ...\n")       
          else:
               print("No se encontraron registros...\n")   
        except:
          print("Ocurrio un error")  
    else:
        print("Opción no Válida")    



menuPirncipal()