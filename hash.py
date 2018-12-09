class hash(object):
     def __init__(self,size):
        self.size = size
        self.tabla = [None] * size
        self.colisiones = 0
        self.ocupados = 0
        self.datos = 0

        
     def insertar(self, llave,dato):
        self.datos  += 1
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
            self.ocupados += 1 

        if(hubo): 
            # print("dato colisionado ",dato)
            self.colisiones += 1


     def printo(self):
         print (self.tabla)

     def buscar(self,llave):
        ubicacion = llave%self.size

        while(self.tabla[ubicacion]!= None): 
            if(self.tabla[ubicacion][0] == llave):
                return self.tabla[ubicacion][1]
            ubicacion += 1
            if ubicacion == self.size:
                ubicacion = 0
            if ubicacion == llave%self.size -1:
                return None
        
        if(self.tabla[ubicacion] == None):
            return None

     def info(self):
        print ("colisiones ", self.colisiones)
        print ("ocupados ",self.ocupados)
        print ("datos ", self.datos)
         

#dato no poner numero par para el tamanio genera muchas colisiones de preferencia numero primo o impar 
# EJEMPLO probable si cambias el tamanio por 10 inclusio 20 muchas colisiones

# tamano = 15

# tab = hash(tamano)

# tab.insertar(1,34)
# tab.insertar(1,22)
# tab.insertar(11,11)
# tab.insertar(2,34)
# tab.insertar(2,19)
# tab.insertar(21,44)
# tab.insertar(22,89)
# tab.insertar(4,11)
# tab.insertar(44,34)
# tab.insertar(5,15)
# tab.insertar(6,89)
# tab.insertar(8,21)
# tab.insertar(8,31)

# tab.printo()

# print ( tab.buscar(22) )
# print ("datos ",tab.datos)
# print ("colisiones ", tab.colisiones)
# print ("ocupados", tab.ocupados)




