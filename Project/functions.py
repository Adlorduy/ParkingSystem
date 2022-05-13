import PySimpleGUI as sg

def createFile(name):
    open(name, 'w')

def openFile(name):
    with open (name) as file:
      archivo = file.read().split("\n")
    return archivo

def login_layout():
    layout = [  [sg.Text('Inicio de sesión')],
            [sg.Text('', key='-MESS-')],
            [sg.Text('Usuario'), sg.InputText()],
            [sg.Text('Contraseña'), sg.InputText(password_char = '*'), ],
            [sg.Button('Iniciar sesión', key="-LOGIN-"), sg.Button('Crear cuenta', key="-CREATE-")] ]
    return layout

def park_layout():
    layout = [[sg.Text('Placa:'), sg.InputText(), sg.Text("-"), sg.InputText()],
                [sg.Button("Agregar carro", key="-ADDCAR-")],
             [sg.Button('Cerrar sesión', key="-LOGOUT-")]   
                ]
    return layout