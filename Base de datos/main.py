import prueba2
import leer_carpeta 

#dirfile='/home/akire/Documentos/EDA/uno.mp3'
lista_archivos=[]
leer_carpeta.devolverArchivos("/home/akire/Documentos/EDA/Base de datos/bd",lista_archivos)

i=0
while i < len(lista_archivos):
	prueba2.split_and_addnoise(lista_archivos[i],i)
	#print("i",lista_archivos[i])
	i+=1

