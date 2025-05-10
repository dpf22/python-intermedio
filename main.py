#start: metodos de los strings
# ##Mayusculas
# word = "Porgrama en python 3"
# word_upper = word.upper()
# print(word,'\n',word_upper)

##NOtacion de titulo
# word = "Porgrama en python 3"
# word_title=word.title()
# print(word_title)

##reemplazo
# word = "programa en python 3"
# word_new = word.replace(" ","_")
#print(word+'\n'+word_new)

##3limincion de espacios
# word = "    Programa En Python 3    "
# word_lstrip = word.lstrip()
# print('"' + word_lstrip + '"') # Imprimirá "Programa En Python 3    "

# word = "    Programa En Python 3    "
# word_rstrip = word.rstrip()
# print('"' + word_rstrip + '"') # Imprimirá "    Programa En Python 3"

# word = "    Programa En Python 3    "
# word_strip = word.strip()
# print('"' + word_strip + '"') # Imprimirá "Programa En Python 3"

# ##separador
# word = "programa en python 3"
# word_split = word.split()
# print(word_split)
# email = "example@gmail.com"
# email_split=email.split('@')
# print(email_split)


'''
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
'''




# #end metodos de los strings

#start: estrcutura de Datos

##listas:

#los indices comienzan desde 0

# frutas=["🍎","🍒","🍍"]
# frutas_vacias=list()
# print(frutas)
# print(frutas_vacias)

# ##slicing (rebanadas)
# #sintaxis: lista[dig_inicio:dig_fin-1:dig_paso]
# frutas=["🍎","🍒","🍍"]
# #obtener una sublist sin el primer ni ultimo digito
# print(frutas[1:-1])
# # Obtener el primer elemento
# print(frutas[0])  #

# # Obtener el segundo elemento
# print(frutas[1])  #

# # Obtener los dos primeros elementos
# print(frutas[:2])  # ["", ""]

# # Obtener el último elemento
# print(frutas[-1])  #

# # Obtener los dos últimos elementos
# print(frutas[-2:])  # ["", ""]

# # Obtener la lista invertida
# print(frutas[::-1])  # ["", "", ""]

# # Extraer elementos saltando de 2 en 2
# print(frutas[::2])  # ["", ""]

# # Obtener una sublista sin el primer ni último elemento
# print(frutas[1:-1])  # [""]

# # Intentar acceder más allá del rango (no genera error)
# print(frutas[:10])  # ["", "", ""]

# El slicing también funciona perfectamente con cadenas de texto, ya que en Python las cadenas son secuencias de caracteres. Aquí tienes un ejemplo rápido:
# texto = "Python"

# # Obtener los primeros tres caracteres
# print(texto[:3])  # "Pyt"

# # Obtener los últimos tres caracteres
# print(texto[-3:])  # "hon"

# # Invertir la cadena
# print(texto[::-1])  # "nohtyP"
# print(texto[::-2])  # "



##listas 
####acceder y modificar elemntos
# frutas=["🍎","🍒","🍍"]
# print(frutas)
# frutas[1]="🍋‍🟩"
# print(frutas)

### agregar y eliminar

# frutas=["🍎","🍒","🍍","🍐","🍑","🍅","🫐"]
# print(frutas)
# frutas.append("🍍")
# print(frutas)
# frutas.insert(0,"🫐")
# print(frutas)
# frutas.remove("🫐")
# print(frutas)
# frutas.pop()
# print(frutas)

####ordenar y reordenar

# numeros=[3,4,2,5,7,2,7]
# print(numeros)
# numeros.sort()
# print(numeros)
# numeros.reverse()
# print(numeros)

# #iterar
# frutas=["🍎","🍒","🍍"]
# for fruta in frutas:
#     print(fruta)

###List comprehension
# frutas=["manzana","banana","cereza"]
# #sin list comprehension
# frutas_mayus = []
# for fruta in frutas:
#     frutas_mayus.append(fruta.upper())
# print(frutas_mayus)
# #con list comprehension
# frutas_mayus=[fruta.upper() for fruta in frutas]
# print(frutas_mayus)


############################# EJERCICIOS 1
'''
Ejercicios 1: Define una lista con 5 números y cambia el tercer elemento.
·       Ejercicio2: Dada la lista [4, 7, 2, 9, 1], ordénala de menor a mayor y luego invierte su orden.
·       Ejercicio 3: Con la lista ["a", "b", "c", "d", "e"], obtén la sublista ["c", "d", "e"] usando slicing.
'''

