import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import pandas as pd
class VistaTablas1:
    def __init__(self,objController):
        self.objController=objController

    def iniciarTablas(self):
        # Crear la ventana principal
        self.rootTablas = tk.Tk()
        self.rootTablas.title("TecnoNube")
        self.rootTablas.geometry("800x600")

        self.rootTablas.state('zoomed')

        self.create_top_frame()
        self.create_menu_frame()
        """self.create_sidebar_frame()"""
        self.create_catalog_frame()
        self.crearMarcoInferior()

        self.rootTablas.mainloop()

    def create_top_frame(self):
        """ Crear el marco superior para el nombre de la empresa y la imagen del logo. """
        self.frame_top = tk.Frame(self.rootTablas, relief=tk.RAISED, borderwidth=1)
        self.frame_top.pack(side=tk.TOP, fill=tk.X)
        self.frame_top.config(background="#333333")

        # Añadir un widget de Frame central vacío para centrar los otros widgets
        spacer_left = tk.Frame(self.frame_top)
        spacer_left.pack(side=tk.LEFT, expand=True)
        spacer_left.config(background="#333333")

        company_name = tk.Label(self.frame_top, text="TecnoNube", font=("Arial", 24,"bold"),foreground="#FFFFFF", anchor="center")
        company_name.pack(side=tk.LEFT, padx=10, pady=10)
        company_name.config(background="#333333")

        logo = tk.Frame(self.frame_top,width=20,height=20)
        logo.pack(side=tk.RIGHT, padx=10, pady=10)
        logo.config(background="#333333")
        # Añadir un widget de Frame central vacío para centrar los otros widgets
        spacer_right = tk.Frame(self.frame_top)
        spacer_right.pack(side=tk.RIGHT, expand=True)
        spacer_right.config(background="#333333")
            

        etiqueta = tk.Label(logo)
        etiqueta.pack(side=tk.RIGHT)
        etiqueta.config(background="#333333")

        self.rutaimagen= "LOGO2.jpg"

        if not os.path.exists(self.rutaimagen):
            print(f"Error: La ruta de la imagen no existe: {self.rutaimagen}")
            return
        

        try:
            imagen2 = Image.open(self.rutaimagen)
            imagen2 = imagen2.resize((155, 130))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen2) # Mantén la referencia a la imagen
            
            etiqueta_imagen = tk.Label(logo, image=self.imagen_tk2)
            etiqueta_imagen.pack()

        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")

    def create_menu_frame(self):
        # Crear el marco para el menú de navegación
        frame_menu = tk.Frame(self.rootTablas, relief=tk.RAISED, borderwidth=0.5)
        frame_menu.pack(side=tk.TOP, fill=tk.X)
        frame_menu.config(background="#f5f5f5")

        # Botones de navegación
        menu_buttons = ["Cerrar Sesion"]
        commands = [self.CerrarSesion]

        for text, command in zip(menu_buttons, commands):
            tk.Button(frame_menu, text=text,cursor="hand2",bg="#333333",foreground="#FFFFFF",font=("Arial", 10,"bold") ,command=command).grid(row=0, column=menu_buttons.index(text), padx=10, pady=5)

        # Configurar las columnas para que se expandan igualmente
        for i in range(len(menu_buttons)):
            frame_menu.grid_columnconfigure(i, weight=1)
    
    def create_catalog_frame(self):
        # Crear el marco para las categorías y el informe de productos
        frame_report = tk.Frame(self.rootTablas)
        frame_report.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        frame_report.config(background="#f5f5f5")

        # Crear el título del informe
        report_title = tk.Label(frame_report, text="Informe de Productos", font=("Arial", 16,"bold"),foreground="#FFFFFF")
        report_title.pack(side=tk.TOP, pady=10)
        report_title.config(background="#333333")

        # Crear el marco para los informes de más vendidos y menos vendidos
        frame_products = tk.Frame(frame_report)
        frame_products.pack(fill=tk.BOTH, expand=True)

        # Supongamos que tienes un método en tu controlador para obtener los productos más vendidos y menos vendidos
        self.mas_vendidos, self.menos_vendidos = self.objController.obtenerMasYMenosVendidos()


        # Tabla de Más Vendidos
        frame_mas_vendidos = tk.Frame(frame_products)
        frame_mas_vendidos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
        frame_mas_vendidos.config(background="#333333")

        mas_vendidos_title = tk.Label(frame_mas_vendidos, text="Más Vendidos", font=("Arial", 14), foreground="#FFFFFF")
        mas_vendidos_title.pack(side=tk.TOP, pady=5)
        mas_vendidos_title.config(background="#333333")

        self.mas_vendidos_tree = ttk.Treeview(frame_mas_vendidos, columns=("Producto", "Cantidad", "Categoria"), show="headings")
        self.mas_vendidos_tree.heading("Producto", text="Nombre Producto")
        self.mas_vendidos_tree.heading("Cantidad", text="Cantidad")
        self.mas_vendidos_tree.heading("Categoria", text="Categoria")

        # Insertar datos en la tabla de Más Vendidos
        for producto in self.mas_vendidos:
            self.mas_vendidos_tree.insert("", "end", values=(producto[1], producto[4], producto[3]))  # Ajusta los índices según tu estructura de datos

        self.mas_vendidos_tree.pack(fill=tk.BOTH, expand=True)

        # Tabla de Menos Vendidos
        frame_menos_vendidos = tk.Frame(frame_products)
        frame_menos_vendidos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
        frame_menos_vendidos.config(background="#333333")

        menos_vendidos_title = tk.Label(frame_menos_vendidos, text="Menos Vendidos", font=("Arial", 14), foreground="#FFFFFF")
        menos_vendidos_title.pack(side=tk.TOP, pady=5)
        menos_vendidos_title.config(background="#333333")

        self.menos_vendidos_tree = ttk.Treeview(frame_menos_vendidos, columns=("Producto", "Cantidad", "Categoria"), show="headings")
        self.menos_vendidos_tree.heading("Producto", text="Nombre Producto")
        self.menos_vendidos_tree.heading("Cantidad", text="Cantidad")
        self.menos_vendidos_tree.heading("Categoria", text="Categoria")

        # Insertar datos en la tabla de Menos Vendidos
        for producto in self.menos_vendidos:
            self.menos_vendidos_tree.insert("", "end", values=(producto[1], producto[4], producto[3]))  # Ajusta los índices según tu estructura de datos

        self.menos_vendidos_tree.pack(fill=tk.BOTH, expand=True)

        # Botón para generar el informe
        generate_button = tk.Button(frame_report, text="Generar Informe", cursor="hand2", bg="#FFD700", foreground="black",command=self.crearArchivo)
        generate_button.pack(side=tk.BOTTOM, pady=10)

    def crearArchivo(self):
        # Obtener datos de los Treeview
        mas_vendidos = []
        for item in self.mas_vendidos_tree.get_children():
            producto = self.mas_vendidos_tree.item(item, "values")
            mas_vendidos.append({
                "Producto": producto[0],
                "Cantidad": producto[1],
                "Categoria": producto[2]
            })

        menos_vendidos = []
        for item in self.menos_vendidos_tree.get_children():
            producto = self.menos_vendidos_tree.item(item, "values")
            menos_vendidos.append({
                "Producto": producto[0],
                "Cantidad": producto[1],
                "Categoria": producto[2]
            })

        self.objController.generarInforme(mas_vendidos, menos_vendidos)
        messagebox.showinfo("Informe listo","informe creado con exito")


    def crearMarcoInferior(self):
        # Crear el marco inferior para la barra de navegación
        frame_bottom = tk.Frame(self.rootTablas, relief=tk.RAISED, borderwidth=1)
        frame_bottom.pack(side=tk.BOTTOM, fill=tk.X)


    def CerrarSesion(self):
        self.mensajeCerrrarSesion=tk.Toplevel()
        self.mensajeCerrrarSesion.title("¿seguro?")
        self.mensajeCerrrarSesion.geometry("350x250")
        self.mensajeCerrrarSesion.config(bg="lightblue")
        self.respuesta=tk.StringVar()
        self.contenedorMensaje=tk.Frame(self.mensajeCerrrarSesion,bg="lightblue")
        self.contenedorMensaje.pack()
        self.labelMensaje=tk.Label(self.contenedorMensaje,text="¿Esta seguro que desea cerrar sesion?",font=("Arial", 12,"bold"),bg="lightblue")
        self.labelMensaje.pack(padx=10,pady=10)
        self.botonSi=tk.Button(self.contenedorMensaje,text="SI",command=self.salirTodo,bg="red",font=("Arial", 12, "bold"))
        self.botonSi.pack(padx=10,pady=10)
        self.botonNo=tk.Button(self.contenedorMensaje,text="NO",command=self.destruirMensaje,bg="lightgreen", font=("Arial", 12, "bold"))
        self.botonNo.pack(padx=10,pady=10)
        
    def destruirMensaje(self):
        self.mensajeCerrrarSesion.destroy()

    def salirTodo(self):
        self.mensajeCerrrarSesion.destroy()
        self.rootTablas.destroy()
        self.objController.mostrarLogin() 

