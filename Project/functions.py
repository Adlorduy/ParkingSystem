from datetime import datetime
from sre_parse import State
import PySimpleGUI as sg

def createFile(name):
    open(name, 'w')

def openFile(name):
    with open (name) as file:
      archivo = file.read().split("\n")
    return archivo

def writeFile(file, text = ""):
    archivo = open(file, 'a')
    archivo.write(str(text))
    archivo.close

def deleteLine(file, text):
    original = open(file, "r")
    lines = original.readlines()
    original.close
    createFile(file)
    for x in lines:
        aux = x.split(",")
        print(aux[0] + " " + text)
        if aux[0] != text:
            writeFile(file, x)

def editLine(file, text, i):
    original = open(file, "r")
    lines = original.readlines()
    original.close
    lines = lines[0].split(",")
    createFile(file)
    if i == 0:
        writeFile(file, f"{text},{lines[1]}")
    elif i == 1:
        writeFile(file, f"{lines[0]},{text}")


def login_layout():
    layout = [  [sg.Text('Inicio de sesión')],
            [sg.Text('', key='-MESS-')],
            [sg.Text('Usuario'), sg.InputText()],
            [sg.Text('Contraseña'), sg.InputText(password_char = '*'), ],
            [sg.Button('Iniciar sesión', key="-LOGIN-"), sg.Button('Crear cuenta', key="-CREATE-")] ]
    return layout

def park_layout():
    layout = [
                [sg.Text("Ocupados: "), sg.Text("", key="-NUMBERCARS-"), sg.Text("Tamaño: "), sg.Text("", key="-PARKINGSIZE-") ],
                [sg.Text("", key="-PLATEERROR-")],
                [sg.Text('Placa:'), sg.InputText(default_text="", key="-CHARS-"), sg.Text("-"), sg.InputText(default_text="", key="-NUMBERS-")],
                [sg.Button("Agregar carro", key="-ADDCAR-"), sg.Button("Eliminar carro", key="-DELCAR-") ],
                [sg.Button('Cerrar sesión', key="-LOGOUT-"), sg.Button("Configuraciones", key="-CONFIG-")]   
            ]
    return layout

def verify_layout():
    layout = [  [sg.Text('Verificación de admin')],
            [sg.Text('', key='-MESS-')],
            [sg.Text('Usuario'), sg.InputText(default_text="", key="-USER-", disabled = True)],
            [sg.Text('Contraseña'), sg.InputText(password_char = '*', key="-PASS-"), ],
            [sg.Button('Verificar', key="-VERIFY-"), sg.Button('Cancelar', key="-CANCEL-")] ]
    return layout

def config_layout():
    layout = [
                [sg.Text("", key="-SIZEERROR-")],
                [sg.Text("Tamaño actual: "), sg.Text("", key="-ACTUALSIZE-"), sg.InputText(default_text="", key = "-NEWSIZE-"), sg.Button("Actualizar tamaño", key="-CHANGESIZE-")],
                [sg.Text("", key="-PRICEERROR-")],
                [sg.Text("Precio actual: "), sg.Text("", key="-ACTUALPRICE-"), sg.InputText(default_text="", key = "-NEWPRICE-"), sg.Button("Actualizar precio", key="-CHANGEPRICE-")],
                [sg.Text("", key="-PLATEERROR-")],
                [sg.Text('Placa:'), sg.InputText(default_text="", key="-CHARS-"), sg.Text("-"), sg.InputText(default_text="", key="-NUMBERS-")],
                [sg.Button("Agregar carro trabajador", key="-ADDCARW-"), sg.Button("Eliminar carro trabajador", key="-DELCARW-")],
                [sg.Button('Salir', key="-EXIT-")]
            ]
    return layout

def stringToDate(date):
    return datetime.strptime(date,"%Y-%m-%d %H:%M:%S.%f")