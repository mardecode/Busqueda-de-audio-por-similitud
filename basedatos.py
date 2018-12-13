from hash import hash
import funciones
import pickle

#Cosas pendientes:
#    Persistir la data 
#    Archivo de configuracion, targets etc ... 

separacion_ancla = 10
n_targets = 20
tabla = None 

def nuevo():
    global tabla
    tabla = hash(50000)

def load():
    global tabla
    file = open("bd.pk","rb")
    tabla = pickle.load(file)
    file.close()

def save():
    global tabla
    file = open("bd.pk","wb")
    pickle.dump(tabla,file)
    file.close()

def insertar_cancion(picos, id_cancion):
    global tabla
    #tabla = open_dataset()
    #Creamos los pares e insertamos en la tabla de hash
    #(id_pico,frecuencia,tiempo)
    cont_inserts = 0
    for i in range(len(picos) - separacion_ancla-n_targets):
        ancla = picos[i]
        for j in range(n_targets):
            target = picos[i+separacion_ancla+j]
            
            f_ancla = ancla[0]
            f_point = target[0]
            delta_t = abs(target[1] - ancla[1])

            t_ancla = ancla[1]

            llave =funciones.concatenacionBin3(f_ancla,f_point,delta_t)
            dato = funciones.concatenacionBin2(t_ancla,id_cancion)
            cont_inserts+=1
            tabla.insertar(llave,dato)
    tabla.info()
    print ("Inserciones en tabla", cont_inserts)

def buscar_cancion(picos):
    #tabla = open_dataset()
    #Creamos los pares e insertamos en la tabla de hash
    #(id_pico,frecuencia,tiempo)
    global tabla
    pares = []
    for i in range(len(picos) - separacion_ancla-n_targets):
        ancla = picos[i]
        for j in range(n_targets):
            target = picos[i+separacion_ancla+j]
            
            f_ancla = ancla[0]
            f_point = target[0]
            delta_t = abs(target[1] - ancla[1])

            #t_ancla = ancla[1]

            llave =funciones.concatenacionBin3(f_ancla,f_point,delta_t)

            resp = tabla.buscar(llave)
            if resp:
                pares.append((llave,resp))
    
    return pares

