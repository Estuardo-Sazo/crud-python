import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
          self.conexion=mysql.connector.connect(
              host='localhost',
              port=3306,
              user='root',
              password='',
              db='db_constructora'
          )
        except Error as ex:
          print('Error de conexion: {0}'.format(ex))


    def listarProductos(self):
        if self.conexion.is_connected():
            try:
              cursor=self.conexion.cursor()
              cursor.execute("SELECT * FROM productos")
              productos= cursor.fetchall()
              return productos
            except Error as ex:
                print('Error de conexion: {0}'.format(ex))

    def crearProducto(self,producto):
        if self.conexion.is_connected():
            try:
              cursor=self.conexion.cursor()
              sql="INSERT INTO productos (codigo, nombre, precio) VALUES('{0}','{1}',{2})"
              cursor.execute(sql.format(producto[0],producto[1],producto[2]))
              self.conexion.commit()
              print("¡Producto Registrado!\n")
            except Error as ex:
                print('Error de conexion: {0}'.format(ex))

    def actualizar(self,producto):
        if self.conexion.is_connected():
            try:
              cursor=self.conexion.cursor()
              sql="UPDATE productos SET  nombre='{0}', precio={1} WHERE codigo={2}"
              cursor.execute(sql.format(producto[1],producto[2],producto[0]))
              self.conexion.commit()
              print("¡Producto Actualizado!\n")
            except Error as ex:
                print('Error de conexion: {0}'.format(ex))

    def eliminarProducto(self, codigo):
        if self.conexion.is_connected():
            try:
              cursor=self.conexion.cursor()
              sql="DELETE FROM productos WHERE codigo = '{0}'"
              cursor.execute(sql.format(codigo))
              self.conexion.commit()
              print("¡Producto Eliminado!\n")
            except Error as ex:
                print('Error de conexion: {0}'.format(ex))           
    