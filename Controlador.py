from Models.Contactos import Contacto
from Views.Vista import VistaAgenda

class ControladorAgenda:
    def __init__(self, archivocontactos):
        self.vista_agenda = VistaAgenda()
        self.contactoss = []
        try:
            with open(archivocontactos) as archivo_con_contactos:
                for line in archivo_con_contactos:
                    info_contacto = line.strip().split(',')
                    contactoo = Contacto((info_contacto[0]), info_contacto[1], (info_contacto[2]))
                    self.contactoss.append(contactoo)
        except FileNotFoundError:
            print('No hay servicios cargados')

        archivo_con_contactos.close()


    def ejecutar(self):
        while True:
            self.vista_agenda.mostrar_menu_principal()
            opcion_elegida = self.vista_agenda.validar_entero(1, 5)
            match opcion_elegida:
                case 1:
                    apellido_contacto = self.vista_agenda.soliape()
                    for self.contactoo in self.contactoss:
                        if apellido_contacto == self.contactoo.apellido:
                            self.vista_agenda.mostrarnumero(self.contactoo.getnumero())
                case 2:
                    for self.contactoo in self.contactoss:
                        self.vista_agenda.decoracion()
                        self.vista_agenda.mostrarnombre(self.contactoo.getnombre())
                        self.vista_agenda.mostrarapellido(self.contactoo.getapellido())
                        self.vista_agenda.mostrarnumero(self.contactoo.getnumero())
                case 3:
                    nombre=self.vista_agenda.solinombre()
                    apellido=self.vista_agenda.soliape()
                    numero=self.vista_agenda.solinum()
                    contactoo=Contacto(nombre,apellido,numero)
                    self.contactoss.append(contactoo)



                    try:
                        with open('archivos.txt',"w") as archivo_con_contactos:
                            for self.contactoo in self.contactoss:
                                archivo_con_contactos.write(f'{self.contactoo.string()}\n')
                            self.vista_agenda.exito()

                    except FileNotFoundError:
                        print('no existe ese archivo')
                case 4:
                    nombree=self.vista_agenda.borrar()
                    with open('archivos.txt', 'r') as archivo_con_contactos:
                        for self.contactoo in self.contactoss:
                            if nombree not in self.contactoo:
                                archivo_con_contactos.write(f'{self.contactoo.string()}\n')

                case 5:
                    break























