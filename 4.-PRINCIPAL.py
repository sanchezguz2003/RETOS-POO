
from raton import *


Computadora1=Computadora("Electronico","COMP_1","hp","gris")
print("la DNI de la computadora es: ",Computadora1.DNI)
print("el nombre de la computadora es: ",Computadora1.NOMBRE)
print("la marca es: ",Computadora1.MARCA)
print("el color es:",Computadora1.COLOR)
Computadora1.ENCENDER()
Computadora1.APAGAR()
Computadora1.SUSPENDER()

MONITOR1=monitor("plasma","SFHOPHS03L")
print("El tipo de monitor es",MONITOR1.TIPO)
print("el modelo es",MONITOR1.MODELO)

RATON1=raton("USB","INLAMBRICA")
print("ei tipo de entrada del raton es:",RATON1.TIPO_ENTRADA)
print("la conexion es",RATON1.CONEXION)
RATON1.conectar()
RATON1.desconectar()


mi_archivo=open("COMPUTADORA.txt","w")
try:
    mi_archivo.write(f"esta es una computadora {Computadora1.NOMBRE}\n")
    mi_archivo.write(f"el modelo del monitor es {MONITOR1.MODELO}\n")
    mi_archivo.write(f"el tipo de raton es {RATON1.TIPO_ENTRADA}")

finally:
    mi_archivo.close()