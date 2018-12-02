#!/usr/bin/env python

#para descubrimiento copias de musica,melodias copiadas 
#colegiada de walter leon(melodia) fue copeado por el grupo mana en  "mariposa traicionada ".
from progressbar import ProgressBar
import argparse
import matplotlib.pyplot as plt
import librosa
import numpy as np
import os


def alterando_frecuencia_onda(y,sr):
	y_pitch=y
	bins_per_octave = 24#24
	pitch_pm = 0.3 #pasos
	pitch_change =  pitch_pm * 2*(np.random.uniform()-0.5)   
	print("pitch_change = ",pitch_change)
	y_pitch = librosa.effects.pitch_shift(y_pitch.astype('float64'), 
		                              sr, n_steps=pitch_change, 
		                              bins_per_octave=bins_per_octave)
	return y_pitch
def aumentando_velocidad(y):
	y_pitch_speed=y
	# you can change low and high here
	length_change = np.random.uniform(low=0.5,high=1.5)
	speed_fac = 1.0  / length_change
	print("resample length_change = ",length_change)
	tmp = np.interp(np.arange(0,len(y_pitch_speed),speed_fac),np.arange(0,len(y_pitch_speed)),y_pitch_speed)
	minlen = min(y_pitch_speed.shape[0], tmp.shape[0])
	y_pitch_speed *= 0
	y_pitch_speed[0:minlen] = tmp[0:minlen]
	return y_pitch_speed

def add_noise(y):
	y_noise = y
	noise_amp = 0.0335*np.random.uniform()*np.amax(y_noise)
	y_noise = y_noise.astype('float64') + noise_amp * np.random.normal(size=y_noise.shape[0])
	
	return y
def split_and_addnoise(dirfile,numero): 
	#preparitovos para guardar las divisiones de canciones
	parser = argparse.ArgumentParser(
		description='Split audio into multiple files and save analysis.')
	parser.add_argument('-i', '--input', type=str)
	parser.add_argument('-o', '--output', type=str, default='salida')
	parser.add_argument('-s', '--sr', type=int, default=44100)
	args = parser.parse_args()
	#con el load a toda la cancion lo convierte en una matriz grandota
	y, sr = librosa.load(str(dirfile))
	o_env = librosa.onset.onset_strength(y, sr=sr, feature=librosa.cqt)
	onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)
	onset_samples = list(librosa.frames_to_samples(onset_frames))
	onset_samples = np.concatenate(onset_samples, len(y))
	#starts = onset_samples[0:-1]
	starts = onset_samples[0:-1]#lo estoy mezclando
	stops = onset_samples[1:]
	analysis_folder = args.output
	samples_folder = os.path.join(args.output,str(numero))
	try:
		os.makedirs(samples_folder)
	except:
		pass

	pbar = ProgressBar()#hace el progreso en la consola
	start_i=0;
	stop_f=0;
	flag="false"
	numero="true"
	canti=0
	tamano_bloque=0;
	audio=[]

	for i, (start, stop) in enumerate(pbar(zip(starts, stops))):

	    if  i+280 > len(zip(starts, stops)) :
		    if canti==5 :
			    audio = y[stop_f-200000:stop_f]
			    audio=add_noise(audio)
			    librosa.frames_to_samples(audio)
			    filename = os.path.join(samples_folder, str(numero)+" "+str(canti) + '.wav')
			    librosa.output.write_wav(filename, audio, sr)
			    canti+=1
			    break
	    
	    if i%30==0 and i!=0 and i>20 and canti<=4:
		    audio = y[start_i:stop_f]
		    if len(audio)>=95000:
			    tamano_bloque=tamano_bloque+len(audio)
			    
			    print("audio",len(audio) )
			    audio=add_noise(audio)
			    librosa.frames_to_samples(audio)
			    filename = os.path.join(samples_folder, str(numero)+" "+str(canti) + '.wav')
			    librosa.output.write_wav(filename, audio, sr)
			    canti+=1
			    flag="false"
	    else:
		if flag=="false":
			start_i=start
			flag="true"
			tamano_bloque=0
		else:
			stop_f=stop
	

	   	
		

