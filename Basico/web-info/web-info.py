# ***************************************** Ejercicio **************************************************
# Diseñar y codificar un script en Python que permita hacer peticiones “GET” a un conjunto de sitios web. 
# De la respuesta a la petición web extraiga información detallada del sitio  

import socket 
import requests

def getWebInfo(host) :
    ip = socket.gethostbyname(host)
    url = 'http://' + host
    request = requests.get(url)
    headers = request.headers
    server = headers['server'] if 'server' in headers else 'Unknown'
    contentType = headers['content-type']  if 'content-type' in headers else 'Unknown'
    contentEnconding = headers['content-encoding'] if 'content-encoding' in headers else 'Unknown'
    return {
        'Host' : host, 'Ip' : ip, 'Server' : server, 
        'Content-Encoding' : contentEnconding, 'Content-Type' : contentType
    }


def dictionaryToLines(dictionary) :
    lines = []
    for key, value in dictionary.items():
        lines.append('%s : %s\n' % (key, value))
    return lines


hostsList = [
    'www.google.com',
    'www.facebook.com',
    'www.wikipedia.com',
    'www.twitter.com',
    'www.facebook.com',
    'www.deluxebox.co'
]

filePath = 'hosts-info.txt'


file = open(filePath, 'w')
for host in hostsList :
    print('Obteniendo informacion de %s ...' % (host))
    file.writelines(dictionaryToLines(getWebInfo(host)))
    file.write('\n')
file.close()
print('Informacion guardada en %s' % (filePath))