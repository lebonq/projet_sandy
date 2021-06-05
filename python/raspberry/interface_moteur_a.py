from Moteur import Moteur
from bottle import route, run, template,  request

moteur_a = Moteur()

@route('/moteura')
def index():
    return template("interface_moteur_a", vitesse = moteur_a.vitesse_value, marche = moteur_a.marche_state,sens = moteur_a.sens_state)

@route('/moteura', method='POST')
def traitement():
    speed = int(request.forms.get("speed"))
    run = request.POST.get("run")
    stop = request.POST.get("stop")
    forward = request.POST.get("forward")
    backward = request.POST.get("backward")

    moteur_a.vitesse(speed)

    print(run)

    if(run is not None):
        moteur_a.marche(True)
    elif(stop is not None):
        moteur_a.marche(False)

    if(forward is not None):
        moteur_a.sens(True)
    elif(backward is not None):
        moteur_a.sens(False)

    return template("interface_moteur_a", vitesse = moteur_a.vitesse_value, marche = moteur_a.marche_state,sens = moteur_a.sens_state)

run(host='192.168.43.158', port=8080)# changer en fonction de l'ip du raspberry