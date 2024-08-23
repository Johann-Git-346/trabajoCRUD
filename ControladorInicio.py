from ModeloInicio import ModeloUsuario
from VistaInicio import VistaUsuario
# Las siguientes vistas deberán ser creadas para los diferentes roles
# from VistaAdmin import VistaAdmin
# from VistaVendedor import VistaVendedor
# from VistaCliente import VistaCliente

class Controlador:
    def __init__(self, conexion):
        self.modelo = ModeloUsuario(conexion)
        self.vista = VistaUsuario(self)

    def iniciar(self):
        self.vista.iniciar()

    def registrar(self, email, contrasena, rol):
        return self.modelo.registrar_usuario(email, contrasena, rol)

    def iniciar_sesion(self, email, contrasena):
        rol = self.modelo.autenticar_usuario(email, contrasena)
        if rol:
            if rol == 'Administrador':
                self.mostrar_vista_admin()
            elif rol == 'Vendedor':
                self.mostrar_vista_vendedor()
            elif rol == 'Usuario':
                self.mostrar_vista_cliente()
            return rol
        else:
            return None

    def mostrar_vista_admin(self):
        # Aquí puedes agregar el código para abrir la ventana del Administrador
        self.vista.root.destroy()
        # vista_admin = VistaAdmin()
        # vista_admin.iniciar()

    def mostrar_vista_vendedor(self):
        # Aquí puedes agregar el código para abrir la ventana del Vendedor
        self.vista.root.destroy()
        # vista_vendedor = VistaVendedor()
        # vista_vendedor.iniciar()

    def mostrar_vista_cliente(self):
        # Aquí puedes agregar el código para abrir la ventana del Usuario
        self.vista.root.destroy()
        # vista_cliente = VistaCliente()
        # vista_cliente.iniciar()
