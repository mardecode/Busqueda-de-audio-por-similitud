import numpy as np

class hash(object):
     def __init__(self,size):
        self.size = size
        self.tabla = [None] * size

        
     def insertar(self, dato):
        ubicacion = dato%self.size
        while(self.tabla[ubicacion] != None):
            ubicacion += 1
            if ubicacion == self.size:
                ubicacion = 0
        self.tabla[ubicacion] = dato

     def printo(self):
         print (self.tabla)

     def buscar(self,dato):
         print (9)
         
'''
numeros = np.random.randint(36000, size=30)

tab = hash(30)

for i in range(30):
    tab.insertar(numeros[i])
tab.printo()
'''