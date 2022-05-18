import base64
from functions import createFile, openFile, writeFile

class Password():    
    def __init__(self) -> None:
        self.filename = "passwords.txt"

class Verifier(Password):
    def __init__(self) -> None:
        super().__init__()

    @property
    def file(self):
        return openFile(self.filename)

    def log_in(self, user):
        try:
            for x in self.file:
                username, passw = x.split(",")
                if((username == user.name) & (passw == str(user.password))):
                    return True
            return False
        except:
            return False


    def is_free(self, user):
        try:
            for x in self.file:
                username= x.split(",")[0]
                if(username == user.name):
                    return False
            return True
        except:
            createFile("passwords.txt")
            return True

class User(Password):
  def __init__(self, name, password):
    self.name = name
    self.password = password.encode("UTF-8")
    self.password = base64.b64encode(self.password)
    super().__init__()

  def add(self):
      writeFile(self.filename,f'{self.name},{self.password}\n' )