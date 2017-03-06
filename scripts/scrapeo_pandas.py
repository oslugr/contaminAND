import pandas as pd
import requests
from bs4 import BeautifulSoup


def scraping_dias(dia):

    if dia<10:
        dia = '0'+str(dia)
    
    
    URL = 'http://www.juntadeandalucia.es/medioambiente/atmosfera/informes_siva/feb17/ngr1702{}.htm'.format(dia)
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    tablas = soup.find_all('table')

    datos_cont = pd.DataFrame(columns = ['FECHA-HORA','SO2','PART','NO2','CO','O3'])
    estaciones_dict = {}
    for n,tabla in enumerate(tablas):
        #Separamos cada uno de los medidores
        filas = tabla.find_all('tr')

        #USAR ALGO COMO ESTO PARA SACAR LAS CABECERAS DE LAS COLUMNAS(EL NUMERO QUE HAY DE COLUMNAS ASI COMO SUS NOMBRES,
        #QUE LUEGO USAREMOS PARA CREAR LOS DFs AUTOMATICAMENTE
    ##    print(tabla.find_all('td',{'class':'CabTabla'}))
        
        for x,fila in enumerate(filas):
            if ('Provincia') in fila.text:
##                print('AQUI EMPIEZA UNA TABLA')
                nombre_DF = []
                
                #La tabla cabecera con los datos de localizacion del sensor(provincia,municipio...)
                for i in range(x,x+4):
                    nombre_DF.extend(filas[i].text.split()[1:])
                nombre_DF = '_'.join(nombre_DF)+'_DF'
    ##            print(nombre_DF)


                for tr in tablas[n+1].find_all('tr'):
                    tr_list = []
                    nota = True
                    
                    for td in tr.find_all('td'):
                        if ('Nota') not in td.text:
                            tr_list.append(td.text)
                            nota = False
                            
                    if not nota:       #Al final de las tablas hay una fila con una nota, sin datos         
                        datos_row = pd.DataFrame({'FECHA-HORA':tr_list[0],
                                                  'SO2':tr_list[1],
                                                  'PART':tr_list[2],
                                                  'NO2':tr_list[3],
                                                  'CO':tr_list[4],'O3':tr_list[5]}
                                                 ,index=[0])
                        datos_cont = datos_cont.append(datos_row)
                #La primera fila son los nombres de las columnas, asi que la quitamos
                datos_cont = datos_cont.reset_index(drop=True).drop([0])
                estaciones_dict[nombre_DF] = datos_cont
                datos_cont = pd.DataFrame(columns = ['FECHA-HORA','SO2','PART','NO2','CO','O3'])
            elif ('Nota:') in fila.text:
                
                print(60*'#')

    #En estaciones_dict tenemos ahora cada una de las estaciones(key) con sus respectivos valores en un DF(value)
##    print(estaciones_dict)

    DF = estaciones_dict.get('GRANADA_GRANADA_PALACIO_DE_CONGRESOS_PASEO_DE_VIOLÓN_S/N_DF')
    return DF
##DF.to_csv('Congresos_DATOS.csv')

DF_final = pd.DataFrame()
for x in range(1,28):
    DF = scraping_dias(x)
    DF_final = DF_final.append(DF)
DF_final.to_csv('Congresos_DATOS_varios_dias.csv')
