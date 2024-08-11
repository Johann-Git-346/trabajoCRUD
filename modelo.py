import hashlib

class ModeloUsuario:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, nombre_usuario, contrasena):
        if nombre_usuario in self.usuarios:
            return False
        #Esta opcion guardar la contraseña como un hash por seguridad
        self.usuarios[nombre_usuario] = self.hashear_contrasena(contrasena)
        return True

    def autenticar_usuario(self, nombre_usuario, contrasena):
        contrasena_hash = self.hashear_contrasena(contrasena)
        if nombre_usuario in self.usuarios and self.usuarios[nombre_usuario] == contrasena_hash:
            return True
        return False

    def hashear_contrasena(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()
