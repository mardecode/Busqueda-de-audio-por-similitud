import librosa
import librosa.display
import numpy as np 
import matplotlib.pyplot as plt
#import pandas as pd 
from scipy import stats


count_picos = 0
puntos = []

# Dato (db) ,Frecuencia, Tiempo
def f(x,f,t):
    global count_picos
    if x >= -4:
        count_picos+=1
        puntos.append( (count_picos,f,t) )
        return x
    else:
        return -100
    

def extraer_picos(audio,display=False):
    filename = audio
    y, sr = librosa.load(filename)
    D = np.abs(librosa.stft(y))
    Db = librosa.amplitude_to_db(D,ref=np.max)
    print(Db.shape)
    #Hasta aquí demora 8 segs 

    '''
    Usado para analizar Los Mayores puntos
    tD = D.reshape((1,-1)) #110 -> 300 aprox
    tDb = Db.reshape((1,-1)) #-5db -> 400 aprox
    # df = pd.Series(tDb[0])
    # df.plot.hist(bins=50)
    # plt.show()    
    '''

    #Ignoramos el ultimo dato, ya que se usa para crear la malla para specshow
    frecuencia = librosa.display.__mesh_coords('log', coords=None , n= Db.shape[0])[:-1] #Hz
    tiempo = librosa.display.__mesh_coords('time', coords=None , n= Db.shape[1])[ :-1] #seg

    filteredD = np.zeros(shape=Db.shape)
    filas , cols = Db.shape
    
    #Iteramos sobre el tiempo, luego sobre la frecuencia ( Este For demora  23-8 = 15 )
    for j in range(cols):
        for i in range(filas):
            #print(i,j)
            filteredD[i][j] = f(Db[i][j],int(frecuencia[i]),int(tiempo[j]))

    
    
    print("Cant. Picos: ", count_picos)
    #print(puntos)

    if display:
        show(filteredD)
    return puntos 

def show(D):
    librosa.display.specshow(D, y_axis='log', x_axis='time')
    plt.title('Power spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    plt.show()
