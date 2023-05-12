import pandas as pd
import csv

datos=pd.read_csv('QRO_DIP_LOC_2018.csv', skiprows=5)
columna_clave_acta= datos['CLAVE_ACTA']
columna_clave_casilla= datos['CLAVE_CASILLA']

for i in range(len(columna_clave_acta)):
    datos.loc[i, 'CLAVE_ACTA'] = str(datos.loc[i, 'CLAVE_ACTA']).replace("'","")
    
for j in range(len(columna_clave_casilla)):
    datos.loc[j, 'CLAVE_CASILLA'] = str(datos.loc[j, 'CLAVE_CASILLA']).replace("'","")

datos.to_csv('archivo_modificado.csv', index=False)