#!/usr/bin/python
#coding: utf-8

# CopyRight 2017 Alex bueno francissco.manuel.alexander@gmail.com @Phoenix_Alx
# 2014 Allan Psicobyte (psicobyte@gmail.com)
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


import os, re, sys, tweepy,ConfigParser
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from os import path  
from stop_words import get_stop_words
from images2gif import writeGif


def open_config():
    """Busca y abre un archivo INI para extraer las contraseñas y la configuración
    Por orden de preferencia, busca el archivo en /home/USER/twcli.ini, en /home/USER/.twcli y en twcli.ini
    """ 

    home_dir_ini_file = os.path.join(os.path.expanduser("~"),"contacloud.ini")
    home_dir_ini_hidden_file = os.path.join(os.path.expanduser("~"),".twcli")
    my_dir_ini_file = os.path.join(os.path.abspath(os.path.dirname(__file__)),"contacloud.ini")

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
    
def llamoTweeter():
    ''' Nos identificamos ante twetter'''
    #quien es? soy yo
    config = open_config();
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
def buscoTweets(api):
    '''busco los tweets que contengan la palabra contaminacion'''
    textos={'total':[]};
    latitud_gra="37.25";#centro de la provincia
    longitud_gra="-3.25";#centro de la provincia
    radio_gra="100km";
    query_gra="(clima OR contaminacion OR polucion OR humo OR atasco OR niebla OR respiración OR asma  OR suciedad OR sucio )  -politico -politica -filter:retweets";
    maxTweets = 1000000;
    granada=latitud_gra+","+longitud_gra+","+radio_gra;
    #nos quedamos con los que no sean rt
    for tweets in tweepy.Cursor(api.search, q=query_gra, lang='es',locale='es',geocode=granada,count=maxTweets, include_entities=True).pages():
        for tp in tweets:
            #print(tp.text.encode('utf-8').lower())
            #print(tp.retweeted);
            #print(tp.geo);
            #print(tp.created_at);
            dia=str(tp.created_at.date());
            textito=tp.text.lower();
            if (dia in textos.keys()):
                textos[dia].append(textito);
            else:
                textos[dia]=[textito];
            textos['total'].append(textito);
            
            #print(tp.place);
        
    return textos;
def nubePalabras(textos,fecha,name_file_ou="contaminacloud_"):
    '''nube de palabras '''
    text_textos=" ".join(textos);
    #filtramos palabras y dejamos las mayores de 4 caracteres
    text_filtrar_list=text_textos.split(" ");
    text_filtradas=[p for p in text_filtrar_list if len(p)>3];
    text=" ".join(text_filtradas);
    d = path.dirname(__file__)
    plt.axis("off")

    # lower max_font_size
    #wordcloud = WordCloud(max_font_size=40).generate(text)
    #plt.figure()
    #plt.imshow(wordcloud)
    #plt.axis("off")
    #plt.show()
    granada_mask = np.array(Image.open(path.join(d, "provincia-de-granada.png")))
    stopwords = set(get_stop_words('spanish'))
    stopwords.add("https")
    stopwords.add("co")
    wc = WordCloud(background_color="white", max_words=200, mask=granada_mask,
               stopwords=stopwords)
    # generate word cloud
    wc.generate(text)
    #print(wc.words_)

    # store to file
    name_file_output=name_file_ou+fecha+".png";
    plt.title(fecha);
    #wc.to_file(path.join(d, name_file_output))
    
    # show
    plt.title(fecha)
    
    plt.imshow(wc)
    plt.savefig(path.join(d, name_file_output))
    plt.axis("off")
    
    plt.figure()
    #plt.imshow(granada_mask, cmap=plt.cm.gray)
    plt.axis("off")
    #plt.show()
def creaGif(fechas,name_file_ou="contaminacloud_"):
    '''creamos gif'''
    
    file_names = [os.path.join(os.path.abspath(os.path.dirname(__file__)),name_file_ou+f+".png") for f in fechas if fechas!='total'];
    command='convert -delay 500 -loop 0 %s %s' % (' '.join(file_names),name_file_ou+"all.gif");
    os.system(command )
def main():
    api=llamoTweeter();
    textos=buscoTweets(api);
    print ("número tweets",len(textos))
    fechas=textos.keys();
    fechas=sorted(fechas);
    for k in fechas:
        nubePalabras(textos[k],k);
        print ("fecha procesada",k)
    
    creaGif(fechas)
    
if __name__ == "__main__":
    main()
