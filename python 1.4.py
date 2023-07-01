import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import mysql.connector
from tkinter import messagebox as mb

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
    
    while Titulo == "":
        mb.showinfo("¡ERROR","Ingrese un titulo")
        break
    while Genero == "":
        mb.showinfo("¡ERROR!","Ingrese un género")
        break
    while Año == "":
        mb.showinfo("¡ERROR","Ingrese un año")
        break
    while temporadas == "":
        mb.showinfo("¡ERROR!","Ingrese cantidad de temporadas")
        break
    else:
        mb.showinfo("¡Titulo guardado!","¡Serie añadida exitosamente!")
        accion = "INSERT INTO series (Titulo, Genero, Año, temporadas) VALUES (%s, %s, %s, %s)"
        datos = (Titulo, Genero, Año, temporadas)

    miCursor.execute(accion, datos)
    conexion.commit()
    


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

    while idserie == "":
        mb.showinfo("¡ERROR","Ingrese un ID")
        break
    while nuevo_titulo == "":
        mb.showinfo("¡ERROR","Ingrese un titulo")
        break
    while nuevo_genero == "":
        mb.showinfo("¡ERROR!","Ingrese un género")
        break
    while nuevo_año == "":
        mb.showinfo("¡ERROR","Ingrese un año")
        break
    while nuevo_temporadas == "":
        mb.showinfo("¡ERROR!","Ingrese cantidad de temporadas")
        break
    else:
        mb.showinfo("¡Titulo guardado!","¡Serie añadida exitosamente!")
        accion = "UPDATE series SET Titulo = %s, Genero = %s, Año = %s, temporadas = %s WHERE idseries = %s"
        datos = (nuevo_titulo, nuevo_genero, nuevo_año, nuevo_temporadas, idserie)
    miCursor.execute(accion, datos)
    conexion.commit()
    

def eliminar_serie():
    id_serie = entry_id_eliminar.get()

    while id_serie == "":
        mb.showinfo("¡ERROR!","Ingrese la ID de la serie a eliminar")
    
    else:
        accion = "DELETE FROM series WHERE idseries = %s"
        datos = (id_serie,)
        mb.showinfo("¡Titulo eliminado!","¡Serie eliminada exitosamente!")

    miCursor.execute(accion, datos)
    conexion.commit()
    



# Interfaz gráfica

root = tk.Tk()
root.title("Gestor de Series")

style = ttk.Style()
style.configure("Black.TFrame", background="black")

# Crear pestañas
tab_control = ttk.Notebook(root)

# Pestaña para añadir serie
tab_add_serie = ttk.Frame(tab_control, style="Black.TFrame")
tab_control.add(tab_add_serie, text='Añadir Serie')
# Cargar el logo

logo_image = tk.PhotoImage(file="logo.png")  # Reemplaza "logo.png" con la ruta de tu propia imagen

# Crear un widget de etiqueta para mostrar el logo
logo_label = tk.Label(tab_add_serie, image=logo_image, background="black", width="500px", height="200px")
logo_label.grid(row=0, column=3, columnspan=5, sticky="w")

label_titulo = tk.Label(tab_add_serie, text="Título:", background="black", foreground="#B9B9B9")
label_titulo.grid(row=1, column=3, sticky="e")
entry_titulo = tk.Entry(tab_add_serie, background="#B9B9B9", foreground="black")
entry_titulo.grid(row=1, column=4, sticky="e", pady=5)

label_genero = tk.Label(tab_add_serie, text="Género:", background="black", foreground="#B9B9B9")
label_genero.grid(row=2, column=3, sticky="e")
entry_genero = tk.Entry(tab_add_serie, background="#B9B9B9", foreground="black")
entry_genero.grid(row=2, column=4, sticky="e", pady=5)

label_año = tk.Label(tab_add_serie, text="Año:", background="black", foreground="#B9B9B9")
label_año.grid(row=3, column=3, sticky="e")
entry_año = tk.Entry(tab_add_serie, background="#B9B9B9", foreground="black")
entry_año.grid(row=3, column=4, sticky="e", pady=5)

label_temporadas = tk.Label(tab_add_serie, text="Temporadas:", background="black", foreground="#B9B9B9")
label_temporadas.grid(row=4, column=3, sticky="e")
entry_temporadas = tk.Entry(tab_add_serie, background="#B9B9B9", foreground="black")
entry_temporadas.grid(row=4, column=4, sticky="e", pady=5)

btn_add_serie = tk.Button(tab_add_serie, text="Añadir Serie", command=agregar_serie, background="black", foreground="#B9B9B9")
btn_add_serie.grid(row=5, column=4, columnspan=2, sticky="w", padx=(70,0), pady=30)


# Crear el Treeview para mostrar las series pestaña 1
treeview = ttk.Treeview(tab_add_serie, columns=("ID", "Titulo", "Genero", "Año", "Temporadas"), show="headings")
treeview.grid(row=6, column=1, columnspan=6, rowspan=1, sticky="w", padx=(140,0))

# Crear la barra de desplazamiento vertical
scrollbar = ttk.Scrollbar(tab_add_serie, orient="vertical", command=treeview.yview)
scrollbar.grid(row=6, column=7, sticky="ns")

# Configurar el Treeview para usar la barra de desplazamiento
treeview.configure(yscrollcommand=scrollbar.set, height=4)

# Botón para mostrar las series pestaña 1
btn_show_series = tk.Button(tab_add_serie, text="Mostrar Series", command=mostrar_series, background="black", foreground="#B9B9B9")
btn_show_series.grid(row=7, column=4, columnspan=2, sticky="w", padx=(60,0), pady=30)



