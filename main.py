import os

Usuario1 = 'Usuario 1'
Usuario2 = 'Usuario 2'
palabra_secreta = ''
palabra_cifrada= ''
num_intentos = 0
lista_letras = []
banner_inicio =  '''
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
AHORCADO = ['''
      +---+
          |
          |
          |
          |
          |
    =========''','''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

def mostrar_banner_inicio():
    # muestra el dibujo del inicio del juego
    os.system("cls")
    print(banner_inicio)
    input()

def mostrar_estado_partida():
    # muestra los datos de la partida:
    # La palabra secreta con las letras ya descubiertas
    # el número de intentos
    # el estado del dibujo dle ahorcado
    # os.system("cls")
    print()
    print('Datos del juego:')
    print('Palabra secreta:' + palabra_cifrada)
    print('Lista de letras introducidas: ' , lista_letras)
    print('Numero de intentos:' + str(num_intentos))
    print(AHORCADO[num_intentos])

def mostrar_menu_incial():
    # Muestra el menú inical de la partida
    os.system("cls")
    print()
    print('Datos del juego:')
    print('Usuario 1:' + Usuario1)
    print('Ususario 2:' + Usuario2)
    print('Elije una opción:')
    print('1. Cambiar nombre al Usuario 1')
    print('2. Cambiar nombre al Usuario 2')
    print('3. Comenzar el juego')
    print()

def es_letra(letra):
    #Devuelve True si el dato de entrada es un string, de longitud 1 y una letra y además se cumple que en Unicode es un valor entre la A (64) y la z (122). En caso contrario devuelve False
    if isinstance(letra, str) and len(letra)==1 and letra.isalpha and ord(letra)>64 and ord(letra)< 122:
        return True
    else:
        return False

def es_final_juego():
    # Devuelve True si se cumple alguna condición para terminar el juego. False en caso contrario
    if num_intentos >= 7 or palabra_cifrada.count("_")==0:
        return True
    else:
        return False     

def cifrar_palabra():
    #crea una palabra con el mismo número de letras que la palabra secretra pero sustiutyendo cada caracter por un guión bajo (_)
    palabra_cifrada=palabra_secreta
    l = list(palabra_cifrada)
    for i in range(len(palabra_secreta)):
        l[i] = "_"
        palabra_cifrada = "".join(l)
    print (palabra_cifrada)
    return palabra_cifrada

def comprobar_intento(letra):
    #Comprueba cuantas veces aparece
    global palabra_cifrada
    global palabra_secreta
    global num_intentos
    num_apariciones = palabra_secreta.count(letra)
    if num_apariciones==0:
       num_intentos=num_intentos+1
    lista_letras.append(letra)
    palabra_lista=list(palabra_cifrada)
    for i in range(num_apariciones):
       index = palabra_secreta.index(letra)
       palabra_lista[index]=letra
       palabra_secreta=palabra_secreta.replace(letra, "_", 1)
    palabra_cifrada = "".join(palabra_lista)     

def mostrar_ganador():
    os.system("cls")
    if num_intentos >= 7:
        print(AHORCADO[num_intentos])
        print("Enhorabuena " + Usuario1 + " !!!!!!")
        print(Usuario2 + " no ha sido capaz de descubrir tu palabra")
    elif palabra_cifrada.count("_")==0:
        print(AHORCADO[num_intentos])
        print("¡¡¡¡¡¡ Enhorabuena " + Usuario2 + ", te has salvado !!!!!!")
        print("Has conseguido decubrir la palabra secreta:")
        print(palabra_cifrada)

def comenzar_juego():
    global num_intentos
    final_juego=False
    print('Turno de ' + Usuario2)   
    while not final_juego:
        mostrar_estado_partida()
        letra=input('Introduce una letra: ')
        if es_letra(letra) ==  True:
            comprobar_intento(letra)
            final_juego=es_final_juego()
    mostrar_ganador()

mostrar_banner_inicio()

eleccionMenu=0
# mientras el usuario no introduzca un 3 se seguirá mostrado el menú
while eleccionMenu != '3':
    mostrar_menu_incial()
    
    eleccionMenu=input('Selecciona una opción [1-3]: ')
    match eleccionMenu:
        case '1':
            Usuario1=input("Nombre del Usuario1: ")
        case '2':
            Usuario2=input("Nombre del Usuario2: ")

print()
palabra_secreta=input(Usuario1 + ', introduce la palabra a adivinar: ')
palabra_cifrada=cifrar_palabra()
comenzar_juego()





