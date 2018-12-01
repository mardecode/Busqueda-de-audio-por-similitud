class hash(object):
     def __init__(self,size):
        self.size = size
        self.tabla = [None] * size
        self.colison = 0

        
     def insertar(self, llave,dato):
        ubicacion = llave%self.size
        hubo = False
        masVuelta = 0
         
        while(self.tabla[ubicacion] != None):
            if(masVuelta ==2): print("El tamanio de la data es mas grande que la tabla \n Presiona Crtl + c")
            if(self.tabla[ubicacion][0] == llave):
                self.tabla[ubicacion][1].append(dato)
                break
            hubo = True
            ubicacion += 1
            if ubicacion == self.size:
                masVuelta +=1
                ubicacion = 0

        if(self.tabla[ubicacion] == None):
            self.tabla[ubicacion] = (llave,[])    
            self.tabla[ubicacion][1].append(dato)

        if(hubo): self.colison += 1


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
tab.insertar(1,22)
tab.insertar(11,11)
tab.insertar(2,34)
tab.insertar(2,19)
tab.insertar(21,44)
tab.insertar(22,89)
tab.insertar(4,11)
tab.insertar(44,34)
tab.insertar(5,15)
tab.insertar(6,89)
tab.insertar(8,21)
tab.insertar(8,31)

tab.printo()

# print tab.buscar(1)




