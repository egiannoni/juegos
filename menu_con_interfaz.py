import PySimpleGUI as sg
import csv
import AhorcadoEugenia
import reversegam
import tictactoeModificado


########MODULOS

    
def guardo_archivo (archi,nuevos_datos):
    archi=open('datos_de_juego.csv', 'a+')
    print('nuevos datos:', nuevos_datos)
    writer = csv.writer(archi)
    for row in nuevos_datos:
        writer.writerow(row)
    archi.close()
    
########COLOR INTERFAZ
sg.theme('Bright Colors')

########LAYOUT

layout = [
         [sg.Text('¿Cuál es su nombre?'),sg.InputText(key='nombre')],
         [sg.Text('¿Cuántos años tenés?'), sg.InputText(key='edad')],
         [sg.Text('¿Qué juego te gustaría jugar?')],
         [sg.Button('Ahorcado'), sg.Button('TaTeTi'),sg.Button('Reversi')],
         [sg.Button('Salir')] ]

########WINDOW

window = sg.Window('Juegos para palear el Covid-19', layout)
window.Finalize()

########ITERACION DE LLENADO
    
nuevos_datos=[]
sigo_jugando = True
while True:
    event, values = window.read()
    if event == 'Ahorcado':
        nuevos_datos.append((values['nombre'],values['edad'], "Ahorcado"))
        window.close()
        AhorcadoEugenia.main()
    if event == 'TaTeTi':
        nuevos_datos.append((values['nombre'],values['edad'], "TaTeTi"))
        window.close()
        tictactoeModificado.main()
    if event == 'Reversi':
        nuevos_datos.append((values['nombre'],values['edad'], "Reversi"))
        window.close()
        reversegam.main()
    if event == 'Salir':
        sigo_jugando = False
        window.close()
guardo_archivo('datos_de_juego.csv', nuevos_datos)
       
