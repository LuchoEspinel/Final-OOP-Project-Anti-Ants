import csv
with open('login.csv','r') as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila)
