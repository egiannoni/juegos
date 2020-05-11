import AhorcadoEugenia
import reversegam
import tictactoeModificado
import csv


def abro_datos():
    archi=open('datos_de_juego.csv', 'a+')
    return(archi)

def datos_jugador ():
    nombre=input('Ingresa tu nickname:')
    edad=input('ingresa tu edad:')
    return (nombre,edad)

def juegos():
    sigo_jugando = True
    juego=''
    while sigo_jugando:
        print('''Elegí con qué juego querés jugar:
            1.- Ahorcado
            2.- Ta-TE-TI
            3.- Otello
            4.- Salir''')
        opcion = input()
        if opcion == '1':
            juego= 'Ahorcado'
            AhorcadoEugenia.main()
        elif opcion == '2':
            juego= 'Tictactoe'
            tictactoeModificado.main()
        elif opcion == '3':
            juego= 'reversi'
            reversegam.main()
        elif opcion == '4':
            sigo_jugando = False
    return(juego)
    
def guardo_archivo (archi,nombre,edad,juego):
    nuevos_datos=[[nombre,edad,juego]]
    print('nuevos datos:',nuevos_datos)
    writer = csv.writer(archi)
    for row in nuevos_datos:
        writer.writerow(row)
    archi.close()

########## PROGRAMA PRINCIPAL ##########

def main(args):
    archi2 = abro_datos()
    nombre2,edad2 = datos_jugador()
    juego2 = juegos()
    guardo_archivo(archi2,nombre2,edad2,juego2)
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
