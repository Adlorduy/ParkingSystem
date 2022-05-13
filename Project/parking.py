from datetime import datetime
import time

class Parking():
  def __init__(self, size, money):
    self.size = size
    self.cars = []
    self.workers = []
    self.money = money

  def add_car(self):
    placa = input("Ingrese placa: ")
    lavar = input("Ingrese si quiere lavar: ")
    if placa in self.workers:
      Carro = WorkerCar(placa, lavar)
    else:
      Carro = ClientCar(placa, lavar)
    self.cars.append(Carro)

  def update_workers_cars(self):
    self.workers = []
    with open ("Plates.txt") as file:
      archivo = file.read().split("\n")
    for x in range(len(archivo)):
      self.workers.append(archivo[x])

class Car():
  def __init__(self, plate, wash):
    self.plate = plate
    self.wash = wash
    self.pago = 0

class ClientCar(Car):
    def __init__(self, plate, wash):
      super().__init__(plate, wash)
      self.entrada = datetime.now()
      self.salida = None
    
    def salir(self):
      self.salida = datetime.now()
      
      print(self.entrada)
      print(self.salida)
      diff = self.salida - self.entrada
      self.pago = 2000 * diff.total_seconds() / 3600

class WorkerCar(Car):
  def __init__(self, plate, wash):
    super().__init__(plate, wash)


class Worker():
  def __init__(self):
    pass