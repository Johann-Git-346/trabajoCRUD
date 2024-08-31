import tkinter as tk
from PIL import Image, ImageTk
import os

class Davista:
    def __init__(self, root):
        self.root = root
        self.root.title("TecnoNube")
        self.root.geometry("800x600")

        self.create_top_frame()
        self.create_menu_frame()
        self.create_sidebar_frame()
        self.create_catalog_frame()

    def create_top_frame(self):
        self.baner = tk.Frame(self.root, borderwidth=1)
        self.baner.pack(side=tk.TOP)
        
        izespacio = tk.Frame(self.baner)
        izespacio.pack(side=tk.LEFT)
        
        nombre = tk.Label(self.baner, text="TecnoNube", font=("Arial", 26), anchor="center")
        nombre.pack(side=tk.LEFT)
        
        etiqueta = tk.Label(self.baner)
        etiqueta.pack(side=tk.LEFT)
        
        rutaimagen = 'imagenes/logoc.png'
        
        if not os.path.exists(rutaimagen):
            print(f"Error: La ruta de la imagen no existe: {rutaimagen}")
            return
        
        try:
            imagen = Image.open(rutaimagen)
            imagen = imagen.resize((100, 100))
            self.imagen_tk = ImageTk.PhotoImage(imagen)  # Mantén la referencia a la imagen
            
            etiqueta_imagen = tk.Label(self.baner, image=self.imagen_tk)
            etiqueta_imagen.pack(side=tk.RIGHT, pady=10)
        
        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")

    def create_menu_frame(self):
        self.frame_menu = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame_menu.pack(side=tk.TOP, fill=tk.X)

        menu_buttons = ["Inicio", "Productos", "Perfil", "Contacto"]
        commands = [self.home_command, self.products_command, self.about_command, self.contact_command]

        for text, command in zip(menu_buttons, commands):
            tk.Button(self.frame_menu, text=text, command=command).grid(row=0, column=menu_buttons.index(text), padx=10, pady=5)

        for i in range(len(menu_buttons)):
            self.frame_menu.grid_columnconfigure(i, weight=1)

    def create_sidebar_frame(self):
        self.frame_sidebar = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame_sidebar.pack(side=tk.LEFT, fill=tk.Y)

        sidebar_buttons = ["Apps", "Juegos", "Peliculas", "Libros", "Noticias"]
        sidebar_commands = [self.apps_command, self.games_command, self.movies_command, self.books_command, self.newspapers_command]

        for text, command in zip(sidebar_buttons, sidebar_commands):
            tk.Button(self.frame_sidebar, text=text, command=command).pack(fill=tk.X, padx=5, pady=5)

        multimedia_frame = tk.Frame(self.frame_sidebar)
        multimedia_frame.pack(fill=tk.X, padx=5, pady=5)

    def create_catalog_frame(self):
        self.frame_catalog = tk.Frame(self.root)
        self.frame_catalog.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.frame_categories = tk.Frame(self.frame_catalog, relief=tk.RAISED, borderwidth=1)
        self.frame_categories.pack(side=tk.TOP, fill=tk.X)

        categories = ["Smartphones", "Tablets", "Laptops", "Monitores", "Cámaras", "Audífonos", "Cargadores"]
        for category in categories:
            tk.Button(self.frame_categories, text=category).pack(side=tk.LEFT, padx=10, pady=5)

        catalog_title = tk.Label(self.frame_catalog, text="Título del Catálogo", font=("Arial", 16))
        catalog_title.pack(side=tk.TOP, pady=10)

        self.frame_products = tk.Frame(self.frame_catalog)
        self.frame_products.pack(fill=tk.BOTH, expand=True)

        # Cargar una sola vez la imagen productoc.png
        product_image_path = 'imagenes/productoc.png'  # Ruta a la imagen que se utilizará para todos los productos
        
        print("Intentando cargar la imagen desde:", product_image_path)
        if not os.path.exists(product_image_path):
            print(f"Error: La ruta de la imagen no existe: {product_image_path}")
            return
        
        try:
            imagen = Image.open(product_image_path)
            print("Imagen cargada correctamente")
            imagen = imagen.resize((100, 100))  # Redimensiona la imagen si es necesario
            self.product_image = ImageTk.PhotoImage(imagen)  # Mantén la referencia a la imagen
        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")
            self.product_image = None

        # Añadir productos (simulación de imágenes y texto)
        for i in range(2):  # filas
            row = tk.Frame(self.frame_products)
            row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            for j in range(7):  # columnas
                product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
                product_frame.pack(side=tk.LEFT, padx=5, pady=5)

                if self.product_image is not None:
                    img_label = tk.Label(product_frame, image=self.product_image)
                else:
                    img_label = tk.Label(product_frame, text="Sin Imagen", bg="lightgray", width=10, height=5)
                
                img_label.pack()

                info_label = tk.Label(product_frame, text=f"Producto {(i * 7) + j + 1}\nCategoría\nPrecio", justify=tk.LEFT)
                info_label.pack()

    def home_command(self):
        print("Home button clicked")

    def products_command(self):
        print("Products button clicked")

    def about_command(self):
        print("About button clicked")

    def contact_command(self):
        print("Contact button clicked")

    def apps_command(self):
        print("Apps button clicked")

    def games_command(self):
        print("Games button clicked")

    def movies_command(self):
        print("Movies button clicked")

    def books_command(self):
        print("Books button clicked")

    def newspapers_command(self):
        print("Newspapers button clicked")

# Crear la ventana principal
root = tk.Tk()
app = Davista(root)
root.mainloop()