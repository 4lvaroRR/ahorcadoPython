import os

Usuario1 = 'Usuario 1'
Usuario2 = 'Usuario 2'
palabraSecreta = ''
numIntentos = 0
bannerInicio =  '''
      _=====_                               _=====_
     / _____ \                             / _____ \\
   +.-'_____'-.---------------------------.-'_____'-.+
  /   |     |  '.        S O N Y        .'  |  _  |   \\
 / ___| /|\ |___ \                     / ___| /_\ |___ \\
/ |      |      | ;  __           _   ; | _         _ | ;
| | <---   ---> | | |__|         |_:> | ||_|       (_)| |
| |___   |   ___| ;SELECT       START ; |___       ___| ;
|\    | \|/ |    /  _     ___      _   \    | (X) |    /|
| \   |_____|  .','" "', |___|  ,'" "', '.  |_____|  .' |
|  '-.______.-' /       \ANALOG/       \  '-._____.-'   |
|               |       |------|       |                |
|              /\       /      \       /\               |
|             /  '.___.'        '.___.'  \              |
|            /                            \             |
 \          /                              \           /
  \________/                                \_________/
  '''

def mostrarBannerInicio():
    print(bannerInicio)

def mostrarMenuIncial():
    print()
    print()
    print('Datos del juego:')
    print('Usuario 1:' + Usuario1)
    print('Ususario 2:' + Usuario2)
    print('Elije una opción:')
    print('1. Cambiar nombre al Usuario 1')
    print('2. Cambiar nombre al Usuario 2')
    print('3. Comenzar el juego')
    print()

def esLetra(letra):
    #Devuelve True si el dato de entrada es un string, de longitud 1 y una letra. En caso contrario devuelve False
    if isinstance(letra, str) and len(letra)==1 and letra.isalpha:
        return True
    else:
        return False
    

def comprobarIntento(letra):
   #Comprueba cuantas veces aparece
   num_apariciones = palabraSecreta.count(letra)
   print ("La letra " + letra + " aparece " + str(num_apariciones) + " veces")


def comenzarJuego():
    print('Turno de ' + Usuario2)
    letra=input('Introduce una letra')
    if esLetra(letra) ==  True:
        comprobarIntento(letra)

os.system("cls")

mostrarBannerInicio()

eleccionMenu=0
while eleccionMenu != '3':
    mostrarMenuIncial()
    
    eleccionMenu=input('Selecciona una opción [1-3]: ')
    match eleccionMenu:
        case '1':
            Usuario1=input("Nombre del Usuario1: ")
        case '2':
            Usuario2=input("Nombre del Usuario2: ")

print()
palabraSecreta=input(Usuario1 + ', introduce la palabra a adivinar: ')
comenzarJuego()





