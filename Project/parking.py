from datetime import datetime

from functions import editLine, stringToDate, writeFile, deleteLine

class Parking():
  def __init__(self, size, price, path, ):
    self.path = path
    self.size = size
    self.cars = []
    self.workers = []
    self.price = price
    writeFile(f"{self.path}/workers.txt")
    writeFile(f"{self.path}/cars.txt")


  def add_car(self, plate):
    if self.price != 0:
      if len(self.cars) < self.size:
        if not self.in_list(plate, self.cars):
            if self.in_list(plate, self.workers):
              Carro = WorkerCar(plate)
              writeFile(f'{self.path}/cars.txt', f'{Carro.plate}\n')
            else:
              Carro = ClientCar(plate)
              writeFile(f'{self.path}/cars.txt', f'{Carro.plate},{Carro.entrada}\n')
            self.cars.append(Carro)
            return 1
        return 0
      return -1
    else:
      return -2

  def add_worker(self, plate):
    if not self.in_list(plate, self.workers):
      Carro = WorkerCar(plate)
      writeFile(f'{self.path}/workers.txt', f'{Carro.plate}\n')
      self.workers.append(Carro)
      if self.in_list(plate, self.cars):
        Carro = self.plate_object(plate, self.cars)
        self.cars.remove(Carro)
        deleteLine(self.path+"/cars.txt", plate)
        self.add_car(plate)
      return True
    return False
  
  def in_list(self, plate, lista):
    for car in lista:
      if car.plate == plate:
        return True
    return False
  
  def update_cars(self, file_name, sw):
    with open (self.path+'/'+file_name) as file:
      archivo = file.read().split("\n")
    if(archivo !=[""]):
      for x in archivo:
        if x != "":
          x = x.split(',')
          if sw == 0:
            if len(x) == 1:
              Carro = WorkerCar(x[0])
            else:
              Carro = ClientCar(x[0], stringToDate(x[1]))
            self.cars.append(Carro)
          else:
            Carro = WorkerCar(x[0])
            self.workers.append(Carro)

  def del_car(self, plate):
    if self.in_list(plate, self.workers):
      deleteLine(self.path+"/cars.txt", plate+"\n")
      Carro = self.plate_object(plate, self.cars)
      self.cars.remove(Carro)
      return "NO tiene que pagar"
    elif self.in_list(plate, self.cars):
      Carro = self.plate_object(plate, self.cars)
      self.cars.remove(Carro)
      deleteLine(self.path+"/cars.txt", plate)
      return "Debe pagar "+ str(Carro.tiempo * self.price)
    else:
      return "Carro no registrado"

  def del_worker_car(self, plate):
    if self.in_list(plate, self.workers):
      deleteLine(self.path+"/workers.txt", plate+"\n")
      Carro = self.plate_object(plate, self.workers)
      self.workers.remove(Carro)
      if self.in_list(plate, self.cars):
        self.del_car(plate)
        self.add_car(plate)
      return True
    else:
      return False

  def plate_object(self, plate, lista):
    for car in lista:
      if car.plate == plate:
        return car
  
  def change_size(self, newSize):
    self.size = newSize
    editLine(self.path+"/data.txt", newSize, 0)

  def change_price(self, newPrice):
    self.price = newPrice
    editLine(self.path+"/data.txt", newPrice, 1)


class Car():
  def __init__(self, plate):
    self.plate = plate

class ClientCar(Car):
    def __init__(self, plate, entrada= None):
      super().__init__(plate)
      if (entrada == None):
        self.entrada = datetime.now()
      else:
        self.entrada = entrada
      self.salida = None
    
    @property
    def tiempo(self):
      self.salida = datetime.now()
      diff = self.salida - self.entrada
      return diff.total_seconds() / 3600

class WorkerCar(Car):
  def __init__(self, plate):
    super().__init__(plate)
