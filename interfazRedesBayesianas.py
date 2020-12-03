from tkinter import *
from tkinter import messagebox
import networkx as nx
from matplotlib import pyplot as plt
g1 = nx.DiGraph()
import csv
from string import ascii_uppercase as MAYUS


def on_closing():
    if messagebox.askokcancel("Salir", "Estas seguro?"):
        root.destroy()
    
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

    
class Window:       
    def __init__(self, master):     
        self.filename=""
        self.frLeerArchivo = LabelFrame(master, text="Leer Archivo")
        self.frLeerArchivo.grid(row=0,column=0, columnspan=2)
        self.frIniciar = LabelFrame(master, text="Iniciar Programa")
        self.frIniciar.grid(row=0,column=2, columnspan=2)
        self.frTrazas = LabelFrame(master, text="Trazas")
        self.frTrazas.grid(row=1,column=0, columnspan=2)
        self.frDescripcion = LabelFrame(master, text="Descripcion")
        self.frDescripcion.grid(row=1,column=2)
        self.frImagen = LabelFrame(master, text="Grafo")
        self.frImagen.grid(row=2,column=0, columnspan=2, rowspan=2)
        self.frInfor = LabelFrame(master, text="Informacion")
        self.frInfor.grid(row=1,column=3, columnspan=2)
        self.frInfor2 = LabelFrame(master, text="Probabilidades")
        self.frInfor2.grid(row=2,column=2, columnspan=2, rowspan=2)
        

        #Buttons
        self.btleerArchivo=Button(self.frLeerArchivo, text="Leer Archivo", command=self.leerA).grid(row=0,column=0)
        self.lbArchivoSelecc=Label(self.frLeerArchivo, text=self.filename).grid(row=0,column=1)
        self.btIniciar=Button(self.frIniciar, text="Iniciar", command=self.iniciar).pack()


##        self.lbTrazas = Entry(self.frTrazas, textvariable=self.filename, state='readonly')
##        self.myscroll = Scrollbar(self.frTrazas, orient='vertical', command=self.lbTrazas.yview)
##        self.lbTrazas.config(yscrollcommand=self.myscroll.set)
##        self.lbTrazas.grid(row=0, column=0, sticky='ew')
##        self.myscroll.grid(row=0, column=1, sticky='ew')
        
        #self.lbTrazas=Label(self.frTrazas, text=self.filename).grid()
        self.ST = Scrollbar(self.frTrazas)
        self.T = Text(self.frTrazas, height=15, width=50)
        #self.ST.pack(side=RIGHT, fill=Y)
        #self.T.pack(side=LEFT, fill=Y)
        self.ST.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.ST.set)
        #quote = ""
        #self.T.insert(END, quote)


        self.lbDescripcion=Label(self.frDescripcion, text=self.filename).grid(row=0,sticky=W)
        self.lbIGrafo=Label(self.frImagen, text=self.filename)
        self.lbInfo1=Label(self.frInfor, text=self.filename).grid(row=0,sticky=W)
        self.lbInfo2=Label(self.frInfor2, text=self.filename).grid(row=0,sticky=W)
      


    def leerA(self):
        from tkinter.filedialog import askopenfilename
        self.filename=""
        Tk().withdraw() 
        self.filename = askopenfilename()

        self.lbArchivoSelecc=Label(self.frLeerArchivo, text=self.filename).grid(row=0,column=1)

    def iniciar(self):
        #print(self.filename)
        #self.lbTrazas=Label(self.frTrazas, text=self.filename).pack()
        #definir nombre del archivo de entrada y salida
        nombre_archivo_entrada = self.filename
        nombre_archivo_salida = "trazasconvertido.csv"
        
        #mandamos a leer el archivo y lo almacenamos en la lista
        lista = leerarchivo(nombre_archivo_entrada)

        #convertimos la bitácora con nombres de actividades en 
        #actividades identificadas por letras del alfabeto como IDS
        identificadores, bitacora = trazasID(lista)

        txtDescripcion=""
        #solo mostramos los valores unicos encontrados y los valores de ID asignados
        for key in identificadores:
            txtDescripcion = txtDescripcion + identificadores[key] + " - " + key + "\n"
            #print("A la actividad:",key,"--- Se le asignó:" ,identificadores[key])
            #print(identificadores[key]," - ",key)
        self.lbDescripcion=Label(self.frDescripcion, text=txtDescripcion, justify=LEFT, padx = 10).grid(row=0,sticky=W)

        #mostramos la bitácora nueva, unicamente con IDS
        txtTrazas=""
        tmin=9999
        tmax=0
        suma=0
        tpromedio=0
        #print("Bitácora de eventos")
        for x in bitacora:
            if len(x)< tmin:
                tmin=len(x)
            if len(x)> tmax:
                tmax=len(x)
