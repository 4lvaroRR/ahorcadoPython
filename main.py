Usuario1 = 'Usuario 1'
Usuario2 = 'Usuario 2'
palabraSecreta = ''
numIntentos = 0
bannerInicio =  '''
      _=====_                               _=====_
     / _____ \                             / _____ \
   +.-'_____'-.---------------------------.-'_____'-.+
  /   |     |  '.        S O N Y        .'  |  _  |   \
 / ___| /|\ |___ \                     / ___| /_\ |___ \
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

def comenzarJuego():
    print('Turno de ' + Usuario2)

    

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





