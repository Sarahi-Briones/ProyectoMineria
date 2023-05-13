import pandas as pd
import csv

#______________Limpieza del archivo base_______________________________
datos=pd.read_csv('QRO_DIP_LOC_2018.csv', skiprows=5)
columna_clave_acta= datos['CLAVE_ACTA']
columna_clave_casilla= datos['CLAVE_CASILLA']

#Limpieza de la columna CLAVE_ACTA
for i in range(len(columna_clave_acta)):
    if str(datos.loc[i, 'CLAVE_ACTA']).find("E"):
        datos.loc[i, 'CLAVE_ACTA']=str(datos.loc[i, 'CLAVE_ACTA'])[1:]
    else:
        datos.loc[i, 'CLAVE_ACTA'] = str(datos.loc[i, 'CLAVE_ACTA'].replace("'",""))
    
#Limpieza de la columna CLAVE_CASILLA
for j in range(len(columna_clave_casilla)):
    if str(datos.loc[j, 'CLAVE_CASILLA']).find("E"):
        datos.loc[j, 'CLAVE_CASILLA']=str(datos.loc[j, 'CLAVE_CASILLA'])[1:]
    else:
        datos.loc[j, 'CLAVE_CASILLA'] = str(datos.loc[j, 'CLAVE_CASILLA'].replace("'",""))

#Guardamos el nuevo archivo
datos.to_csv('archivo_modificado.csv', index=False)

#Visualizaciones importantes del archivo base modificado

#_______________________________________________________________________________

#________________1- Analisis de Votos Contabilizados por entidad________________

#________________2- Analisis de Votos Nulos por entidad_________________________

#____3- Analisis de Votos Contabilizados que fueron capturados en casillas básicas_____

#____4- Analisis de Votos Contabilizados que fueron capturados en casillas especiales__

#_____5- Analisis de entidad federativa con mayor participación ciudadana______
