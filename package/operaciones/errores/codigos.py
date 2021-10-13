
import json
class codigos_respuesta:
    def __init__(self, code, status):
        self.code = code
        self.status = status

    def to_dict(self):
        dictionary = {
            "code":self.code,
            "status":self.status
        }
        return dictionary

codigo=codigos_respuesta(100,"Ok")

def error():
    print("Hubo un error")
def advertencia():
    print("Podemos resolver esto")
def exito():
    print("todo bien")


