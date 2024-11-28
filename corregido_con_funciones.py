import sqlite3

# Función para crear la base de datos y la tabla si no existen
def CrearDB1():
    try:
        conexion = sqlite3.connect("Stock")  # Conectamos o creamos la base de datos "Stock"
        miCursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL en la base de datos

        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS STOCKDISPONIBLE (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_ARTICULO VARCHAR(50),
                PRECIO INTEGER,
                SECCION VARCHAR(50),
                MARCA VARCHAR(50)
            )
        ''')  # Ejecutamos la creación de la tabla STOCKDISPONIBLE si no existe

        conexion.commit()  # Confirmamos los cambios en la base de datos
        conexion.close()  # Cerramos la conexión con la base de datos
        print("Base de datos y tabla creadas exitosamente.")
    except sqlite3.Error as error:
        print("Error al crear la base de datos y la tabla:", error)  # Manejamos errores si surgen

# Función para conectar con la base de datos
def conectarDB1():
    try:
        conexion = sqlite3.connect("Stock")  # Conectamos a la base de datos "Stock"
        return conexion  # Retornamos la conexión para utilizarla en otras funciones
    except sqlite3.Error as error:
        print("Error al abrir la base de datos:", error)
        return None

# Función para ingresar datos desde teclado
def ingresarDatosTeclado():
    nombre = input("Ingrese el nombre del artículo: ")  # Solicitamos al usuario el nombre del artículo
    precio = int(input("Ingrese el precio del artículo: "))  # Solicitamos al usuario el precio del artículo
    seccion = input("Ingrese la sección del artículo: ")  # Solicitamos al usuario la sección del artículo
    marca = input("Ingrese la marca del artículo: ")  # Solicitamos al usuario la marca del artículo
    return nombre, precio, seccion, marca  # Retornamos los datos ingresados por el usuario

# Función para agregar un artículo a la base de datos
# Realiza la conexión, inserta un nuevo registro con los datos proporcionados y muestra un mensaje de éxito o error
# Si hay un error, maneja las excepciones y realiza un rollback
def agregarArticulo(nombre, precio, seccion, marca):
    conexion = conectarDB1()  # Conectamos a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL

            # Insertamos un nuevo artículo en la tabla STOCKDISPONIBLE con los datos proporcionados
            miCursor.execute("INSERT INTO STOCKDISPONIBLE (NOMBRE_ARTICULO, PRECIO, SECCION, MARCA) VALUES (?, ?, ?, ?)",
                            (nombre, precio, seccion, marca))

            conexion.commit()  # Confirmamos los cambios en la base de datos
            conexion.close()  # Cerramos la conexión con la base de datos
            print("¡Artículo agregado al stock exitosamente!")
        except sqlite3.Error as error:
            print("Error al agregar el artículo:", error)  # Manejamos errores si surgen
            conexion.rollback()  # Realizamos un rollback si hay errores
            conexion.close()  # Cerramos la conexión con la base de datos


#Funcion de ordenamiento ascendente para tabla de stock

def ordenarArticulosNomAsc():
    conexion = conectarDB1()  # Conectamos a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL

            # Consultar y ordenar por nombre de forma ascendente
            miCursor.execute('SELECT * FROM STOCKDISPONIBLE ORDER BY NOMBRE_ARTICULO ASC')
            articulos = miCursor.fetchall()

            if not articulos:  # Si no hay registros
                print("No hay artículos en el stock.")
            else:
                print(f"{'ID':<5} {'Nombre Artículo':<20} {'Precio':<10} {'Sección':<15} {'Marca':<15}")
                print("-" * 65)
                for articulo in articulos:
                    print(f"{articulo[0]:<5} {articulo[1]:<20} {articulo[2]:<10.2f} {articulo[3]:<15} {articulo[4]:<15}")

        except sqlite3.Error as error:
            print("Error al ordenar el artículo:", error)  # Manejamos errores si surgen
            conexion.rollback()  # Realizamos un rollback si hay errores
            conexion.close()  # Cerramos la conexión con la base de datos
            
            
            
def ordenarArticulosPreAsc():
    conexion = conectarDB1()  # Conectamos a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL

            # Consultar y ordenar por nombre de forma ascendente
            miCursor.execute('SELECT * FROM STOCKDISPONIBLE ORDER BY PRECIO ASC')
            articulos = miCursor.fetchall()

            if not articulos:  # Si no hay registros
                print("No hay artículos en el stock.")
            else:
                print(f"{'ID':<5} {'Nombre Artículo':<20} {'Precio':<10} {'Sección':<15} {'Marca':<15}")
                print("-" * 65)
                for articulo in articulos:
                    print(f"{articulo[0]:<5} {articulo[1]:<20} {articulo[2]:<10.2f} {articulo[3]:<15} {articulo[4]:<15}")

        except sqlite3.Error as error:
            print("Error al ordenar el artículo:", error)  # Manejamos errores si surgen
            conexion.rollback()  # Realizamos un rollback si hay errores
            conexion.close()  # Cerramos la conexión con la base de datos



def ordenarArticulosNomDesc():
    conexion = conectarDB1()  # Conectamos a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL

            # Consultar y ordenar por nombre de forma ascendente
            miCursor.execute('SELECT * FROM STOCKDISPONIBLE ORDER BY NOMBRE_ARTICULO DESC')
            articulos = miCursor.fetchall()

            if not articulos:  # Si no hay registros
                print("No hay artículos en el stock.")
            else:
                print(f"{'ID':<5} {'Nombre Artículo':<20} {'Precio':<10} {'Sección':<15} {'Marca':<15}")
                print("-" * 65)
                for articulo in articulos:
                    print(f"{articulo[0]:<5} {articulo[1]:<20} {articulo[2]:<10.2f} {articulo[3]:<15} {articulo[4]:<15}")

        except sqlite3.Error as error:
            print("Error al ordenar el artículo:", error)  # Manejamos errores si surgen
            conexion.rollback()  # Realizamos un rollback si hay errores
            conexion.close()  # Cerramos la conexión con la base de datos
            
            
            
def ordenarArticulosPreDesc():
    conexion = conectarDB1()  # Conectamos a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL

            # Consultar y ordenar por nombre de forma ascendente
            miCursor.execute('SELECT * FROM STOCKDISPONIBLE ORDER BY PRECIO DESC')
            articulos = miCursor.fetchall()

            if not articulos:  # Si no hay registros
                print("No hay artículos en el stock.")
            else:
                print(f"{'ID':<5} {'Nombre Artículo':<20} {'Precio':<10} {'Sección':<15} {'Marca':<15}")
                print("-" * 65)
                for articulo in articulos:
                    print(f"{articulo[0]:<5} {articulo[1]:<20} {articulo[2]:<10.2f} {articulo[3]:<15} {articulo[4]:<15}")

        except sqlite3.Error as error:
            print("Error al ordenar el artículo:", error)  # Manejamos errores si surgen
            conexion.rollback()  # Realizamos un rollback si hay errores
            conexion.close()  # Cerramos la conexión con la base de datos




# Función para mostrar todos los artículos en el stock
# Realiza la conexión, ejecuta una consulta para obtener todos los registros y los muestra en pantalla
def mostrarArticulos():
    conexion = conectarDB1()  # Conectamos a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL

            # Seleccionamos todos los registros de la tabla STOCKDISPONIBLE
            miCursor.execute("SELECT * FROM STOCKDISPONIBLE")
            articulos = miCursor.fetchall()  # Obtenemos todos los registros

            conexion.close()  # Cerramos la conexión con la base de datos

            if not articulos:  # Si no hay registros
                print("No hay artículos en el stock.")
            else:
                print("Artículos en el stock:")
                for articulo in articulos:  # Iteramos sobre los registros y los mostramos en pantalla
                    print(articulo)
        except sqlite3.Error as error:
            print("Error al mostrar los artículos:", error)  # Manejamos errores si surgen

# Función para actualizar un artículo en el stock
# Realiza la conexión, actualiza el registro con el ID proporcionado con los nuevos datos y muestra un mensaje de éxito o error
# Si hay un error, maneja las excepciones y realiza un rollback
def actualizarArticulo(id_articulo, nombre, precio, seccion, marca):
    conexion = conectarDB1()  # Conectamos a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL

            # Actualizamos el registro con el ID proporcionado con los nuevos datos
            miCursor.execute("UPDATE STOCKDISPONIBLE SET NOMBRE_ARTICULO = ?, PRECIO = ?, SECCION = ?, MARCA = ? WHERE ID = ?",
                            (nombre, precio, seccion, marca, id_articulo))

            conexion.commit()  # Confirmamos los cambios en la base de datos
            conexion.close()  # Cerramos la conexión con la base de datos
            print("¡Artículo actualizado exitosamente!")
        except sqlite3.Error as error:
            print("Error al actualizar el artículo:", error)  # Manejamos errores si surgen
            conexion.rollback()  # Realizamos un rollback si hay errores
            conexion.close()  # Cerramos la conexión con la base de datos

# Función para borrar un artículo del stock
# Realiza la conexión, elimina el registro con el ID proporcionado y muestra un mensaje de éxito o error
# Si hay un error, maneja las excepciones y realiza un rollback
def eliminarArticulo(id_articulo):
    conexion = conectarDB1()  # Conectamos a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL

            # Eliminamos el registro con el ID proporcionado de la tabla STOCKDISPONIBLE
            miCursor.execute("DELETE FROM STOCKDISPONIBLE WHERE ID = ?", (id_articulo,))

            conexion.commit()  # Confirmamos los cambios en la base de datos
            conexion.close()  # Cerramos la conexión con la base de datos
            print("¡Artículo eliminado exitosamente!")
        except sqlite3.Error as error:
            print("Error al eliminar el artículo:", error)  # Manejamos errores si surgen
            conexion.rollback()  # Realizamos un rollback si hay errores
            conexion.close()  # Cerramos la conexión con la base de datos

# Función para mostrar la base de datos completa
# Realiza la conexión, obtiene todos los registros de la tabla y los muestra en pantalla
def mostrarBaseDatos():
    conexion = None
    try:
        conexion = conectarDB1()  # Conectamos a la base de datos
        miCursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL

        # Seleccionamos todos los registros de la tabla STOCKDISPONIBLE
        miCursor.execute("SELECT * FROM STOCKDISPONIBLE")
        articulos = miCursor.fetchall()  # Obtenemos todos los registros

        if not articulos:  # Si no hay registros
            print("No hay artículos en el stock.")
        else:
            print(f"{'ID':<5} {'Nombre Artículo':<20} {'Precio':<10} {'Sección':<15} {'Marca':<15}")
            print("-" * 65)
            for articulo in articulos:
                print(f"{articulo[0]:<5} {articulo[1]:<20} {articulo[2]:<10.2f} {articulo[3]:<15} {articulo[4]:<15}")
    except sqlite3.Error as error:
        print("Error al mostrar la base de datos:", error)  # Manejamos errores si surgen
    finally:
        if conexion:
            conexion.close()  # Aseguramos cerrar la conexión

def ordenamiento():
    print("¿Como desea ordenarlo?")
    print("1. Nombre Ascendente")
    print("2. Nombre Descendente")
    print("3. Precio Ascendente")
    print("4. Precio Descendente")
    opcion = input()
        
    if  opcion == "1":
        ordenarArticulosNomAsc() # Ordenar ascendentemente
    elif opcion == "2":
        ordenarArticulosNomDesc() # Ordenar descendentemente
    elif opcion == "3":
        ordenarArticulosPreAsc() 
    elif opcion == "4":
        ordenarArticulosPreDesc() 
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")  # Manejar opción inválida

# Función para mostrar el menú y obtener la opción elegida
def mostrarMenu():
    print("\n** MENÚ **")
    print("1. Agregar artículo")
    print("2. Mostrar artículos")
    print("3. Actualizar artículo")
    print("4. Eliminar artículo")
    print("5. Mostrar base de datos completa")
    print("6. Ordenar Stock")
    print("7. Salir")

    opcion = input("Ingrese el número de la opción que desea ejecutar: ")  # Solicitamos la opción al usuario
    return opcion  # Retornamos la opción ingresada por el usuario

# Función para agregar un artículo a la base de datos utilizando datos ingresados por teclado
def agregarArticuloTeclado():
    nombre, precio, seccion, marca = ingresarDatosTeclado()  # Obtenemos los datos del artículo desde teclado
    agregarArticulo(nombre, precio, seccion, marca)  # Llamamos a la función para agregar el artículo
    mostrarBaseDatos()  # Mostramos la base de datos actualizada

# Función para actualizar un artículo en el stock utilizando datos ingresados por teclado
def actualizarArticuloTeclado():
    mostrarBaseDatos()  # Mostramos la base de datos actualizada
    id_articulo = int(input("Ingrese el ID del artículo a actualizar: "))  # Solicitamos el ID del artículo a actualizar
    nombre, precio, seccion, marca = ingresarDatosTeclado()  # Obtenemos los datos del artículo desde teclado
    actualizarArticulo(id_articulo, nombre, precio, seccion, marca)  # Llamamos a la función para actualizar el artículo
    

# Función para borrar un artículo del stock utilizando datos ingresados por teclado
def eliminarArticuloTeclado():
    mostrarBaseDatos()  # Mostramos la base de datos actualizada
    id_articulo = int(input("Ingrese el ID del artículo a eliminar: "))  # Solicitamos el ID del artículo a eliminar
    eliminarArticulo(id_articulo)  # Llamamos a la función para eliminar el artículo
    

# Función principal del programa
def programa():
    CrearDB1()  # Llamamos a la función para crear la base de datos si no existe
    
    while True:  # Ejecutamos el programa en un bucle infinito hasta que el usuario elija salir
        opcion = mostrarMenu()  # Mostramos el menú y obtenemos la opción elegida por el usuario

        if opcion == "1":
            agregarArticuloTeclado()  # Agregar artículo
        elif opcion == "2":
            mostrarBaseDatos()  # Mostrar artículos
        elif opcion == "3":
            actualizarArticuloTeclado()  # Actualizar artículo
        elif opcion == "4":
            eliminarArticuloTeclado()  # Eliminar artículo
        elif opcion == "5":
            mostrarBaseDatos()  # Mostrar base de datos completa
        elif opcion == "6":
            ordenamiento()
        elif opcion == "7":
            print("¡Hasta luego!")  # Salir del programa
            break  # Salir del bucle infinito
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 6.")  # Manejar opción inválida




#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



# Función para crear la base de datos y la tabla si no existen
def crearBD():
    try:
        conexion = sqlite3.connect("Usuarios")  # Se conecta a la base de datos "Usuarios"
        miCursor = conexion.cursor()  # Crea un cursor para ejecutar comandos SQL en la base de datos

        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS USUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                CONTRASENA VARCHAR(50),
                ROL VARCHAR(20)
            )
        ''')  # Ejecuta la creación de la tabla USUARIOS si no existe

        conexion.commit()  # Confirma los cambios en la base de datos
        conexion.close()  # Cierra la conexión con la base de datos
        print("Base de datos y tabla creadas exitosamente.")  # Muestra un mensaje de éxito
    except sqlite3.Error as error:
        print("Error al crear la base de datos y la tabla:", error)  # Maneja errores si surgen

