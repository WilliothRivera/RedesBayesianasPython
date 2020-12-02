import csv
from string import ascii_uppercase as MAYUS
import networkx as nx
from matplotlib import pyplot as plt

def leerarchivo(archivo):
    lista = []
    #Leemos los valores de la lista y los almacenamos en la lista
    with open(archivo) as data:
        entrada = csv.reader(data)
        lista = list(entrada)
    return lista

def trazasID(lista):
    #identificadores servirá para almacenar los valores únicos de los datos de entrada
    identificadores = []
    #la lista traza nos será de ayuda para darle el formato correcto a la lista de bitacoras
    traza = []
    #la lista de bitacora almacenará las bitacora unicamente con los identificadores en letras
    bitacora = []
    #el diccionario IDS nos servirá para intercambiar los valores de identificadores
    #con las letras del abecedario
    IDS = {}

    #Iteramos sobre los valores de la lista palabra por palabra, si encontramos
    #una nueva ocurrencia de palabra, lo añadimos a la lista identificadores
    for linea in lista:
        for palabra in linea:
            if palabra not in identificadores:
                identificadores.append(palabra)

    #llenamos nuestro diccionario de IDS, iteramos en la lista de identificadores
    #que contiene valores unicos de ocurrencias, y los vamos añadiendo en el diccionario
    #MAYUS contiene las letras mayúsculas del alfabeto, y se importa al inicio
    #en el diccionario IDS, añadimos el nombre de la actividad a KEY
    #y el identificador de la actividad (letra del abecedario) a VALUE
    for x in range(0, len(identificadores)):
        IDS[identificadores[x]] = (MAYUS[x])

    #Recorremos nuestra lista inicial, comparando cada palabra con el valor en diccionario
    #cuando haya una coincidencia de nombre de la actividad con la KEY del diccionario
    #se agrega el VALUE del diccionario (letra del abecedario) a nuestra lista de trazas
    for linea in lista:
        for palabra in linea:
            for key in IDS:
                if palabra == key:
                    #agregamos la letra del abecedario a la traza
                    traza.append(IDS[key])
        #agregamos la traza a la bitacora
        bitacora.append(traza)
        #limpiamos la traza para la siguiente iteración
        traza=[]

    return IDS, bitacora

def escribearchivo(bitacora, nombre_archivo_salida):
    f = open(nombre_archivo_salida,'a')
    for linea in bitacora:
            for palabra in linea:
                f.write(palabra + ",")
            f.write("\n")
    f.close()

def unique(list1):
    # iniciamos la lista vacia 
    unique_list = []   
    # iteramos por la lista de entrada 
    for x in list1: 
        # revisamos si existe o no un numero 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

def bayes(nombre_archivo_salida):
    f = open(nombre_archivo_salida , "r")
    f1 = f.readlines()
    matriz = []
    array = []
    graph = nx.DiGraph()

    #Leemos los datos del archivo txt excluyendo las comas y saltos de linea
    #y agregamos los nodos en el grafo
    for x in f1:
        for j in x:
            i = 1
            while j != ",":
                while j != "\n":
                    array.append(j)
                    graph.add_node(j)
                    break
                break
        matriz.append(array)
        array=[]
    print("arreglo de valores leidos")
    print(len(matriz))
    print()
    #Repasamos la matriz, y almacenamos en las variables v1 y v2 los arcos
    #para después revisar si se genera un ciclo, si no, se agrega el arco
    #en nuestro grafo
    ciclos = 0
    print("-------------------------------------------------------------------------------")
    for x in range(len(matriz)):
        for j in range(len(matriz[x])-1):
            v1=matriz[x][j]
            v2=matriz[x][j+1]
            if v2 in nx.ancestors(graph,v1):
                print("Se genera un ciclo con el arco del nodo:", v1,"al nodo", v2)
                ciclos += 1
            #Si no existe significa que ese camino no causa ciclos
            else:
                graph.add_edge(v1,v2)
    print()
    print("Se detectaron", ciclos, "ciclos")
    print("-------------------------------------------------------------------------------")
    print()


    #almacenamos los datos en un arreglo para poder hacer uso de
    #la funcion que retorna valores unicos del arreglo
    aux =[]
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            aux.append(matriz[x][y])

    #Obtenemos valores unicos del arreglo llamando para el proceso del cálculo de probabilidades
    vertices =unique(aux)
    print("Los vertices del grafo son: ", vertices)
    print()

    #Calculamos la probabilidad de los nodos padre, unicamente trabajando los primeros
    #valores de la matriz
    print("Probabilidad de los nodos raíz")
    dim = len(matriz)
    nodosraiz = []
    for x in range(0,dim):
        nodosraiz.append(matriz[x][0])
    unicosraiz = unique(nodosraiz)
    for x in unicosraiz:
        print("Probabilidad de que ocurra nodo", x, "=",nodosraiz.count(x)/dim,"--Probabilidad de que no ocurra = ",1- nodosraiz.count(x)/dim)

    #Calculamos la probabilidad de los nodos hijo, trabajando con el resto de nodos que no son considerados
    #como nodos iniciales
    print()
    print("Probabilidad de los nodos hijos")
    for x in vertices:
        prob = list(graph.predecessors(x))
        if prob != 0:
            cont = 0
            for y in prob:
                for i in f1:
                    if i.find((y)+","+(x))>=0:
                        cont +=1
            if cont/len(f1)!=0:
                print("Probabilidad del nodo",x,"=", cont/len(f1) ,"--Probabilidad de que no ocurra = ",1-cont/len(f1))

    #Representación gráfica del grafo
    plt.tight_layout()
    nx.draw_networkx(graph, arrows=True)
    plt.show()
    plt.clf()

def main():
    #el archivo de entrada debe estar con formato de csv (columnas separadas por comas, y lineas separadas por saltos)
    #no importa la extension del archivo, probado con .csv y ,txt
    
    #definir nombre del archivo de entrada y salida
    nombre_archivo_entrada = "trazas.txt"
    nombre_archivo_salida = "trazasconvertido.csv"

    #mandamos a leer el archivo y lo almacenamos en la lista
    lista = leerarchivo(nombre_archivo_entrada)

    #convertimos la bitácora con nombres de actividades en 
    #actividades identificadas por letras del alfabeto como IDS
    identificadores, bitacora = trazasID(lista)

    #solo mostramos los valores unicos encontrados y los valores de ID asignados
    print("Se identificaron las siguientes actividades:")
    for key in identificadores:
        print("A la actividad:",key,"--- Se le asignó:" ,identificadores[key])
    print()

    #mostramos la bitácora nueva, unicamente con IDS
    print("Bitácora de eventos")
    for x in bitacora:
        print(x)

    #creamos el archivo de texto con letras del alfabeto como IDS 
    escribearchivo(bitacora, nombre_archivo_salida)

    bayes(nombre_archivo_salida)

main()
