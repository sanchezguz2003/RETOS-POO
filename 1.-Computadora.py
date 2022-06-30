class Computadora:
    def __init__(self, DNI, NOMBRE, MARCA, COLOR):
        self.DNI = DNI
        self.NOMBRE = NOMBRE
        self.MARCA = MARCA
        self.COLOR = COLOR

    def ENCENDER(self):
            print("TU COMPUTADORA ",self.NOMBRE,"ESTA ENCENDIDA")

    def APAGAR(self):
            print("TU COMPUTADORA ",self.NOMBRE,"ESTA APAGA")

    def SUSPENDER(self):
            print(self.NOMBRE,"ESTA SUSPENDIDA")
