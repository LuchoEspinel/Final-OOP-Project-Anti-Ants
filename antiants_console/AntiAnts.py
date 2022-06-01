log = 'login'
import csv
import pandas as pd
import matplotlib.pyplot as plt


class usuario():
    def __init__(self, name, psw):
        self.name = name
        self.psw = psw
        
    def registrar (self):
        print("¿Cuanto gastaste?")
        self.valor = int(input())
        print("¿Qué categoría?")
        self.categoria = categoria()
        with open(self.name +'.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.categoria, self.valor])

    def graficas (self):
        datos = pd.read_csv(self.name + '.csv', header = 0)
        df = pd.DataFrame(datos)
        df.groupby('Categoria')['Valor'].sum().plot(kind = 'bar')
        plt.show()
        
    def mostrar (self):
        with open(self.name + '.csv','r') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:  
                print(row)  

    def crear_cuenta(self):
        lista = [self.name, self.psw]
        with open(self.name +'.csv','w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Categoria','Valor'])

        with open(log+'.csv', 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(lista)

    def login(self):
        with open('login.csv','r') as readfile:
            reader = csv.DictReader(readfile)
            sw=False
            for row in reader:  
                if row['Usuario'] == self.name and row['Password'] == self.psw:
                    sw = True
            if sw==True:
                print("")
                print("Ingresando...####################")
            else:
                print("----------------------------------------------------")
                print("Contraseña o Usuario incorrectos. Ingresar de nuevo.")
                print("----------------------------------------------------")
                app()
        
def categoria ():
    print("CATEGORÍAS:")
    print("------------")
    print("1. comida.\n2. bebidas.\n3. otros")
    ans = input("*")
    if ans == '1':
        return "comida"
    elif ans == '2':
        return "bebida"
    elif ans == '3':
        return "otros"
    else:
        print("-----------------------------------------")
        print("categoría no válida, ingresar nuevamente")
        print("-----------------------------------------")
        return categoria()

def loginfile():
    lista = ['Usuario','Password']
    with open('login.csv','w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(lista)

def bienvenida():
    print("--------------------------")
    print(" *** ¡¡¡BIENVENID@!!! ***    ")
    print("------------------------- ")
    print("Anti-Ants te ayuda a tener un mejor manejo de tus ,")
    print("finzanzas personales. Más exactamente con esos ")
    print("pequeños gastos, a los cuales no les damos la suficiente")
    print("importancia, denominados 'Gastos Hormiga'")
    print("-------------------------")

def login_pg():
    print("")
    print("Hola! ¿Qué desea?")
    print("1) Crear cuenta.\n2) Iniciar sesión.\n3) Salir.")
    ans = input("*")
    return ans

def tiene_cuenta(res):
    if res == '1':
        print("Username:")
        name = input("*")
        print("Password:")
        psw = input("*")
        user = usuario(name, psw)
        user.crear_cuenta()
        app()
    elif res == '2':
        print("Username:")
        name = input("*")
        print("Password:")
        psw = input("*")
        user = usuario(name, psw)
        user.login()
        print("-----------------------")
        print("--------INICIO---------")
        print("-----------------------")
        print("")
        print("*** ¿Qué desea? ***")
        print("1) registrar.\n2) Ver gráficas.\n3) Ver datos.\n4) Cerrar sesión.")
        ans = input("*")
        while ans != 4:
            if ans == '1':
                user.registrar()

            elif ans == '2':
                user.graficas()

            elif ans == '3':
                user.mostrar()

            elif ans == '4':
                app()
            else:
                print("--------------------------------------")
                print("Opción no válida. Intente de nuevo.")
                print("--------------------------------------")
                print("")

            print("-----------------------")
            print("--------INICIO---------")
            print("-----------------------")
            print("")
            print("*** ¿Qué desea? ***")
            print("1) registrar.\n2) Ver gráficas.\n3) Ver datos.\n4) Cerrar sesión.")
            ans = input("*")

    elif res == '3':
        print("-------------------------")
        print("¡¡¡GRACIAS POR PREFERIRNOS!!!" )
        print("-------------------------")
        exit(0)
        
    else:
        print("")
        print("--------------------------------------")
        print("Opción no válida. Ingresar de nuevo.")
        print("--------------------------------------")
        ans = login_pg()
        tiene_cuenta(ans)

def app():
    bienvenida()
    ans = login_pg()
    tiene_cuenta(ans)

if __name__=='__main__':
    app()        