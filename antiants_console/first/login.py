import csv

from creacion import Creacion
class Login(Creacion):
    def logoin():
        print('tiene usted una cuenta?\nY para si\nN para no')
        resp = input()
        ok=False

        while(resp!='Y'and resp!='N'):
            print('error de formato, intente de nuevo.')
            resp=input()  
        if(resp=='Y'): #aun le falta desarrollo a esto, esta mas avanzada la creacion de cuenta
            with open('login.csv','r') as csvfile:
                reader = csv.DictReader(csvfile)
                print('ingrese su usuario')
                user = input()
                print('ingrese su contraseña')
                passw = input()
                for row in reader:
                    if(row['Usuario']==user and row['Contraseña']==passw):
                        IdRegistro = row['Registro']
                        print(row['Registro'])
                        ok=True
                    else:
                        #print('los datos ingresados no se encuentran en nuestra base de datos')
                        ok=False
                csvfile.close()
                while(ok==False):
                    print('La cuenta a la que desea acceder no existe, intente nuevamente')
                    with open('login.csv','r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        print('ingrese su usuario o si desea cerrar escriba "Quit"')
                        user = input()
                        if(user=='Quit'):
                            quit()
                        print('ingrese su contraseña')
                        passw = input()
                        for row in reader:
                            if(row['Usuario']==user and row['Contraseña']==passw):
                                IdRegistro = row['Registro']
                                print(row['Registro'])
                                ok=True
                            else:
                                #print('los datos ingresados no se encuentran en nuestra base de datos')
                                ok=False
        else:
            print('CREACION DE CUENTA:\nIngrese el usuario que quiera crear')
            newUser = input()
            print('Ingrese su contraseña')
            newPass= input()
            print('Ingrese nuevamente su contraseña')
            samePass =input()
            sw=1
            while(sw==1):
                if(newPass==samePass):
                    with open('login.csv','a', newline='') as csvfile: #obviamente para que esto funcione debes ejecutar primero el creacion.py que es donde se crea el archivo de los login
                        writer= csv.DictWriter(csvfile, fieldnames=['Usuario','Contraseña','Registro'])
                        writer.writerow({'Usuario': newUser,'Contraseña': newPass,'Registro':newUser+'.csv'})
                        csvfile.close()
                    print('Usted ha creado exitosasmente su cuenta')
                    sw=0
                else:
                    print('Las contraseñas no coinciden, intentar de nuevo: ')
                    print('Ingrese su contraseña')
                    newPass= input()
                    print('Ingrese nuevamente su contraseña')
                    samePass =input()
                    sw=1