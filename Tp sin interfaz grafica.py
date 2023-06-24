import mysql.connector

conexion = mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="series_netflix_tp")
miCursor = conexion.cursor()


opcion=0
print("Bienvenido al gestor de series")


def option():
    opcion=int(input("-")) 

    #añadir serie
    if opcion==1:
       
        Titulo = input("Ingrese el titulo de la serie: ")
        Genero = input("Ingrese el genero de la serie: ")
        Año = input("Ingrese el año de la serie: ")
        temporadas = input("Ingrese la cantidad de temporadas: ")
    
        cursor = conexion.cursor()
        accion = "INSERT INTO series ( Titulo, Genero, Año, temporadas) VALUES ( %s, %s, %s, %s)"
        datos = ( Titulo, Genero, Año, temporadas)
    
        cursor.execute(accion, datos)
        conexion.commit()
        print("Serie añadida exitosamente.")
        
        
    #mostrar catalogo
    elif opcion==2:
    
        cursor = conexion.cursor()
        accion = "SELECT * FROM series"
    
        cursor.execute(accion)
        series = cursor.fetchall()
    
        for serie in series:
            print(f"ID: {serie[0]}, Titulo: {serie[1]}, Genero: {serie[2]}, Año: {serie[3]}, temporadas: {serie[4]}")



    #editar serie
    elif opcion ==3:

        idserie = (input("Ingrese el ID de la serie a modificar: "))
        nuevo_titulo = input("Ingrese el nuevo titulo de la serie: ")
        nuevo_genero = input("Ingrese el nuevo genero: ")
        nuevo_año = input("Ingrese el año: ")
        nuevo_temporadas = input("Ingrese cantidad de temporadas: ")

        cursor = conexion.cursor()
        accion = "UPDATE series SET Titulo = %s, Genero = %s, Año = %s, temporadas = %s WHERE idseries = %s"
        datos = (nuevo_titulo, nuevo_genero, nuevo_año, nuevo_temporadas, idserie)
    
        cursor.execute(accion, datos)


        conexion.commit()
        print("Serie modificada exitosamente.")

    #eliminar serie
    elif opcion ==4:
        
        id_serie = input("Ingrese el ID de la serie a eliminar: ")
    
        cursor = conexion.cursor()
        accion = "DELETE FROM series WHERE idseries = %s"
        datos = (id_serie,)
    
        cursor.execute(accion, datos)
        conexion.commit()
        print("Serie eliminada exitosamente.")
    
    
    
    elif opcion ==5:
        print("¡Hasta luego!")

    elif opcion < 1 or opcion > 5:
        print("Opcion invalida. Marque una opcion correcta.")

    while opcion !=5:
        mainmenu()
        option()
        break
    
    
        
        

#menu principal de opciones
def mainmenu():
    print("Seleccione una opción")
    print("1 - Añadir Serie")
    print("2 - Mostrar Series") 
    print("3 - Editar Serie")   
    print("4 - Eliminar Serie") 
    print("5 - Cerrar")
   
    

mainmenu()
option()


conexion.close()
    

    











