# Importamos el random para que nos genere posición aleatoria de los barcos
import random

# Definimos las variables de nuestro juego
BARCO = 'B'
AGUA = '~'
HUNDIDO = 'X'
FALLO = 'O'
BARCOS_TAMAÑOS = [2,3,3,4,5]
TABLERO_TAMAÑO = 10

# Creamos la función del tablero, con sus filas y columnas
def crear_tablero():
 tablero = [["~" for _ in range(TABLERO_TAMAÑO)] for _ in range(TABLERO_TAMAÑO)]
 return tablero

# Imprimimos el tablero y la posición del agua y los barcos
def imprimir_tablero(tablero, ocultar_barcos=True):
 print(" " + " ".join(str(i) for i in range(10)))
 for i in range(10):
  fila = [str(i)]
  for j in range(10):
   if ocultar_barcos and tablero [i][j] == BARCO:
    fila.append(AGUA)
   else:
    fila.append(tablero[i][j])
  print((" ").join(fila))

# Generamos la posición aleatoria de nuestra flota
def colocar_barcos(tablero):
 for tam in BARCOS_TAMAÑOS:
  while True:
   fila= random.randint(0, TABLERO_TAMAÑO - 1)
   columna = random.randint(0, TABLERO_TAMAÑO - 1)
   direccion = random.choice(["horizontal", "vertical"])
   if posicion_valida(tablero, fila, columna, tam, direccion):
    colocar_barco(tablero, fila, columna, tam, direccion)
    break

# Verificamos que la posición es correcta dentro del tablero
def posicion_valida(tablero, fila, columna, tam, direccion):
 if direccion == "horizontal":
  if columna + tam > TABLERO_TAMAÑO:
   return False
  return all(tablero[fila][columna + i] == AGUA for i in range(tam))
 elif direccion == "vertical":
  if fila + tam > TABLERO_TAMAÑO - 1:
   return False
  return all(tablero[fila + i][columna] == AGUA for i in range(tam))

# Definimos la función que coloca nuestro barco
def colocar_barco(tablero, fila, columna, tam, direccion):
 if direccion == "horizontal":
  for i in range(tam):
   tablero[fila][columna + i] = BARCO
 elif direccion == "vertical":
  for i in range(tam):
   tablero[fila + i][columna] = BARCO

# Definimos la función para poder disparar a los barcos
def disparar(tablero, fila, columna):
 if tablero[fila][columna] == BARCO:
  tablero[fila][columna] = HUNDIDO
  return True
 elif tablero[fila][columna] == AGUA:
  tablero[fila][columna] = FALLO
  return False

# Generamos nuestra función principal (motor de nuestra aplicación)
def hundir_la_flota():
 tablero = crear_tablero()
 colocar_barcos(tablero)
 while True:
  imprimir_tablero(tablero)
  try:
   fila = int(input("Ingresa la fila para disparar: "))
   columna = int(input("Ingresa la columna para disparar: "))
   if fila < 0 or fila >= TABLERO_TAMAÑO or columna < 0 or columna >= TABLERO_TAMAÑO:
    print(" ¡Posición fuera del tablero, vuelve a intentarlo! ")
   
   if disparar(tablero, fila, columna):
    print("¡Barco golpeado!")
   else:
    print("¡Disparo al agua!")
   if all(all(casilla != BARCO for casilla in fila) for fila in tablero):
    imprimir_tablero(tablero, ocultar_barcos=False)
    print("¡Has hundido la flota!")
    break
  
  except ValueError:
   print("Entrada inválida, ingresa un número.")

if __name__ == "__main__":
 hundir_la_flota()