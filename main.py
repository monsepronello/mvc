from Controllers.Controlador import ControladorAgenda

archivocontactos = 'archivos.txt'

controlador_main = ControladorAgenda(archivocontactos)

controlador_main.ejecutar()