# Función para conectar con la base de datos
def conectarBD():
    try:
        conexion = sqlite3.connect("Usuarios")  # Se conecta a la base de datos "Usuarios"
        return conexion  # Retorna la conexión para usarla en otras funciones
    except sqlite3.Error as error:
        print("Error al abrir la base de datos:", error)
        return None

# Función para agregar un usuario a la base de datos
def agregarUsuario(nombre_usuario, contrasena, rol):
    conexion = conectarBD()  # Conecta a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Crea un cursor para ejecutar comandos SQL

            # Inserta un nuevo usuario en la tabla USUARIOS con los datos proporcionados
            miCursor.execute("INSERT INTO USUARIOS (NOMBRE_USUARIO, CONTRASENA, ROL) VALUES (?, ?, ?)",
                            (nombre_usuario, contrasena, rol))

            conexion.commit()  # Confirma los cambios en la base de datos
            conexion.close()  # Cierra la conexión con la base de datos
            print("¡Usuario agregado exitosamente!")  # Muestra un mensaje de éxito
        except sqlite3.Error as error:
            print("Error al agregar el usuario:", error)  # Maneja errores si surgen
            conexion.rollback()  # Realiza un rollback si hay errores
            conexion.close()  # Cierra la conexión con la base de datos

# Función para mostrar todos los usuarios
def mostrarUsuarios(eleccion):
    conexion = conectarBD()  # Conecta a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Crea un cursor para ejecutar comandos SQL

            # Selecciona todos los registros de la tabla USUARIOS
            miCursor.execute("SELECT * FROM USUARIOS")
            usuarios = miCursor.fetchall()  # Obtiene todos los registros

            conexion.close()  # Cierra la conexión con la base de datos

            if not usuarios:  # Si no hay registros
                print("No hay usuarios en la base de datos.")
            else:
                if eleccion==1:
                    print("Usuarios en la base de datos:")

                    print(f"{'ID':<5} {'Nombre Usuario':<20} {'Contraseña':<20} {'Rol':<10}")
                    print("-" * 65)
                    for usuarios in usuarios:# Itera sobre los registros y los muestra en pantalla
                        print(f"{usuarios[0]:<5} {usuarios[1]:<20} {usuarios[2]:<20} {usuarios[3]:<10}")
                elif eleccion==2:
                    lista_usuarios=[]
                    for usuario in usuarios:
                        lista_usuarios.append(usuario)
                    return lista_usuarios

        except sqlite3.Error as error:
            print("Error al mostrar los usuarios:", error)  # Maneja errores si surgen

