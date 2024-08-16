from ControladorInicio import Controlador
from BaseInicio import Crear_Conexion

#PRINCIPAL
conexion = Crear_Conexion.conexionBaseDeDatos()
controlador = Controlador(conexion)
controlador.iniciar()
