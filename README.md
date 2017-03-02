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
  