# Función para actualizar la contraseña de un usuario
def actualizarContrasena(nombre_usuario, nueva_contrasena):
    conexion = conectarBD()  # Conecta a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Crea un cursor para ejecutar comandos SQL

            # Actualiza la contraseña del usuario con el nombre proporcionado
            miCursor.execute("UPDATE USUARIOS SET CONTRASENA = ? WHERE NOMBRE_USUARIO = ?",
                            (nueva_contrasena, nombre_usuario))

            conexion.commit()  # Confirma los cambios en la base de datos
            conexion.close()  # Cierra la conexión con la base de datos
            print("¡Contraseña actualizada exitosamente!")  # Muestra un mensaje de éxito
        except sqlite3.Error as error:
            print("Error al actualizar la contraseña:", error)  # Maneja errores si surgen
            conexion.rollback()  # Realiza un rollback si hay errores
            conexion.close()  # Cierra la conexión con la base de datos

# Función para eliminar un usuario
def eliminarUsuario(nombre_usuario):
    conexion = conectarBD()  # Conecta a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Crea un cursor para ejecutar comandos SQL

            # Elimina el usuario con el nombre proporcionado de la tabla USUARIOS
            miCursor.execute("DELETE FROM USUARIOS WHERE NOMBRE_USUARIO = ?", (nombre_usuario,))

            conexion.commit()  # Confirma los cambios en la base de datos
            conexion.close()  # Cierra la conexión con la base de datos
            print("¡Usuario eliminado exitosamente!")  # Muestra un mensaje de éxito
        except sqlite3.Error as error:
            print("Error al eliminar el usuario:", error)  # Maneja errores si surgen
            conexion.rollback()  # Realiza un rollback si hay errores
            conexion.close()  # Cierra la conexión con la base de datos