#Ejercicio 1

# nums=[1,2,3,4,5]
# nums[2]=7
# print(nums)

# #ejericcio 2

# nums=[4, 7, 2, 9, 1,"abc", "df", "aa"]
# nums.sort() #tambien sirve en listas de letras, se arreglan de manera allfabetica
# print(nums)
# nums.reverse()
# print(nums)
# O también:
# lista = [4, 7, 2, 9, 1]
# lista_ordenada_invertida = sorted(lista)[::-1]
# print(lista_ordenada_invertida)  # [9, 7, 4, 2, 1]

# #### ejerciico 3
# letras=["a", "b", "c", "d", "e"]
# print(letras[-3:])

# ##Tuplas

# coordenadas=(10,20)
# print(coordenadas)

## desempaquetado
# coordenadas=(10,20)
# x,y = coordenadas
# print(x,coordenadas)

# #encontrar y acceder por el indice
# frutas=["🍎","🍒","🍍"]
# cereza_index=frutas.index("🍒")
# print(cereza_index,frutas[cereza_index])

###########3convertir tupla a lista y lista a tupla

# coordenadas = (10,20)
# lista_coordenadas=list(coordenadas)
# print(lista_coordenadas)
# tupla=tuple(lista_coordenadas)
# print(tupla)

'''
Ejercicio 1: Crea una tupla con tres frutas y muestra la segunda fruta usando índice.
Ejercicio 2: Dada la tupla punto = (7, 3), extrae sus coordenadas a dos variables y súmalas.
Ejercicio 3: Convierte la lista ['a', 'b', 'c'] en tupla, e intenta agregar un elemento nuevo (observa qué sucede).

'''
#####ejercicio 1

# frutas=("🍎","🍒","🍍")
# print(frutas[1])

###ejercicio 2
# coordenadas=(7,3)
# x,y=coordenadas
# print(x + y)

# #ejercicio 3
# nums=['a', 'b', 'c']
# tuplanums=tuple(nums)
# tuple.append("s")

#Diccionarios
# alumno = {"nombre":"Luis", "curso":"python","nota":8.5}
# print(alumno)

#qcceder y modificar
# alumno = {"nombre":"Luis", "curso":"python","nota":8.5}
# print(alumno["curso"])
# print(alumno["nombre"])
# print(alumno["nota"])
# alumno["nota"]=9
# print(alumno)

# #Añadir y eliminar pares
# alumno = {"nombre":"Luis", "curso":"python","nota":8.5}
# alumno["edad"]=20
# print(alumno)
# valor=alumno.pop("curso")
# print(valor)
# print(alumno)

###iterar
# alumno={"nombre":"Luis", "curso":"python","nota":8.5}
# # print(alumno.keys())
# # print(alumno.values())
# # print(alumno.items())

# for clave in alumno.keys():
#     print(clave)
# for clave in alumno.values():
#     print(clave)
# for clave,valor in alumno.items():
#     print(clave,valor)


##### manejo seguro
# alumno={"nombre":"Luis", "curso":"python","nota":8.5}
# # ciudad = ["ciudad"]
# ciudad=alumno.get("nombre","desconocido")
# print(ciudad)
# print(alumno)

## operador in
#en listas y tuplas

# frutas=["manzana","banana","pera"]
# print("banana" in frutas) #true

# #en cadenas de texto
# texto="Hola como estas"
# print("como" in texto)

# #En diccionarios (verifica si una clave existe)
# edades={"juan":45,"Maria":48}
# print("Maria" in edades) #True
# print("Laura" in edades) #false

####Dict comprehension
#ejemplo 1: crear un diccionario a partir de una lista. "cada nuero de la lista se convierte en una clave, y su cuadrado es el valor"
# numeros=[1,2,3,4]
# cuadrados={num: num**2 for num in numeros}
# print(cuadrados)

#ejemplos 2:

#transformar valores

####sets (conjuntos)

# letras={"a","b","c"}
# ### agregar y eliminar
# letras.add("p")
# print(letras)
# letras.remove("c")
# print(letras)
# letras.discard("z")

## unir e intersectar sets

