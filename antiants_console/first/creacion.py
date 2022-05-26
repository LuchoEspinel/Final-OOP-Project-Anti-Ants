import csv
class Creacion:
    def loginfileC():
        with open('login.csv', 'w') as loginfile:
            encabezados = ['Usuario','Contraseña','Registro']
            wrt = csv.DictWriter(loginfile, fieldnames= encabezados)
            wrt.writeheader()


