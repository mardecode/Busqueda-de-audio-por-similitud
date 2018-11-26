from audio import extraer_picos
from hash import hash

audiofile = "audios/himno.mp3"

#Retorna una lista de tuplas con (id_pico,frecuencia,tiempo)
picos = extraer_picos(audiofile,False)