# pares={2,4,6}
# impares = {1,3,4,5}
# todos = pares | impares #union: {1,2,3,4,5,6}
# print(todos)
# comunes = pares & {2,3,4} ### inteerrseccion = {2,4}
# print(comunes)
# diff = pares - impares   #### diferencia -: {2,6}
# print(diff)

# #Eliminar duplicados
# numeros=[1,2,2,3,4,5,5]
# unicos= set(numeros)
# print(numeros,unicos)


# #ietrar (recorrer)
# numeros = {2,5,7,8}
# for n in numeros:
#     print(n)

'''
Ejercicio 1: Representa una lista de contactos donde la clave sea el nombre y el valor el número de teléfono.
·       Ejercicio 2: Dado el diccionario inventario = {"manzanas": 10, "naranjas": 5}, incrementa el valor de "manzanas" en 20%.
·       Ejercicio 3: Elimina un elemento con pop() y luego verifica si la clave aún existe usando in.

'''
# #ejercicio1
# contactos={
#     "Nombre: ": 123456789

# }
# print(contactos)

# #ejericcio 2:

# inventario = {"manzanas": 10, "naranjas": 5}
# print(inventario)
# inventario["manzanas"]=12
# print(inventario)

# Ejercicio 2: Dado el diccionario inventario = {"manzanas": 10, "naranjas": 5}, incrementa el valor de "manzanas" en 20%.
# inventario = {"manzanas": 10, "naranjas": 5}
# inventario["manzanas"] = int(inventario["manzanas"] * 1.2)  # Incremento del 20%
# print(inventario)  # {'manzanas': 12, 'naranjas': 5}
# #ejercicio 3


# inventario = {"manzanas": 10, "naranjas": 5, "peras: ": 8}
# print(inventario)
# inventario.pop("naranjas")
# print(inventario)
# if 5 in inventario:
#     print("hola")

# Ejercicio 3: Elimina un elemento con pop() y luego verifica si la clave aún existe usando in.
# productos = {"leche": 2, "pan": 5, "huevos": 12}
# eliminado = productos.pop("pan")  # Eliminamos "pan"
# print(f'Elemento eliminado: {eliminado}')  # 5
# Verificamos si la clave aún existe
# print("pan" in productos)  # False

# '''

# Ejercicio 1: Crea un set con los números del 1 al 5, elimina el 3 y añade el 10.
# •	Ejercicio 2: Dados A = {1,2,3} y B = {3,4}, calcula A∪B, A∩B y B−A.
# •	Ejercicio 3: A partir de la lista ['a','b','a','c','b','d'], genera un set para quedarse solo con los elementos únicos.

#ejericcio 1
# numeros={1,2,3,4,5}
# print(numeros)
# numeros.remove(3)
# numeros.add(10)
# print(numeros)

# #ejercicio 2
# A = {1,2,3} 
# B = {3,4}

# print(A.union(B))
# print(A.intersection(B))
# print(B.difference(A))

#ejericcio 3

# lista = ['a','b','a','c','b','d']
# unicos=set(lista)
# print(unicos)
# # # #emd:estrcutura de datos

# Start: Funciones 
# def saludar(nombre):
#     """imprimir un saludo personalizado"""
#     print(f"Hola, {nombre}")

# saludar("felipe") #argumentos poscionales
# saludar(nombre="pedro") #argumentos con nombre(keyword).

##Definicion de una funcion con docstrings mas detallados
# def saludar(nombre):
'''Muestra un mensaje de saludo personalizado

    Paramters:
    nombre(str): el nombre de la persona a saludar
    Returns: none : solo imprime el saludo en pantalla
##https://peps.python.org/pep-0257/
'''
# def calculo(a,b,c):
#     '''Es para hacer un calculo'''
#     return (a+b) * c

# print(calculo(b=2,c=4,a=3))

# #funcion sin retorno
# def sin_retorno():
#     a = 5+3

# print(sin_retorno())####

####resultado = sin_retorno()
# print(f"la funcion sin retorno devuelve: {resultado}"")


##parametros con valores por defecto
#def potencia(base, exponente=2):
#   return=base**exponente

#print(ptencia(base=5))
#(print(potencia(5,3)))


#diferencie entre print y return: print solo muestra cosas, return devuelve las cosas
#end fucniones