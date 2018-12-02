import os
#lista_archivos=[]
def devolverArchivos(carpeta,lista_archivos):

	for archivo in os.listdir(carpeta):

		filename=os.path.join(carpeta,archivo)

		if os.path.isdir(os.path.join(carpeta,archivo)):

			devolverArchivos(os.path.join(carpeta,archivo),lista_archivos)
		else:
			lista_archivos.append(filename)
			print("filename",filename)


