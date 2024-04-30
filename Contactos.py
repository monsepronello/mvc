class Contacto:
    def __init__(self, nombre, apellido, numero):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero

    def string(self):
        return f"{self.nombre},{self.apellido},{self.numero}"

    def getnombre(self):
        return self.nombre


    def getnumero(self):
        return self.numero

    def setnombre(self, nombre):
        self.nombre = nombre

    def getapellido(self):
        return self.apellido

    def setapellido(self, apellido):
        self.apellido = apellido

    def setnumero(self, numero):
        self.numero = numero

    def __str__(self):
        return f'Nombre: {self.nombre}\nApellido: {self.apellido}\n numero: {self.numero}'


