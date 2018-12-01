import numpy as np

class hash(object):
     def __init__(self,size):
        self.size = size
        self.tabla = [None] * size
        self.colison = 0

        
     def insertar(self, llave,dato):
        ubicacion = llave%self.size
        # hubo = False
        if(self.tabla[ubicacion] == None):
            self.tabla[ubicacion] = []
        self.tabla[ubicacion].append(dato)

        # while(self.tabla[ubicacion] != None):
        #     hubo = True
        #     ubicacion += 1
        #     if ubicacion == self.size:
        #         ubicacion = 0
        # self.tabla[ubicacion] = dato
        # if(hubo): self.colison += 1


     def printo(self):
         print (self.tabla)

     def buscar(self,llave):
        ubicacion = llave%self.size
        if(self.tabla[ubicacion]!= None): return self.tabla[ubicacion]
        else: return None
         

tamano = 10
# numeros = np.random.randint(4294967295, size=tamano)

tab = hash(tamano)

# for i in range(tamano):
#     tab.insertar(numeros[i],89)
# print(tab.colison)
tab.insertar(1,34)
tab.insertar(1,44)
tab.insertar(1,22)
tab.insertar(1,11)
tab.printo()

print tab.buscar(1)




