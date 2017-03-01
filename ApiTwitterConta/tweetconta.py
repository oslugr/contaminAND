#!/usr/bin/python
#coding: utf-8

# CopyRight 2014 Allan Psicobyte (psicobyte@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# Por si se puede utilizar en hackatón, pero no encuentro ninguna cuenta de Twitter.

import os, re, sys, getopt, tweepy, ConfigParser, codecs, locale

def main(argv):

    cuenta_de_la_dgt = "informaciondgt"

    # http://stackoverflow.com/questions/4545661/unicodedecodeerror-when-redirecting-to-file
    sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 

    config = open_config()

    imagen = ""
    reply = ""

    show_user(config,cuenta_de_la_dgt,0)
    sys.exit()

def open_config():
    """Busca y abre un archivo INI para extraer las contraseñas y la configuración
    Por orden de preferencia, busca el archivo en /home/USER/twcli.ini, en /home/USER/.twcli y en twcli.ini
    """ 

    home_dir_ini_file = os.path.join(os.path.expanduser("~"),"twcli.ini")
    home_dir_ini_hidden_file = os.path.join(os.path.expanduser("~"),".twcli")
    my_dir_ini_file = os.path.join(os.path.abspath(os.path.dirname(__file__)),"twcli.ini")

    if os.path.isfile(home_dir_ini_file):
        configfile = home_dir_ini_file
    elif os.path.isfile(home_dir_ini_hidden_file):
        configfile = home_dir_ini_hidden_file
    elif os.path.isfile(my_dir_ini_file):
        configfile = my_dir_ini_file
    else:
        show_error("Falta archivo INI")
        sys.exit()

    config = ConfigParser.ConfigParser()

    config.read(configfile)

    if not config.has_section("Preferences"):
        config.add_section("Preferences")

    if not config.has_option("Preferences", "tweets_per_page"):
        config.set("Preferences", "tweets_per_page", "20")
    if not config.get("Preferences", "tweets_per_page").isdigit:
        config.set("Preferences", "tweets_per_page", "20")

    if not config.has_option("Preferences", "color_schema"):
        config.set("Preferences", "color_schema", "red")
    if not config.get("Preferences", "color_schema"):
        config.set("Preferences", "color_schema", "red")

    return config


def login_api(config):
    """Se loguea en twitter mediante OAuth con las claves extraídas del archivo de configuración"""

    try:
        consumer_key= config.get("Keys", "consumer_key")
        consumer_key_secret= config.get("Keys", "consumer_key_secret")
        access_token= config.get("Keys", "access_token")
        access_token_secret= config.get("Keys", "access_token_secret")
    except:
        show_error("faltan datos de clave en CONFIG, LECHES")
        sys.exit()

    auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth)

    if api.verify_credentials():
        return api
    else:
        show_error("error de autorizacion")
        sys.exit()



def show_user(config,user,view_details_user=0):
    """Muestra detalles de un usuario (si view_details_user=1) y sus últimos tweets"""

    api = login_api(config)

    s = api.get_user(user)

    traffic_regexp = u'\#([a-zA-ZÁÉÍÓÚáéíóúÇç]*)\s\w*\s?(\w+)[\s\w\/ÁÉÍÓÚáéíóúÇç]+\#(\w+)\s\(pk\s([\d\.]*)\s?\w*\s?([\d\.]*)\s?([\w\s\.]+)\)\s?([\s\w\/\-\.ÁÉÍÓÚáéíóúÇç]*)\s\#DGT(\w+)[\s\#\w]+(http://[\w\W]+)'

    print u'"Estado","Nivel","Vía","Kilómetro Inicial","Kilómetro Final","Sentido","Provincia","Población","URL"'

    if unicode(s.protected) != "True" or unicode(s.following) == "True":
        for s in tweepy.Cursor(api.user_timeline, id= user).items(config.getint("Preferences", "tweets_per_page")):

            resultado = re.search(traffic_regexp,s.text)

            if resultado:

                linea = ""

                for frase in resultado.groups():
                    if linea == "":
                        linea = '"' + frase + '"'
                    else:
                        linea = linea + ',"' + frase + '"'

                print linea


def show_error(error):
    """Muestra los errores, o los mostrará cuando esta función esté hecha"""
    
    print error




if __name__ == "__main__":
main(sys.argv[1:])
