# contaminAND

Repositorio para análisis y publicación de datos de contaminación en
Andalucía. El
[resto de los proyectos están en la web del evento](http://odd-grx-17.github.io) En
este nos concentramos en la contaminación atmosférica, especialmente
de NO y NO2.


El **objetivo**
de este proyecto es crear un API que permita leer desde *apps* o
cualquier programa las lecturas de la calidad del aire de las
diferentes ciudades andaluzas con medidores. En Granada
[exiten una serie de medidores](http://www.granada.org/inet/wambiente.nsf/b1b426e5d69467c3c125763b0031d0c4/9d664bddf7e64554c125764e003875c0!OpenDocument)
que depositan los resultados en
[esta página](http://www.juntadeandalucia.es/medioambiente/atmosfera/informes_siva/feb17/ngr170201.htm). Hay
que extraer periódicamente los resultados de esa página y publicarlos;
ese será el foco principal de este subproyecto coordinado desde la OSL
por [JJ](http://github.com/JJ). 

Los diferentes subproyectos que se incluyen en este son:
* Extracción de datos de la página arriba indicada y almacenamiento de
  los mismos para su fácil disponiblidad, en Google Fusion Tables,
  Google SpreadSheet, o cualquier otro lugar donde estén
  disponibles. También en alguna base de datos.
* Creación de un middleware que publique los datos en un interfaz REST
  fácilmente disponible y sin limitación de peticiones.
* Creación de un *app* que avise sobre niveles de contaminación.
* Narración de la historia de la contaminación en una zona
  determinada.
* Correlación de los datos de contaminación con otros: enfermedades,
  meteorógicos, circulación si existen.
* Publicación de un informe sobre contaminación en una ciudad
  determinada.
* Calibración de los sensores existentes en Granada haciendo
  mediciones in situ y comparándolas.
* Creación de un modelo que extrapole las mediciones de los sensores
  al resto de la ciudad (o ciudades).

## Posibles ideas

  A la vez, el foco del [Open Data Day](http://opendataday.org) es sobre
contaminación. Cualquier otro proyecto relacionado con la misma tendrá
cabida. Por ejemplo
* Sensores *low-cost* de contaminación atmosférica usando cámaras de
  tráfico o la cámara del móvil.
* Observatorio de redes sociales sobre comentarios sobre contaminación
  o palabras relacionadas con los efectos de la contaminación.

## A quién buscamos

Buscamos a gente que pueda
* Idear sensores de bajo coste de contaminación basados en la luz, sensores de bajo coste, monitorización de sensores existentes, es decir, cacharreo.
* Programar un servidor.
* Escribir una historia basada en los datos obtenidos, relacionándolos con datos de salud.
* Desplegar los servidores en infraestructura Azure en la nube.
* Aplicar algoritmos de aprendizaje automático para predecir contaminación a corto y medio plazo.
* Programar apps de móviles.
* Crear juegos que usen los datos de contaminación para gamificar hábitos y evitarla.
* Visualizar de forma original datos de contaminación.
* Crear historias visuales basadas en los datos obtenidos.

## Ciencia abierta

A la vez, este Open Data Day tiene también un foco en la ciencia abierta. Durante el fin de semana se liberarán conjuntos de datos en [Figshare](http://figshare.com) o se usará el Open Science Framework para liberar código, datos e informes técnicos. Se usará RMarkdown o Knitr para crear informes técnicos; si hay quien lo conozca, Jupyter Notebooks también. 

## Quiero participar

Si quieres participar *in situ* o remotamente, añádete
a [la lista de participantes](PARTICIPANTES.md). Adicionalmente, si
vas a estar en la Corrala en algún momento del fin de semana, te
agradeceríamos
que
[te inscribas en MeetUp](https://www.meetup.com/es-ES/Granada-Geek/events/236840299/).
