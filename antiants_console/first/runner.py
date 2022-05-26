from creacion import Creacion
from creacionRegUser import CreaRUser
from login import Login
from registro import Registro

def main():
    print('(SOLO~ADMIN)Si desea crear un archivo de login, press 1 in another way press 0')
    R =input()
    if(R==1):
        createLogin = Creacion()
        createLogin.loginfileC()
    print('{Para Usuarios}')
    runLogin = Login()
    runLogin.logoin()
    createRUser = CreaRUser()
    createRUser.CRU()
    registar = Registro()
    registar.reg()
    
if __name__ == "__main__":
    main()