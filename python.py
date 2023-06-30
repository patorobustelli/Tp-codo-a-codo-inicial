import tkinter as tk
from tkinter import ttk
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Neno1026",
    database="series_netflix",
    port="3307"
)

miCursor = conexion.cursor()

# Funciones

def agregar_serie():
    Titulo = entry_titulo.get()
    Genero = entry_genero.get()
    Año = entry_año.get()
    temporadas = entry_temporadas.get()

    accion = "INSERT INTO series (Titulo, Genero, Año, temporadas) VALUES (%s, %s, %s, %s)"
    datos = (Titulo, Genero, Año, temporadas)

    miCursor.execute(accion, datos)
    conexion.commit()
    print("Serie añadida exitosamente.")


def mostrar_series():
    accion = "SELECT * FROM series"

    miCursor.execute(accion)
    series = miCursor.fetchall()

    # Borrar las filas existentes en el Treeview de la pestaña "agregar series"
    for row in treeview.get_children():
        treeview.delete(row)

    # Borrar las filas existentes en el Treeview de la pestaña "Editar Serie"
    for row in treeview_edit.get_children():
        treeview_edit.delete(row)

    # Borrar las filas existentes en el Treeview de la pestaña "Eliminar Serie"
    for row in treeview_delete.get_children():
        treeview_delete.delete(row)

    # Insertar las series en el Treeview de la pestaña "Añadir Serie"
    for serie in series:
        treeview.insert("", "end", values=serie)

    # Insertar las series en el Treeview de la pestaña "Editar Serie"
    for serie in series:
        treeview_edit.insert("", "end", values=serie)

    # Insertar las series en el Treeview de la pestaña "Eliminar Serie"
    for serie in series:
        treeview_delete.insert("", "end", values=serie)


def editar_serie():
    idserie = entry_id.get()
    nuevo_titulo = entry_nuevo_titulo.get()
    nuevo_genero = entry_nuevo_genero.get()
    nuevo_año = entry_nuevo_año.get()
    nuevo_temporadas = entry_nuevo_temporadas.get()

    accion = "UPDATE series SET Titulo = %s, Genero = %s, Año = %s, temporadas = %s WHERE idseries = %s"
    datos = (nuevo_titulo, nuevo_genero, nuevo_año, nuevo_temporadas, idserie)

    miCursor.execute(accion, datos)
    conexion.commit()
    print("Serie modificada exitosamente.")

def eliminar_serie():
    id_serie = entry_id_eliminar.get()

    accion = "DELETE FROM series WHERE idseries = %s"
    datos = (id_serie,)

    miCursor.execute(accion, datos)
    conexion.commit()
    print("Serie eliminada exitosamente.")

def cerrar_app():
    print("¡Hasta luego!")
    conexion.close()
    root.destroy()


# Interfaz gráfica

root = tk.Tk()
root.title("Gestor de Series")

# Crear pestañas
tab_control = ttk.Notebook(root)

# Pestaña para añadir serie
tab_add_serie = ttk.Frame(tab_control)
tab_control.add(tab_add_serie, text='Añadir Serie')

label_titulo = tk.Label(tab_add_serie, text="Título:")
label_titulo.pack()
entry_titulo = tk.Entry(tab_add_serie)
entry_titulo.pack()

label_genero = tk.Label(tab_add_serie, text="Género:")
label_genero.pack()
entry_genero = tk.Entry(tab_add_serie)
entry_genero.pack()

label_año = tk.Label(tab_add_serie, text="Año:")
label_año.pack()
entry_año = tk.Entry(tab_add_serie)
entry_año.pack()

label_temporadas = tk.Label(tab_add_serie, text="Temporadas:")
label_temporadas.pack()
entry_temporadas = tk.Entry(tab_add_serie)
entry_temporadas.pack()

btn_add_serie = tk.Button(tab_add_serie, text="Añadir Serie", command=agregar_serie)
btn_add_serie.pack()

# Pestaña para editar serie
tab_edit_serie = ttk.Frame(tab_control)
tab_control.add(tab_edit_serie, text='Editar Serie')

label_id = tk.Label(tab_edit_serie, text="ID a modificar:")
label_id.pack()
entry_id = tk.Entry(tab_edit_serie)
entry_id.pack()

label_nuevo_titulo = tk.Label(tab_edit_serie, text="Nuevo título:")
label_nuevo_titulo.pack()
entry_nuevo_titulo = tk.Entry(tab_edit_serie)
entry_nuevo_titulo.pack()

label_nuevo_genero = tk.Label(tab_edit_serie, text="Nuevo género:")
label_nuevo_genero.pack()
entry_nuevo_genero = tk.Entry(tab_edit_serie)
entry_nuevo_genero.pack()

label_nuevo_año = tk.Label(tab_edit_serie, text="Nuevo año:")
label_nuevo_año.pack()
entry_nuevo_año = tk.Entry(tab_edit_serie)
entry_nuevo_año.pack()

label_nuevo_temporadas = tk.Label(tab_edit_serie, text="Nuevas temporadas:")
label_nuevo_temporadas.pack()
entry_nuevo_temporadas = tk.Entry(tab_edit_serie)
entry_nuevo_temporadas.pack()

btn_edit_serie = tk.Button(tab_edit_serie, text="Editar Serie", command=editar_serie)
btn_edit_serie.pack()

# Pestaña para eliminar serie
tab_delete_serie = ttk.Frame(tab_control)
tab_control.add(tab_delete_serie, text='Eliminar Serie')

label_id_eliminar = tk.Label(tab_delete_serie, text="ID a eliminar:")
label_id_eliminar.pack()
entry_id_eliminar = tk.Entry(tab_delete_serie)
entry_id_eliminar.pack()

btn_delete_serie = tk.Button(tab_delete_serie, text="Eliminar Serie", command=eliminar_serie)
btn_delete_serie.pack()

# Agregar pestañas a la ventana principal
tab_control.pack(expand=1, fill='both')

# Crear el Treeview para mostrar las series pestaña 1
treeview = ttk.Treeview(tab_add_serie, columns=("ID", "Titulo", "Genero", "Año", "Temporadas"), show="headings")
treeview.pack()

# Crear el Treeview para mostrar las series pestaña 2
treeview_edit = ttk.Treeview(tab_edit_serie, columns=("ID", "Titulo", "Genero", "Año", "Temporadas"), show="headings")
treeview_edit.pack()

# Crear el Treeview para mostrar las series pestaña 3
treeview_delete = ttk.Treeview(tab_delete_serie, columns=("ID", "Titulo", "Genero", "Año", "Temporadas"), show="headings")
treeview_delete.pack()

# Definir las columnas del Treeview
treeview.heading("ID", text="ID")
treeview.heading("Titulo", text="Título")
treeview.heading("Genero", text="Género")
treeview.heading("Año", text="Año")
treeview.heading("Temporadas", text="Temporadas")

# Botón para mostrar las series pestaña 1
btn_show_series = tk.Button(tab_add_serie, text="Mostrar Series", command=mostrar_series)
btn_show_series.pack()

# Botón para mostrar las series pestaña 2
btn_show_series = tk.Button(tab_edit_serie, text="Mostrar Series", command=mostrar_series)
btn_show_series.pack()

# Botón para mostrar las series pestaña 3
btn_show_series = tk.Button(tab_delete_serie, text="Mostrar Series", command=mostrar_series)
btn_show_series.pack()

root.mainloop()
