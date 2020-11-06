class Usuario:
    def __init__(self, nombre, apellido, userName, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.userName = userName
        self.contrasena = contrasena

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido = apellido

    def getUserName(self):
        return self.userName

    def setUserName(self, userName):
        self.userName = userName

    def getContrasena(self):
        return self.contrasena

    def setContrasena(self, contrasena):
        self.contrasena = contrasena