# Función para el menú de selección de operaciones
def menu():
    print("\n** MENÚ **")
    print("1. Agregar usuario")
    print("2. Mostrar usuarios")
    print("3. Actualizar contraseña")
    print("4. Eliminar usuario")
    print("5. Volver")

    opcion = input("Seleccione la opción que desee: ")
    return opcion

# Ejemplo de uso:
crearBD()  # Llama a la función para crear la base de datos si no existe




#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------




def mostrarBaseDatosVendedor():
    conexion = conectarDB1()  # Conectamos a la base de datos
    if conexion:
        try:
            miCursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL

            # Seleccionamos todos los registros de la tabla STOCKDISPONIBLE
            miCursor.execute("SELECT * FROM STOCKDISPONIBLE")
            articulos = miCursor.fetchall()  # Obtenemos todos los registros

            conexion.close()  # Cerramos la conexión con la base de datos
            
            if not articulos:  # Si no hay registros
                print("No hay artículos en el stock.")
            else:
                print(f"{'ID':<5} {'Nombre Artículo':<20} {'Precio':<10} {'Sección':<15} {'Marca':<15}")
                print("-" * 65)
                for articulo in articulos:
                    print(f"{articulo[0]:<5} {articulo[1]:<20} {articulo[2]:<10.2f} {articulo[3]:<15} {articulo[4]:<15}")
        except sqlite3.Error as error:
            print("Error al mostrar la base de datos:", error)  # Manejamos errores si surgen

