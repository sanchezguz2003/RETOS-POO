from MONITOR import *

class raton(monitor):
    def __init__(self,TIPO_ENTRADA,CONEXION):
        self.TIPO_ENTRADA=TIPO_ENTRADA
        self.CONEXION=CONEXION
    def conectar(self):
        print("tu tipo de entrada",self.TIPO_ENTRADA,"esta conectada")
    def desconectar(self):
        print("tu conexion esta",self.CONEXION,"esta desconectado")
