from importlib.resources import path
import os
import PySimpleGUI as sg
from functions import createFile, login_layout, park_layout
from login import User, Verifier

verifier = Verifier()
sg.theme("DarkAmber")
gen_sw = True
login_sw = True
park_sw = True

while gen_sw:
    sc = sg.Window("Inicio sesión", login_layout())
    while login_sw:
        event, values = sc.read()
        if event == sg.WIN_CLOSED:
            login_sw= False
            park_sw= False
        else:
            user = User(values[0], values[1])
            if event == "-LOGIN-":
                if verifier.log_in(user):
                    sc['-MESS-'].update("Iniciando sesión...")
                    ruta = user.name;
                    login_sw = False
                    park_sw= True
                else:
                    sc['-MESS-'].update("Usuario o contraseña incorrect@...")
            else:
                if verifier.is_free(user):
                    user.add()
                    sc['-MESS-'].update("Creando cuenta...")
                    ruta = user.name;
                    os.mkdir(f"{ruta}")
                    createFile(f"{ruta}/plates.txt")
                    login_sw = False
                    park_sw= True
                else:
                    sc['-MESS-'].update("Usuario no disponible...")
    sc.close()
    sc = sg.Window("Parqueadero", park_layout())
    
    while park_sw:
        event, values = sc.read()
        if event == '-LOGOUT-':
            park_sw = False
            login_sw = True
        elif event == "-ADDCAR-":
            pass
        else:
            park_sw = False

    gen_sw = login_sw or park_sw
    sc.close()