# función para que el vendedor seleccione artículos y calcule el total a pagar
def seleccionarArticulosVendedor():
    total_pagar = 0
    while True:
        mostrarBaseDatosVendedor()  # Mostramos la base de datos al vendedor
        id_articulo = int(input("Ingrese el ID del artículo que desea agregar al carrito (0 para finalizar): "))
        if id_articulo == 0:
            break  # El vendedor ha finalizado la selección
        else:
            cantidad = int(input("Ingrese la cantidad de unidades: "))

            conexion = conectarDB1()
            if conexion:
                try:
                    miCursor = conexion.cursor()
                    # Obtenemos el precio del artículo seleccionado
                    miCursor.execute("SELECT PRECIO FROM STOCKDISPONIBLE WHERE ID = ?", (id_articulo,))
                    precio_unitario = miCursor.fetchone()[0]
                    # Calculamos el subtotal y lo sumamos al total a pagar
                    subtotal = cantidad * precio_unitario
                    total_pagar += subtotal
                    print(f"Artículo agregado al carrito. Subtotal: ${subtotal}")
                except sqlite3.Error as error:
                    print("Error al procesar la selección:", error)
                finally:
                    conexion.close()

    print(f"\nTotal a pagar: ${total_pagar}")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Usuario:
    def __init__(self, nombre_usuario, cargo):
        self.nombre_usuario = nombre_usuario
        self.cargo = cargo
    
    def inicio_de_sesion_correcto(self):
        print(f"Bienvenido {self.nombre_usuario}")
    
    def inicio_de_sesion_incorrecto(self):
        print("usuario/contraseña incorrecta")

