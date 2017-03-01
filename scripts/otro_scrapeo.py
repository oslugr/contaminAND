# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

URL_BASE = "http://www.juntadeandalucia.es/medioambiente/atmosfera/informes_siva/"
MAX_PAGES = 1
counter = 0

for i in range(1, MAX_PAGES):

    # Construyo la URL
    if i > 1:
        url = "%spage/%d/" % (URL_BASE, i)
    else:
        url = URL_BASE

    # Realizamos la petición a la web
    req = requests.get(url)
    # Comprobamos que la petición nos devuelve un Status Code = 200
    statusCode = req.status_code
    if statusCode == 200:

        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "html.parser")

        # Obtenemos todos los divs donde estan las entradas
        entradas = html.find_all('div', {'class': 'col-md-4 col-xs-12'})

        # Recorremos todas las entradas para extraer el título, fecha y ciudad
        for entrada in entradas:
            counter += 1
            # titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
            # fecha = entrada.find('span', {'class': 'fecha'}).getText()
			ciudad = ciudad.find('span', {'class': 'ciudad'}).getText()

            # Imprimo el Título, Fecha y ciudad de las entradas
            print "%d - %s  |  %s  |  %s" % (counter, titulo, fecha, ciudad)

    else:
        # Si ya no existe la página y me da un 400
        break
