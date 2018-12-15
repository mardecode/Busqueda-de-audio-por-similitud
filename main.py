from audio import extraer_picos
import basedatos
import time 
from hash import hash
from funciones import desconcatenacion
'''
basedatos.nuevo()

#Retorna una lista de tuplas con (frecuencia,tiempo)
picos = extraer_picos("final/0.mp3",False)
basedatos.insertar_cancion(picos,65531)
#basedatos.tabla.info()

#Retorna una lista de tuplas con (frecuencia,tiempo)
picos = extraer_picos("final/1.mp3",False)
print("Picos Extraidos")
basedatos.insertar_cancion(picos,65532)

picos = extraer_picos("final/2.mp3",False)
basedatos.insertar_cancion(picos,65533)
#basedatos.tabla.info()

#Retorna una lista de tuplas con (frecuencia,tiempo)
picos = extraer_picos("final/3.mp3",False)
print("Picos Extraidos")
basedatos.insertar_cancion(picos,65534)

picos = extraer_picos("final/4.mp3",False)
print("Picos Extraidos")
basedatos.insertar_cancion(picos,65535)

picos = extraer_picos("final/5.mp3",False)
print("Picos Extraidos")
basedatos.insertar_cancion(picos,65530)

basedatos.tabla.info()

basedatos.save()
'''
basedatos.load()
#'''

def buscar(name):
        audiotest = name 
        picos2 = extraer_picos(audiotest,False)
        pares = basedatos.buscar_cancion(picos2)

        #[ <k,[<id,tA>]>  ]
        print ("Coincidencias " ,len(pares))

        tabla2 = hash(10000)
        for par in pares:
                #print (par)
                for taid in par[1]:
                        #insertar ( llave par[0],llave)
                        tabla2.insertar2(taid,par[0])
                        #print(ta,par[0])

        #tabla2.info()
        umbral = 0
        tabla3 = hash(10000)
        for dato in tabla2.tabla:
                if dato != None:
                        #print(dato[1])
                        if dato[1] >= umbral :
                                #print(dato[0])
                                ta,id = desconcatenacion(dato[0])
                                tabla3.insertar2(id,[ta,dato[2]])

        #umbral2 = 100 * 0.9
        for dato in tabla3.tabla:
                if dato != None:
                        print(dato[0],dato[1])
                #if dato[1] >= umbral :
                #    print(dato[0])



buscar("final/salida_filtro/0_1_3.mp3")
buscar("final/salida_filtro/1_3_4.mp3")