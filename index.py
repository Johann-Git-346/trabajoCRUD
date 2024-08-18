import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class Davista:
    def __init__(self, root):
        self.root = root
        self.root.title("Nombre de la Empresa")
        self.root.geometry("800x600")

        self.create_top_frame()
        self.create_menu_frame()
        self.create_sidebar_frame()
        self.create_catalog_frame()
        

    def create_top_frame(self):
        """ Crear el marco superior para el nombre de la empresa y la imagen del logo. """
        self.frame_top = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame_top.pack(side=tk.TOP, fill=tk.X)

        company_name = tk.Label(self.frame_top, text="Nombre de la Empresa", font=("Arial", 24))
        company_name.pack(side=tk.LEFT, padx=10, pady=10)

        # Logo (espacio reservado)
        logo = tk.Label(self.frame_top, text="Logo", width=20, height=10, bg="lightgray")
        logo.pack(side=tk.RIGHT, padx=10, pady=10)

    def create_menu_frame(self):
        """ Crear el marco para el menú de navegación. """
        self.frame_menu = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame_menu.pack(side=tk.TOP, fill=tk.X)

        # Botones de navegación
        menu_buttons = ["Home", "Products", "About", "Contact"]
        commands = [self.home_command, self.products_command, self.about_command, self.contact_command]

        for text, command in zip(menu_buttons, commands):
            tk.Button(self.frame_menu, text=text, command=command).grid(row=0, column=menu_buttons.index(text), padx=10, pady=5)

        # Configurar las columnas para que se expandan igualmente
        for i in range(len(menu_buttons)):
            self.frame_menu.grid_columnconfigure(i, weight=1)

    def create_sidebar_frame(self):
        """ Crear el marco para la barra lateral izquierda y añadir botones. """
        self.frame_sidebar = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame_sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Añadir botones de la barra lateral
        sidebar_buttons = ["Apps", "Games", "Movies", "Books", "Newspapers"]
        sidebar_commands = [self.apps_command, self.games_command, self.movies_command, self.books_command, self.newspapers_command]

        for text, command in zip(sidebar_buttons, sidebar_commands):
            tk.Button(self.frame_sidebar, text=text, command=command).pack(fill=tk.X, padx=5, pady=5)

        # Controles multimedia (espacios reservados)
        multimedia_frame = tk.Frame(self.frame_sidebar)
        multimedia_frame.pack(fill=tk.X, padx=5, pady=5)

    def create_catalog_frame(self):
        """ Crear el marco para las categorías y el catálogo. """
        self.frame_catalog = tk.Frame(self.root)
        self.frame_catalog.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Crear el marco de categorías
        self.frame_categories = tk.Frame(self.frame_catalog, relief=tk.RAISED, borderwidth=1)
        self.frame_categories.pack(side=tk.TOP, fill=tk.X)

        # Añadir botones de categorías
        categories = ["Categoría 1", "Categoría 2", "Categoría 3", "Categoría 4", "Categoría 5"]
        for category in categories:
            tk.Button(self.frame_categories, text=category).pack(side=tk.LEFT, padx=10, pady=5)

        # Crear el título del catálogo
        catalog_title = tk.Label(self.frame_catalog, text="Título del Catálogo", font=("Arial", 16))
        catalog_title.pack(side=tk.TOP, pady=10)

        # Crear el marco para los productos
        self.frame_products = tk.Frame(self.frame_catalog)
        self.frame_products.pack(fill=tk.BOTH, expand=True)

        # URLs válidas de las imágenes
        image_urls = [
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100"
        ]
        
        # Descargar y procesar imágenes
        self.images = []
        for url in image_urls:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Asegura que la solicitud fue exitosa
                img_data = response.content
                img = Image.open(BytesIO(img_data)).resize((100, 100))
                self.images.append(ImageTk.PhotoImage(img))
            except (requests.exceptions.RequestException, Image.UnidentifiedImageError) as e:
                print(f"Error al cargar la imagen desde {url}: {e}")
                self.images.append(None)

        # Añadir productos (simulación de imágenes y texto)
        for i in range(2):  # filas
            row = tk.Frame(self.frame_products)
            row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            for j in range(7):  # columnas
                product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
                product_frame.pack(side=tk.LEFT, padx=5, pady=5)

                # Asignar una imagen diferente a cada producto
                img_index = (i * 10) + j  # Calcular el índice de la imagen
                if img_index < len(self.images) and self.images[img_index] is not None:
                    img_label = tk.Label(product_frame, image=self.images[img_index])
                else:
                    img_label = tk.Label(product_frame, text="Sin Imagen", bg="lightgray", width=10, height=5)
                
                img_label.pack()

                info_label = tk.Label(product_frame, text=f"Producto {img_index + 1}\nCategoría\nPrecio", justify=tk.LEFT)
                info_label.pack()

    # Métodos de comando para los botones
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

# Crear la instancia de la clase Davista
app = Davista(root)

# Iniciar el bucle principal de la aplicación
root.mainloop()

