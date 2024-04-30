class Agenda:
    def __int__(self, contactos=[]):
        self.contactos = contactos

    def getcontactos(self):
        return self.contactos
    def setcontactos(self,contactos):
        self.contactos = contactos
    def agregarcontacto (self, contacto):
        self.contactos.append(contacto)




