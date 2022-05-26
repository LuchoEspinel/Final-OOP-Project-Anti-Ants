import csv

from login import Login
class CreaRUser(Login):
    def CRU():
        from login import IdRegistro
        with open(IdRegistro+'.csv','w') as csvfile:
            fieldnames = ['Tipo','Valor', 'Concepto']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()