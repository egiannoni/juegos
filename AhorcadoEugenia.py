import random

def palabra_tema():
    palabras = {1:['gato','perro','pato','elefante','lobo','cocodrilo','pajaro'],
                2:['rojo','azul','verde','amarillo','violeta','celeste','marron'],
                3:['milanesa','pure','pizza','salchicha','hamburguesa','empanada']}
    tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))
    pal = palabras[tema][random.randrange(len(palabras[tema]))]
    return(pal)


def armado(pal):
    pal_separada = []
    for y in pal:
        pal_separada.append(['_ '])
    print ('- '*len(pal))
    return(pal_separada)
    

def iteracion(pal,pal_separada):
    ahorcado = [' O ', '/|\\','/ \\']
    cantidad_letras_adivinadas = 0
    cantidad_partes_cuerpo = 0
    sigue = True
    while sigue:
    	letra = input('Ingresa una letra: ').lower()
    	if letra in pal:
    		
    		for pos in range(len (pal)):
    			
    			if pal[pos] == letra:
    				pal_separada[pos] = letra				
    				cantidad_letras_adivinadas = cantidad_letras_adivinadas + 1
    			
    		pal_imprime = ''
    		for y in pal_separada:
    			pal_imprime = pal_imprime +' '+ y[0]
    		print (pal_imprime)
    		if cantidad_letras_adivinadas == len(pal):
    			print ('GANASTE!!')
    			sigue = False
    	else:
    		cantidad_partes_cuerpo=cantidad_partes_cuerpo + 1
    		for x in range(cantidad_partes_cuerpo):
    			print (ahorcado[x])
    		if cantidad_partes_cuerpo == 3:
    			print ('Perdiste!. La palabra era: ', pal)
    			sigue = False
    			
		

def main():
    while True :
        variable_palabra_tema= palabra_tema()
        variable_armado= armado(variable_palabra_tema)
        iteracion(variable_palabra_tema, variable_armado)
        print('Seguimos jugando? (si o no)')
        if not input().lower().startswith('si'):
            break


if __name__ == '__main__':
    main()
