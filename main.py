from audio import extraer_picos
import basedatos

id_cancion = 23898
audiofile = "audios/himno.mp3"

#Retorna una lista de tuplas con (id_pico,frecuencia,tiempo)
picos = extraer_picos(audiofile,False)
print("Picos Extraidos")
basedatos.insertar_cancion(picos,id_cancion)

