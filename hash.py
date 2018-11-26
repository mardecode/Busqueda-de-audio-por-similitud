import numpy as np

class hash(object):
     def __init__(self,size):
        self.size = size
        self.tabla = [None] * size
        self.colison = 0

        
     def insertar(self, llave,dato):
        ubicacion = llave%self.size
        hubo = False
        while(self.tabla[ubicacion] != None):
            hubo = True
            ubicacion += 1
            #print("loc",ubicacion) ###
            if ubicacion == self.size:
                ubicacion = 0
        self.tabla[ubicacion] = dato
        if(hubo): self.colison += 1


     def printo(self):
         print (self.tabla)

     def buscar(self,dato):
         print (9)
         
'''
tamano = 1000
numeros = np.random.randint(4294967295, size=tamano)

tab = hash(tamano)

for i in range(tamano):
    tab.insertar(numeros[i],89)
# tab.printo()
print(tab.colison)
'''