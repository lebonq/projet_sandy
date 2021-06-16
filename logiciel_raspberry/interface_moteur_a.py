from Moteur import Moteur
from bottle import run, route, debug, template, request, static_file
import json

moteur_a = Moteur()

@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='ressources')

@route('/_change_speed')
def change_speed():
    moteur_a.vitesse(request.params.get('vitesse', 0, type=int))
    return json.dumps({'speed': moteur_a.vitesse_value})

@route('/_run')
def run_motor():
    moteur_a.marche(not bool(moteur_a.marche_state))
    if(moteur_a.marche_state == True):
        return json.dumps({'run_aff' : "Marche"})
    elif(moteur_a.marche_state == False):
        return json.dumps({'run_aff' : "Arrêt"})
    else:
        return json.dumps({'run_aff' : "Alors la c'est pas normal"})

@route('/_sens')
def sens_motor():
    moteur_a.sens(not bool(moteur_a.sens_state))
    if(moteur_a.sens_state == True):
        return json.dumps({'sens' : "Avant"})
    elif(moteur_a.sens_state == False):
        return json.dumps({'sens' : "Arrière"})
    else:
        return json.dumps({'sens' : "Alors la c'est pas normal"})

@route('/moteura')
def index():
    return template("interface_moteur_a", request=request)

debug(True)
run(host='192.168.43.158', port=8080)# changer en fonction de l'ip du raspberry