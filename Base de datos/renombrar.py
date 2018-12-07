import os
def devolverArchivos(carpeta,i):
     	j=0
	for archivo in os.listdir(carpeta):
	     if os.path.isdir(os.path.join(carpeta,archivo)):
		devolverArchivos(os.path.join(carpeta,archivo),i)
		os.rename(carpeta+"/"+archivo,carpeta+"/"+str(i))
#		print("imprimiendo /n")
#		print(os.listdir(carpeta+"/"+archivo ))
		i+=1
	     else:

	     	if archivo[-4:]==".m4a":					
			os.rename(carpeta+"/"+archivo,carpeta+"/"+str(i)+"."+str(j)+".m4a")
	        if archivo[-4:]==".mp3":	
			os.rename(carpeta+"/"+archivo,carpeta+"/"+str(i)+"."+str(j)+".mp3")
	     j+=1

devolverArchivos("/home/akire/Documentos/EDA/proyecto/Base de datos/bd",1)
