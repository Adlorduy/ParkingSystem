from datetime import datetime
import time

from functions import stringToDate, writeFile

class Parking():
  def __init__(self, size, money, path):
    self.path = path
    self.size = size
    self.cars = []
    self.workers = []
    self.money = money
    writeFile(f"{self.path}/workers.txt")
    writeFile(f"{self.path}/cars.txt")


  def add_car(self, plate):
    if not self.in_list(plate, self.cars):
        Carro = ClientCar(plate)
        self.cars.append(Carro)
        writeFile(f'{self.path}/cars.txt', f'{Carro.plate},{Carro.entrada}\n')
  
  def in_list(self, plate, lista):
    for car in lista:
      if car.plate == plate:
        return True
    return False
  
  def update_cars(self, file_name, sw):
    with open (self.path+'/'+file_name) as file:
      archivo = file.read().split("\n")
    if(archivo ==[""]):
      print("archivo vacio")
    else:
      for x in archivo:
        if(x == [""]):
          x = x.split(',')
          print(x)
          if sw == 0:
            Carro = ClientCar(x[0], stringToDate(x[1]))
            self.cars.append(Carro)
          else:
            Carro = WorkerCar(x[0])
            self.workers.append(Carro)
    

class Car():
  def __init__(self, plate):
    self.plate = plate
    self.pago = 0

class ClientCar(Car):
    def __init__(self, plate, entrada= None):
      super().__init__(plate)
      if (entrada == None):
        self.entrada = datetime.now()
      else:
        self.entrada = entrada
      self.salida = None
    
    def salir(self):
      self.salida = datetime.now()
      
      print(self.entrada)
      print(self.salida)
      diff = self.salida - self.entrada
      self.pago = 2000 * diff.total_seconds() / 3600

class WorkerCar(Car):
  def __init__(self, plate):
    super().__init__(plate)


class Worker():
  def __init__(self):
    pass