from hash import hash
import funciones 

#Cosas pendientes:
#    Persistir la data 
#    Archivo de configuracion, targets etc ... 

separacion_ancla = 10
n_targets = 20
#tabla = hash(1000)

def open_dataset(filename="bd"):
    return hash(1000)

def insertar_cancion(picos, id_cancion):
    tabla = open_dataset()
    #Creamos los pares e insertamos en la tabla de hash
    #(id_pico,frecuencia,tiempo)
    for i in range(len(picos) - separacion_ancla-n_targets):
        ancla = picos[i]
        print(i)
        for j in range(n_targets):
            target = picos[i+separacion_ancla+j]
            
            f_ancla = ancla[1]
            f_point = target[1]
            delta_t = abs(target[2] - ancla[2])

            t_ancla = ancla[2]

            llave =funciones.concatenacionBin3(f_ancla,f_point,delta_t)
            dato = funciones.concatenacionBin2(t_ancla,id_cancion)

            tabla.insertar(llave,dato)

