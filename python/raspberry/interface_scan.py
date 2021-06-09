from Moteur import Moteur
from bottle import run, route, debug, template, request, static_file
import json

moteur_a = Moteur()

@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='ressources')

@route('/scan')
def index():
    return template("interface_scan", request=request)

debug(True)
run(host='192.168.43.158', port=8080)# changer en fonction de l'ip du raspberry