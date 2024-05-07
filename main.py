import os

Usuario1 = 'Usuario 1'
Usuario2 = 'Usuario 2'
palabra_secreta = ''
palabra_cifrada= ''
num_intentos = 0
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

def mostrar_banner_inicio():
    os.system("cls")
    print(banner_inicio)

def mostrar_estado_partida():
   # os.system("cls")
    print()
    print('Datos del juego:')
    print('Palabra secreta:' + palabra_cifrada)
    print('Numero de intenos:' + str(num_intentos))

def mostrar_menu_incial():
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
    #Devuelve True si el dato de entrada es un string, de longitud 1 y una letra. En caso contrario devuelve False
    if isinstance(letra, str) and len(letra)==1 and letra.isalpha:
        return True
    else:
        return False

def es_final_juego():
    if num_intentos >= 10 or palabra_cifrada.count("_")==0:
        return True
    else:
        return False     

def cifrar_palabra():
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
   num_apariciones = palabra_secreta.count(letra)
   print ("La letra " + letra + " aparece " + str(num_apariciones) + " veces")
   palabra_lista=list(palabra_cifrada)
   for i in range(num_apariciones):
       index = palabra_secreta.index(letra)
       print("la letra " + letra + "aparece en la posicion " + str(index))
       palabra_lista[index]=letra
       palabra_secreta=palabra_secreta.replace(letra, "_", 1)
       print("palabra secreta ahora: " +palabra_secreta)
   palabra_cifrada = "".join(palabra_lista)     

def mostrar_ganador():
    os.system("cls")
    if num_intentos >= 10:
        print("Enhorabuena " + Usuario1 + " !!!!!!")
        print(Usuario2 + " no ha sido capaz de descubrir tu palabra")
    elif palabra_cifrada.count("_")==0:
        print("Enhorabuena " + Usuario2 + " !!!!!!")
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
            num_intentos=num_intentos+1
            comprobar_intento(letra)
            final_juego=es_final_juego()
    mostrar_ganador()

os.system("cls")

mostrar_banner_inicio()

eleccionMenu=0
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





