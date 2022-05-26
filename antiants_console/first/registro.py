import csv
from creacionRegUser import CreaRUser 
class Registro(CreaRUser):
    def reg():    
        msgRegistro = ('Ingrese tipo de registro:\n'
        'E para designar con cuanto sale de casa \n'
        'D para designar un registro durante el dia\n'
        'S para designar con cuanto llega a casa')

        print('---------------\nHola')
        def ask():
            print('Desea hacer un registro?\n Y para si\n N para no')
            respuesta = input()
            return respuesta

        def askType(msgRegistro):
            print(msgRegistro)
            tipoR = input()
            return tipoR

        def validar_Num(valor):
            try:
                int(valor)
                valid = True
            except ValueError:
                valid = False
            return valid

        answ = ask()
        while(answ!='Y' and answ!='N'):
            print('--o--')
            print('Intente de nuevo')
            answ = ask()

        while(answ=='Y'):
            tipoR = askType(msgRegistro)
            while(tipoR!='E' and tipoR!='D'and tipoR!='S'):
                print('Error de formato, intente de nuevo.')
                tipoR = askType(msgRegistro)
                
            print('Indice el valor del registro que desea hacer: ')
            valorR = input()
            valido= validar_Num(valorR)
            while(valido == False):
                print('NUEVAMENTE|||El valor debe estar en numeros')
                valorR = input()
                valido= validar_Num(valorR)

            print('Agregue una breve descripcion de que uso le dio a este gasto: ')
            concept = input()
            valido = validar_Num(concept)
            while(valido == True):
                print('NUEVAMENTE|||La descripcion deben ser letras')
                concept = input()
                valido = validar_Num(concept)

            if(tipoR=='E'):
                type ='Entrada'
            elif(tipoR=='D'):
                type ='Diario'
            elif(tipoR=='S'):
                type='Salida'
            with open(CreaRUser.IdRegistro+'.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['Tipo','Valor', 'Concepto'])
                writer.writerow({'Tipo': type,
                'Valor': valorR,
                'Concepto': concept})
                csvfile.close()
            print('°°NUEVAMENTE°°')
            answ = ask()
        