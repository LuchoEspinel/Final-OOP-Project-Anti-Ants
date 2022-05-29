import csv

class usuario():
    def __init__(self, name, psw):
        self.name = name
        self.psw = psw
        
    def registrar (self, valor, categoria):
        self.valor = valor
        self.categgoria = categoria
        with open(self.name+'.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([valor, categoria])

def crear_cuenta(user, psw):
    lista = [user, psw]
    with open(user+'.csv','w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['entrada', 'salida','Valor', 'Categoria'])
    with open('login.csv', 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(lista)
    user = usuario(user, psw)
    
def login(usr, psw):
    file = open("login.csv","r+")
    readfile = file.readlines()

    for string in readfile:
        fila = string.split(",")
        usuario = fila[0]
        password = fila[1]
        if(usuario == usr and password == psw):
            print("Ingresando...")

def categoria ():
    print("CATEGORÍAS:")
    print("1. comida. \n 2. gaseosa/bebidas 3. otros")


    





