#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

from urllib.request import urlopen
import bs4

class ClientWeb(object):
    """Web client for openweathermap"""
    def __init__(self):
        super(ClientWeb, self).__init__()

    def do_request(self):
        # https://api.openweathermap.org/data/2.5/find?q=Lleida&units=metric&appid=7de50c11e01dc42f66131cb4c8c0dc10
        f = urlopen("https://api.openweathermap.org/data/2.5/find?q=Lleida&units=metric&appid=7de50c11e01dc42f66131cb4c8c0dc10&mode=xml&lang=ca")
        data = f.read()
        f.close()
        return data

    def process_weather(self, html):
        arbre = bs4.BeautifulSoup(html, features="lxml")
        temperature = arbre.find("temperature")
        weather = arbre.find("weather")
        print(temperature["value"] + " and " + weather["value"])
        return None

    def run(self):
        # descarregar-me html
        data = self.do_request()
        # buscar activitats
        data = self.process_weather(data)
        # imprimir resultat
        # print(data)

if __name__ == "__main__":
    c = ClientWeb()
    c.run()