##                if len(x)>180:
##                    print(x)
            suma=suma+len(x)
            
            txtTrazas=txtTrazas + str(x) +"\n"
            #print(x)
        tpromedio=suma/len(bitacora)

        txtinfo="Num. Total: "+str(len(bitacora))+"\nTam. Minimo: "+str(tmin)+"\nTam. Maximo: "+str(tmax)+"\nTam. Promedio: "+str(round(tpromedio, 2))
        self.lbInfo1=Label(self.frInfor,text=txtinfo, justify=LEFT, padx = 10).grid(row=0,sticky=W)
        
        self.ST = Scrollbar(self.frTrazas)
        self.T = Text(self.frTrazas, height=15, width=80)
        self.ST.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.ST.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.ST.set)
        self.T.insert(END, txtTrazas)

        #creamos el archivo de texto con letras del alfabeto como IDS 
        escribearchivo(bitacora, nombre_archivo_salida)
        #Leer archivo trazasconvertido.csv, tiene que estar en la misma carpeta
        ar = open ('trazasconvertido.csv', 'r')
        #Guarda cada linea del archivo como un elemento de una lista
        lineas = ar.readlines()
        #print("Cantidad de lineas del archivo "+str(len(lineas)))
        ori=""
        des=""
        nodos= set()
        #Generar lista ordenada de todos los nodos para matriz
        for x in lineas:
            x=x.replace(" ", "")
            #print(x[:-1])
            for i in x[:-2].split(","):
                nodos.add(i)
                g1.add_node(i)

        lnodos = list(nodos)
        lnodos.sort()

        #print(len(lnodos))
                    
        for x in lineas:
            x=x.replace(" ", "")
            x=x.replace(",", "")

            for i in range(1,len(x[:-1]),1):
                #valida que el destino no sea un padre ya existente
                if x[i] in nx.ancestors(g1,x[i-1]):
                    hola=1
                    #print("Se genera un ciclo con "+str(x[i-1]+"->"+str(x[i])))
                #Si no existe significa que ese camino no causa ciclos
                else:
                    g1.add_edge(x[i-1],x[i])



        #Matriz de adjacencia
        ma = list()
        for x in lnodos:
            la = list()
            vecinos =list(g1.adj[x])
            for y in lnodos:
                if y in vecinos:
                    la.append(1)
                else:
                    la.append(0)
            ma.append(la)

##        for x in ma:
##            print(x)


        #Probabilidades de Nodos
        pnp= list()
        for i in lnodos:
            pro=list()
            pro.append(i)
            aux=0
            for j in lnodos:
                cont=0
                for k in lineas:
                    buscar=str(i)+","+str(j)
                    if k.find(buscar)>=0:
                        cont +=1
                aux =(cont/len(lineas))
                pro.append(round(aux,2))
            pnp.append(pro)
##        print("HOla")
        matrizProbabilidad="\\\t"
        
##        print("\\", end = '\t')
        for x in lnodos:
            matrizProbabilidad=matrizProbabilidad+str(x)+"\t"
##            print(x, end = '\t')
        for x in pnp:
            matrizProbabilidad=matrizProbabilidad+"\n"
##            print()
            for y in x:
                matrizProbabilidad=matrizProbabilidad+str(y)+"\t"
##                print(y, end = '\t')
        matrizProbabilidad=matrizProbabilidad+"\n"

        self.lbInfo2=Label(self.frInfor2, text=matrizProbabilidad).grid(row=0,sticky=W)
        
        for x in lnodos:
            pa=list(g1.predecessors(x))
            pro=list()
            #Nodos Padre
            if len(pa)==0:
                pro.append(x)
                cont=0
                for y in lineas:
                    if y.find(x)>=0:
                        cont +=1
                pro.append(cont/len(lineas))
                pnp.append(pro)
            else:
            #Nodos Hijos
                pro.append(x)
                aux=0
                for y in pa:
                    cont=0
                    for z in lineas:
                        buscar=str(y)+","+str(x)
                        if z.find(buscar)>=0:
                            cont +=1
                    aux =aux+(cont/len(lineas))
                pro.append(aux)
                pnp.append(pro)

##        for x in pnp:
##            print(x)


        plt.tight_layout()
        nx.draw_networkx(g1, arrows=True)
        #plt.show()
        plt.savefig("g1.png", format="PNG")
        plt.clf()
        #img = Image.open('g1.png')
        self.tkimage = PhotoImage(file="g1.png")
        self.lbIGrafo = Label(self.frImagen,image=self.tkimage)
        self.lbIGrafo.pack()
        


root = Tk()
root.title('Trazas')

window=Window(root)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()  