# Pestaña para editar serie
tab_edit_serie = ttk.Frame(tab_control, style="Black.TFrame")
tab_control.add(tab_edit_serie, text='Editar Serie')

# Crear un widget de etiqueta para mostrar el logo
logo_label = tk.Label(tab_edit_serie, image=logo_image, background="black", width="500px", height="200px")
logo_label.grid(row=0, column=3, columnspan=5, sticky="w")

label_id = tk.Label(tab_edit_serie, text="ID a modificar:", background="black", foreground="#B9B9B9")
label_id.grid(row=1, column=3, sticky="e")
entry_id = tk.Entry(tab_edit_serie, background="#B9B9B9", foreground="black")
entry_id.grid(row=1, column=4, sticky="e", pady=5)

label_nuevo_titulo = tk.Label(tab_edit_serie, text="Nuevo título:", background="black", foreground="#B9B9B9")
label_nuevo_titulo.grid(row=2, column=3, sticky="e")
entry_nuevo_titulo = tk.Entry(tab_edit_serie, background="#B9B9B9", foreground="black")
entry_nuevo_titulo.grid(row=2, column=4, sticky="e", pady=5)

label_nuevo_genero = tk.Label(tab_edit_serie, text="Nuevo género:", background="black", foreground="#B9B9B9")
label_nuevo_genero.grid(row=3, column=3, sticky="e")
entry_nuevo_genero = tk.Entry(tab_edit_serie, background="#B9B9B9", foreground="black")
entry_nuevo_genero.grid(row=3, column=4, sticky="e", pady=5)

label_nuevo_año = tk.Label(tab_edit_serie, text="Nuevo año:", background="black", foreground="#B9B9B9")
label_nuevo_año.grid(row=4, column=3, sticky="e")
entry_nuevo_año = tk.Entry(tab_edit_serie, background="#B9B9B9", foreground="black")
entry_nuevo_año.grid(row=4, column=4, sticky="e", pady=5)

label_nuevo_temporadas = tk.Label(tab_edit_serie, text="Nuevas temporadas:", background="black", foreground="#B9B9B9")
label_nuevo_temporadas.grid(row=5, column=3, sticky="e")
entry_nuevo_temporadas = tk.Entry(tab_edit_serie, background="#B9B9B9", foreground="black")
entry_nuevo_temporadas.grid(row=5, column=4, sticky="e", pady=5)

btn_edit_serie = tk.Button(tab_edit_serie, text="Editar Serie", command=editar_serie, background="black", foreground="#B9B9B9")
btn_edit_serie.grid(row=6, column=4, columnspan=2, sticky="w", padx=(70,0), pady=30)

# Crear el Treeview para mostrar las series pestaña 2
treeview_edit = ttk.Treeview(tab_edit_serie, columns=("ID", "Titulo", "Genero", "Año", "Temporadas"), show="headings")
treeview_edit.grid(row=7, column=1, columnspan=6, sticky="w", padx=(170,0))

treeview_edit.configure(yscrollcommand=scrollbar.set, height=4)


# Pestaña para eliminar serie
tab_delete_serie = ttk.Frame(tab_control, style="Black.TFrame")
tab_control.add(tab_delete_serie, text='Eliminar Serie')

# Crear un widget de etiqueta para mostrar el logo
logo_label = tk.Label(tab_delete_serie, image=logo_image, background="black", width="500px", height="200px")
logo_label.grid(row=0, column=3, columnspan=5, sticky="w")

label_id_eliminar = tk.Label(tab_delete_serie, text="ID a eliminar:", background="black", foreground="#B9B9B9")
label_id_eliminar.grid(row=1, column=3, sticky="e")
entry_id_eliminar = tk.Entry(tab_delete_serie, background="#B9B9B9", foreground="black")
entry_id_eliminar.grid(row=1, column=4, sticky="e", pady=5)

btn_delete_serie = tk.Button(tab_delete_serie, text="Eliminar Serie", command=eliminar_serie, background="black", foreground="#B9B9B9")
btn_delete_serie.grid(row=2, column=4, columnspan=2, sticky="w", padx=(70,0), pady=30)

# Agregar pestañas a la ventana principal
tab_control.pack(expand=1, fill='both')

# Crear el Treeview para mostrar las series pestaña 3
treeview_delete = ttk.Treeview(tab_delete_serie, columns=("ID", "Titulo", "Genero", "Año", "Temporadas"), show="headings")
treeview_delete.grid(row=3, column=1, columnspan=6, sticky="w", padx=(170,0))

treeview_delete.configure(yscrollcommand=scrollbar.set, height=4)

# Definir las columnas del Treeview
treeview.heading("ID", text="ID")
treeview.heading("Titulo", text="Título")
treeview.heading("Genero", text="Género")
treeview.heading("Año", text="Año")
treeview.heading("Temporadas", text="Temporadas")


# Botón para mostrar las series pestaña 2
btn_show_series = tk.Button(tab_edit_serie, text="Mostrar Series", command=mostrar_series, background="black", foreground="#B9B9B9")
btn_show_series.grid(row=8, column=0, columnspan=2, sticky="e")

# Botón para mostrar las series pestaña 3
btn_show_series = tk.Button(tab_delete_serie, text="Mostrar Series", command=mostrar_series, background="black", foreground="#B9B9B9")
btn_show_series.grid(row=4, column=0, columnspan=2, sticky="e")

root.mainloop()
conexion.close()