if __name__ == "__main__":
    # Inicialización del contador general para el bucle principal
    
    contador_general = 0
    
    while contador_general == 0:
        # Solicitar al usuario si desea registrarse o iniciar sesión
        
        nuevo_viejo_usuario = input("Ingrese 'registrarse' o 'iniciar sesion': ").upper()
        
        if nuevo_viejo_usuario == "REGISTRARSE":
            # Obtener información del nuevo usuario
            
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            contrasena = input("Ingrese la contraseña: ")
            rol = input("Ingrese el rol (vendedor/administrador): ")
            
            # Llama a la función para agregar un usuario 
            
            agregarUsuario(nombre_usuario, contrasena, rol)
        
        elif nuevo_viejo_usuario == "INICIAR SESION":
            # Selección del tipo de usuario (administrador o vendedor)
            
            seleccionar_tipo_usuario = input("Ingrese como desea ingresar. Como administrador (AD) o vendedor (VE): ").upper()
            
            if seleccionar_tipo_usuario == "AD":
                usuario_tipo = "administrador"
            elif seleccionar_tipo_usuario == "VE":
                usuario_tipo = "vendedor"
            else:
                print("Tipo de usuario no válido. Intente nuevamente.")
                continue
            
            # Iniciar sesión con correo y contraseña
            
            mail = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            credenciales_validas = False
            
            # Validar las credenciales del usuario
            
            for usuario in mostrarUsuarios(2):  # 
                if mail == usuario[1] and contraseña == usuario[2]:
                    if usuario[3] == usuario_tipo:
                        # Crear una instancia de la clase Usuario
                        
                        p1 = Usuario(usuario[1], usuario[3])
                        p1.inicio_de_sesion_correcto()
                        
                        # Acciones específicas para vendedor o administrador
                        
                        if usuario_tipo == "vendedor":
                            print("vendedor")
                            # Llama a la función para seleccionar artículos del vendedor 
                            
                            seleccionarArticulosVendedor() 
                            credenciales_validas = True
                            break
                            
                        elif usuario_tipo == "administrador":
                            contador_inicial_admin = 0
                            while contador_inicial_admin == 0:
                                # Menú para el administrador
                                
                                divisor_secciones = input("Ingrese el área a la que desea entrar \nClientes-Proveedores(CP) / Stock(ST) / Usuario(US) / Cerrar App(FIN): ").upper()
                                
                                if divisor_secciones == "CP":
                                    print("Código para Clientes-Proveedores futura versión")
                                    contador_inicial_admin = 0
                                elif divisor_secciones == "ST":
                                    
                                    # Llama a la función principal del stock 
                                    
                                    programa()
                                    
                                    
                                elif divisor_secciones == "US":
                                    while True:
                                        
                                        # Menú de opciones para el administrador
                                        
                                        opcion = menu() 

                                        # Realizar acciones según la opción seleccionada
                                        
                                        if opcion == "1":
                                            # Llama a la función para agregar un usuario 
                                            
                                            nombre_usuario = input("Ingrese el nombre de usuario: ")
                                            contrasena = input("Ingrese la contraseña: ")
                                            rol = input("Ingrese el rol (vendedor/administrador): ")
                                            agregarUsuario(nombre_usuario, contrasena, rol)
                                            
                                        elif opcion == "2":
                                            # Llama a la función para mostrar todos los usuarios 
                                            
                                            mostrarUsuarios(1)
                                            
                                        elif opcion == "3":
                                            # Llama a la función para actualizar la contraseña 
                                            
                                            mostrarUsuarios(1)
                                            nombre_usuario = input("Ingrese el nombre de usuario para actualizar la contraseña: ")
                                            nueva_contrasena = input("Ingrese la nueva contraseña: ")
                                            actualizarContrasena(nombre_usuario, nueva_contrasena)
                                            
                                        elif opcion == "4":
                                            # Llama a la función para eliminar un usuario 
                                            
                                            mostrarUsuarios(1)
                                            nombre_usuario = input("Ingrese el nombre de usuario a eliminar: ")
                                            eliminarUsuario(nombre_usuario)
                                            
                                        elif opcion == "5":
                                            
                                            print("¡Hasta luego!")  # Sale del programa
                                            
                                            break
                                        else:
                                            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
                                
                                elif divisor_secciones == "FIN":
                                    # Finaliza los bucles cuando se cierra la aplicación
                                    
                                    contador_general = 1
                                    contador_inicial_admin = 1
                            credenciales_validas = True
                            break
            
            # Si las credenciales no son válidas, mostrar mensaje de inicio de sesión incorrecto
            
            if not credenciales_validas:
                p1 = Usuario("desconocido", "desconocido")
                p1.inicio_de_sesion_incorrecto()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------