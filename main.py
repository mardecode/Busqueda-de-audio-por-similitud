from audio import extraer_picos
import basedatos
import time 
inicio_def = time.time()

id_cancion = 23898
audiofile = "audios/himno.mp3"

#Retorna una lista de tuplas con (id_pico,frecuencia,tiempo)
picos = extraer_picos(audiofile)
print("Picos Extraidos")
basedatos.insertar_cancion(picos,id_cancion)

fin_def = time.time()

print("Tiempo Todo", fin_def-inicio_def)

