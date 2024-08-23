from ControladorInicio import Controlador
from BaseInicio import Crear_Conexion

# PRINCIPAL
conexion = Crear_Conexion.conexionBaseDeDatos()
if conexion:
    controlador = Controlador(conexion)
    controlador.iniciar()
else:
    print("No se pudo establecer conexión con la base de datos.")
