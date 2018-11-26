def concatenacionBin3(ancla,frecuencia,delta):
    anclaBin = "{0:b}".format(ancla)
    frecuenciaBin = "{0:b}".format(frecuencia)
    deltaBin = "{0:b}".format(delta)

    anclaRest = '0' * (18 - len(anclaBin) )
    frecuenciaRest = '0' * (18 - len(frecuenciaBin) )
    deltaRest = '0'  *(28 - len(deltaBin) ) 

    anclaFull = anclaRest + anclaBin
    frecuenciaFull = frecuenciaRest + frecuenciaBin
    deltaFull = deltaRest + deltaBin

    numeroFull = anclaFull + frecuenciaFull + deltaFull

    return int(numeroFull,2)

def concatenacionBin2(ancla,id):
    anclaBin = "{0:b}".format(ancla)
    idBin = "{0:b}".format(id)
    
    anclaRest = '0' * (32 - len(anclaBin) )
    idRest = '0' * (32 - len(idBin) )

    anclaFull = anclaRest + anclaBin
    idFull = idRest + idBin

    numeroFull = anclaFull + idFull

    return int(numeroFull,2)
