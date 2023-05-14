import pandas as pd
import csv
import matplotlib.pyplot as plt

def limpiar_distritos(df,distrito):
    dist=df.loc[df['DISTRITO_LOCAL']==distrito]
    dist=dist["TOTAL_VOTOS_SACADOS"]
    dist=dist.tolist()
    dist_num=[]
    for i in dist:
        try:
            dist_num.append(int(i))
        except:
            pass

    total_dist=sum(dist_num)
    return total_dist

def votos_casilla(df,distrito,tipo):
    dist=df.loc[(df['DISTRITO_LOCAL']==distrito) & (df['TIPO_CASILLA']==tipo)]
    dist=dist["TOTAL_PERSONAS_VOTARON"]
    dist=dist.tolist()
    dist_num=[]
    for i in dist:
        try:
            dist_num.append(int(i))
        except:
            pass

    total_dist=sum(dist_num)
    return total_dist

def votos_nulos(df,distrito):
    dist=df.loc[df['DISTRITO_LOCAL']==distrito]
    dist=dist["NULOS"]
    dist=dist.tolist()
    dist_num=[]
    for i in dist:
        try:
            dist_num.append(int(i))
        except:
            pass

    total_dist=sum(dist_num)
    return total_dist

def participacion_por_distrito(df,distrito):
    dist=df.loc[df['DISTRITO_LOCAL']==distrito]
    dist=dist["TOTAL_PERSONAS_VOTARON"]
    dist=dist.tolist()
    dist_num=[]
    for i in dist:
        try:
            dist_num.append(int(i))
        except:
            pass

    total_dist=sum(dist_num)
    return total_dist

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
df=pd.read_csv('QRO_DIP_LOC_2018.csv', skiprows=5)

##En esta consulta obtendremos cuantas casillas hay en cada estado - 01
# SMALL_SIZE = 4.5
# plt.rc('font', size=SMALL_SIZE)
# plt.rc('axes', titlesize=SMALL_SIZE)
# plt.rc('ytick', labelsize=10) 
# cantidad_de_casillas_p_estado=df["DISTRITO_LOCAL"].value_counts()
# plt.bar(cantidad_de_casillas_p_estado.index,cantidad_de_casillas_p_estado)
# plt.show()

##En esta consulta obtendremos cuantas tipos de casillas distintas hay - 02
# cantidad_tipos_de_casillas=df["TIPO_CASILLA"].value_counts()
# plt.bar(cantidad_tipos_de_casillas.index,cantidad_tipos_de_casillas)
# plt.show()

##En esta consulta graficaremos la cantidad casillas con ubicaciones urbanas y no urbanas - 03
# casillas_urbana=df.query('UBICACION_CASILLA == "URBANA"')
# casillas_urbana=casillas_urbana.loc[:,'UBICACION_CASILLA']
# casillas_no_urbana=df.query('UBICACION_CASILLA != "URBANA"')
# casillas_no_urbana=casillas_no_urbana.loc[:,'UBICACION_CASILLA']
# plt.bar(['Urbano','No urbano'], [len(casillas_urbana),len(casillas_no_urbana)])
# plt.show()

##En esta consulta graficaremos la cantidad de tipos de actas distintas - 04
# cantidad_tipos_de_actas=df["TIPO_ACTA"].value_counts()
# plt.bar(cantidad_tipos_de_actas.index,cantidad_tipos_de_actas)
# plt.show()

##En esta consulta obtendremos la cantidad de votos obtenidos por distrito - 05
# distritos_distintos=df["DISTRITO_LOCAL"].unique().tolist()

# lista_totales=[]
# for i in distritos_distintos:
#     lista_totales.append(limpiar_distritos(df,i))

# plt.rc('font', size=4.5)
# plt.rc('axes', titlesize=20)
# plt.rc('ytick', labelsize=10) 
# plt.bar(distritos_distintos,lista_totales)
# plt.show()

#____Analisis del Total de Votos que fueron capturados en casillas básicas - 06_____
# distritos_distintos=df["DISTRITO_LOCAL"].unique().tolist()
# casilla_basica="B"
# total_votos_casillas_basicas=[]
# for i in distritos_distintos:
#     total_votos_casillas_basicas.append(votos_casilla(df,i,casilla_basica))

# plt.rc('font', size=10)
# plt.rc('axes', titlesize=20)
# plt.rc('ytick', labelsize=10)
# plt.rc('xtick', labelsize= 3.9)
# plt.title('Total de personas que votaron en casilla Basica por distrito')
# plt.xlabel('Distrito')
# plt.ylabel('Total personas que votaron en casillas Basica')
# plt.bar(distritos_distintos,total_votos_casillas_basicas)
# plt.show()

#____Analisis del Total de Votos que fueron capturados en casillas especiales - 07_____
# distritos_distintos=df["DISTRITO_LOCAL"].unique().tolist()
# casilla_especial="S"
# total_votos_casillas_especiales=[]
# for i in distritos_distintos:
#     total_votos_casillas_especiales.append(votos_casilla(df,i,casilla_especial))

# plt.rc('font', size=10)
# plt.rc('axes', titlesize=20)
# plt.rc('ytick', labelsize=10)
# plt.rc('xtick', labelsize= 3.9)
# plt.title('Total de personas que votaron en casilla Especial por distrito')
# plt.xlabel('Distrito')
# plt.ylabel('Total personas que votaron en casillas Especial')
# plt.bar(distritos_distintos,total_votos_casillas_especiales)
# plt.show()

#________________Analisis de Votos Nulos por distrito - 08_________________________
# distritos_distintos=df["DISTRITO_LOCAL"].unique().tolist()

# total_votos_nulos=[]
# for i in distritos_distintos:
#     total_votos_nulos.append(votos_nulos(df,i))

# plt.rc('font', size=10)
# plt.rc('axes', titlesize=20)
# plt.rc('ytick', labelsize=10)
# plt.rc('xtick', labelsize= 3.9)
# plt.title('Total de votos nulos por distrito')
# plt.xlabel('Distrito')
# plt.ylabel('Total votos nulos')
# plt.bar(distritos_distintos,total_votos_nulos)
# plt.show()

#_____Analisis de entidad federativa con mayor participación ciudadana - 09______
distritos_distintos=df["DISTRITO_LOCAL"].unique().tolist()

total_participacion=[]
for i in distritos_distintos:
    total_participacion.append(participacion_por_distrito(df,i))

plt.rc('font', size=10)
plt.rc('axes', titlesize=20)
plt.rc('ytick', labelsize=10)
plt.rc('xtick', labelsize= 3.9)
plt.title('Participacion ciudadana en cada distrito')
plt.xlabel('Distrito')
plt.ylabel('Total participantes')
plt.bar(distritos_distintos,total_participacion)
plt.show()