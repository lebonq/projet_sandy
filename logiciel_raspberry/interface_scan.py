from Scanner import Scanner
from bottle import run, route, debug, template, request, static_file
import json

my_scanner = Scanner()

@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='ressources')

@route('/_get_position')
def change_speed():
    return json.dumps({'x': my_scanner.x_aff_barre, 'y': my_scanner.y_aff_support})

@route('/_get_input_needed')
def change_speed():
  return json.dumps({'user_input': my_scanner.need_user_input})

@route('/_get_pins')
def change_speed():
  return json.dumps({'pins_warning': my_scanner.warning_pin})

@route('/_run_again')
def run_again():
  if(my_scanner.need_user_input == True and my_scanner.allere_retour_done <= my_scanner.nb_aller_retour):
    my_scanner.need_user_input = False
    my_scanner.launch()
    

@route('/scan')
def index():
    return template("interface_scan", request=request)

debug(True)
run(host='192.168.43.158', port=8080)# changer en fonction de l'ip du raspberry
