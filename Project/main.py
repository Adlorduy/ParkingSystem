import os
import PySimpleGUI as sg
import base64
from functions import createFile, login_layout, openFile, park_layout, verify_layout, config_layout, writeFile
from login import Password, User, Verifier
from parking import Parking

verifier = Verifier()
sg.theme("DarkAmber")
gen_sw = True
login_sw = True
park_sw = True
cofig_sw = False
verify_sw = False

while gen_sw:
    sc = sg.Window("Inicio sesión", login_layout())
    while login_sw:
        event, values = sc.read()
        if event == sg.WIN_CLOSED:
            login_sw= False
            park_sw= False
        else:
            user = User(values[0],values[1])
            if event == "-LOGIN-":
                if verifier.log_in(user):
                    sc['-MESS-'].update("Iniciando sesión...")
                    ruta = user.name
                    login_sw = False
                    park_sw= True
                else:
                    sc['-MESS-'].update("Usuario o contraseña incorrect@...")
            else:
                if verifier.is_free(user) and user.name != "" and user.password != "":
                    user.add()
                    sc['-MESS-'].update("Creando cuenta...")
                    ruta = user.name;
                    os.mkdir(f"{ruta}")
                    createFile(f"{ruta}/data.txt")
                    writeFile(f"{ruta}/data.txt", "0,0")
                    login_sw = False
                    park_sw= True
                else:
                    sc['-MESS-'].update("Usuario no disponible...")

    if park_sw and not (cofig_sw or verify_sw):
        sc.close()
        sc = sg.Window("Parqueadero", park_layout(), finalize= True)
        datos = openFile(user.name+"/data.txt")[0]
        datos = datos.split(",")
        Park = Parking(int(datos[0]), int(datos[1]), user.name)
        Park.update_cars("cars.txt", 0)
        Park.update_cars("workers.txt", 1)
        sc["-NUMBERCARS-"].update(str(len(Park.cars)))
        sc["-PARKINGSIZE-"].update(str(Park.size))

    while park_sw:
        event, values = sc.read()
        chars = values["-CHARS-"]
        nums = values["-NUMBERS-"]
        if event == '-LOGOUT-':
            park_sw = False
            login_sw = True
        elif event == "-ADDCAR-":
            if chars.isalpha() and len(chars) == 3 and nums.isnumeric() and len(nums) == 3:  
                sw = Park.add_car(f'{chars}{nums}')
                if sw == 0:
                    sc["-PLATEERROR-"].update("Placa ya ingresada")
                elif sw == 1:
                    sc["-NUMBERCARS-"].update(str(len(Park.cars)))
                    sc["-PLATEERROR-"].update("")
                    sc["-CHARS-"].update("")
                    sc["-NUMBERS-"].update("")
                elif sw == -1:
                    if Park.size == 0:
                        sc["-PLATEERROR-"].update("Su tamaño actual es 0, por favor configúrelo")
                    else:
                        sc["-PLATEERROR-"].update("No hay puestos disponibles")
                elif sw == -2:
                    sc["-PLATEERROR-"].update("Su precio actual es 0, por favor configúrelo")
            else:
                sc["-PLATEERROR-"].update("Placa invalida")
        elif event == "-DELCAR-":
            sc["-PLATEERROR-"].update(Park.del_car(chars+nums))
            if sc["-PLATEERROR-"] != "Carro no registrado": 
                sc["-NUMBERCARS-"].update(str(len(Park.cars)))
                sc["-CHARS-"].update("")
                sc["-NUMBERS-"].update("")
        elif event == "-CONFIG-":
            park_sw = False
            verify_sw = True
        elif event == sg.WIN_CLOSED:
            park_sw = False

    if verify_sw:
        sc.close()
        sc = sg.Window("Verificador", verify_layout(), finalize= True)
        sc["-USER-"].update(user.name)

    while verify_sw:
        event, values = sc.read()
        if event == sg.WIN_CLOSED:
            park_sw = False
            verify_sw = False
        elif event == "-VERIFY-":
            user = User(values["-USER-"], values["-PASS-"])
            if verifier.log_in(user):
                    sc['-MESS-'].update("Iniciando sesión...")
                    config_sw = True
                    verify_sw = False
            else:
                sc['-MESS-'].update("Usuario o contraseña incorrect@...")
        elif event == "-CANCEL-":
            park_sw = True
            verify_sw = False

    if config_sw:
        sc.close()
        sc = sg.Window("Config", config_layout(), finalize= True)
        sc["-ACTUALSIZE-"].update(str(Park.size))
        sc["-ACTUALPRICE-"].update(str(Park.price))
    
    while config_sw:
        event, values = sc.read()
        chars = values["-CHARS-"]
        nums = values["-NUMBERS-"]
        if event == sg.WIN_CLOSED:
            config_sw = False
            park_sw = False
        elif event == "-CHANGESIZE-":
            if values["-NEWSIZE-"].isnumeric():
                if int(values["-NEWSIZE-"]) < len(Park.cars) or int(values["-NEWSIZE-"]) == 0 :
                    sc["-SIZEERROR-"].update("ERROR: El nuevo tamaño es menor a la cantidad de carros actual o 0")
                else:
                    Park.change_size(int(values["-NEWSIZE-"]))
                    sc["-ACTUALSIZE-"].update(str(Park.size))
                    sc["-NEWSIZE-"].update("")
                    sc["-SIZEERROR-"].update("")

        elif event == "-CHANGEPRICE-":
            if values["-NEWPRICE-"].isnumeric():
                if int(values["-NEWPRICE-"]) <= 0:
                    sc["-PRICEERROR-"].update("ERROR: El nuevo precio es ilógico")
                else:
                    Park.change_price(int(values["-NEWPRICE-"]))
                    sc["-ACTUALPRICE-"].update(str(Park.price))
                    sc["-NEWPRICE-"].update("")
                    sc["-PRICEERROR-"].update("")
        elif event == "-ADDCARW-":
            if chars.isalpha() and len(chars) == 3 and nums.isnumeric() and len(nums) == 3:  
                if not Park.add_worker(f'{chars}{nums}'):
                    sc["-PLATEERROR-"].update("Trabajador ya registrado")
                else:
                    sc["-PLATEERROR-"].update("Trabajador agregado")
                    sc["-CHARS-"].update("")
                    sc["-NUMBERS-"].update("")
            else:
                sc["-PLATEERROR-"].update("Placa invalida")

        elif event == "-DELCARW-":
            if chars.isalpha() and len(chars) == 3 and nums.isnumeric() and len(nums) == 3:
                if Park.del_worker_car(chars+nums):
                    sc["-PLATEERROR-"].update("Trabajador eliminado")
                    sc["-CHARS-"].update("")
                    sc["-NUMBERS-"].update("")
                else:
                    sc["-PLATEERROR-"].update("Trabajador no registrado")

        elif event == "-EXIT-":
            config_sw = False
            park_sw = True

    gen_sw = login_sw or park_sw
    sc.close()
