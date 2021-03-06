from flask import Flask, request, Response
from graphviz import Digraph
import base64
import threading
import time
import sys
import simplejson as json
import qrcode
import datetime
from threading import Timer
from Binario import ArbolBinario
import math
from Dispersa import MatrizDispersa
from ArbolB import ArbolB
from ArbolAVL import AVL
from Hash import Hash
app = Flask("Proyecto")

def numval(letra):
    numero = ord(letra.lower()) - 96
    #print(str(numero))
    return str(numero)

def sumar(x,y):
    c = ord(x.upper())
    n = c + y
    return str(chr(n))

def restar(x,y):
    c = ord(x.upper())
    n = c - y
    return str(chr(n))

class nave(object):
    def __init__(self,casillas=0):
        self.casillas=casillas
    def contar(self):
        self.casillas-=1
        if self.casillas == 0:
            return 'eliminado'
        elif self.casillas > 0:
            return 'golpe'
        else:
            return 'error'

class juego(object):
    def __init__(self,naves=0,tipo_disparo=None,x=0,y=0,variante=None):
        self.tipo_disparo=tipo_disparo
        self.x=x
        self.y=y
        self.variante=variante
        self.tiempo=0

        self.jugador1=None
        self.cuboinicial1=Cubo() #cuboinicial
        self.cubo1=Cubo() # cubo que sirve como estado actual
        self.acertados1 = Cubo() # acertados
        self.fallados1 = Cubo() #fallados
        self.cubodisparos1 = Cubo() # contiene los disparos del adversario?

        self.jugador2=None
        self.cubo2=Cubo()
        self.acertados2 = Cubo()
        self.fallados2 = Cubo()
        self.cubodisparos2 = Cubo()
        self.cuboinicial2=Cubo()

        self.tirosa1=0
        self.tirosa2=0
        self.tirosf1=0
        self.tirosf2=0
        self.actuales=0
        self.turno=None
        self.numerodisparos=0
        self.disparos=0
        self.historial=ArbolB()
    def cambiarturno(self):
        if self.variante == 2:
            self.actuales += 1
            #print(str(self.actuales) + ' ' + str(self.numerodisparos))
            #print(repr(self.actuales))
            #print(repr(self.numerodisparos))
            if self.actuales == self.numerodisparos:
                print('entro aca')
                if self.jugador1.upper() == self.turno.upper():
                    self.turno = self.jugador2
                    print('Turno de: ' + self.jugador2)
                elif self.jugador2.upper() == self.turno.upper():
                    self.turno = self.jugador1
                    print('Turno de: ' + self.jugador1)
                else:
                    print('Error')
                self.actuales = 0
        else:
            if self.jugador1.upper() == self.turno.upper():
                self.turno = self.jugador2
                print('Turno de: ' + self.jugador2)
            elif self.jugador2.upper() == self.turno.upper():
                self.turno = self.jugador1
                print('Turno de: ' + self.jugador1)
            else:
                print('Error')

class Barco(nave):
    def __init__(self,modo=None,direccion=None):
        self.tipo='barco'
        self.modo=modo
        self.direccion=direccion
        if modo == 1:
            self.casillas = 1
        elif modo == 2:
            self.casillas = 2
        elif modo == 3:
            self.casillas = 3
    def colocar(self,matriz,x,y):
        if self.modo == 1:
            matriz.insertar(x,y,self)
        elif self.modo == 2:
            if self.direccion == 1:
                matriz.insertar(x,y,self)
                matriz.insertar(sumar(x,1),y,self)
            else:
                matriz.insertar(x,y,self)
                matriz.insertar(x,(y+1),self)
        elif self.modo == 3:
            if self.direccion == 1:
                matriz.insertar(x,y,self)
                matriz.insertar(sumar(x,1),y,self)
                matriz.insertar(sumar(x,2),y,self)
            else:
                matriz.insertar(x,y,self)
                matriz.insertar(x,(y+1),self)
                matriz.insertar(x,(y+2),self)

class Avion(nave):
    def __init__(self,modo=None):
        self.tipo='avion'
        self.modo=modo
        if modo == 1:
            self.casillas = 4
        elif modo == 2:
            self.casillas = 6
    def colocar(self,matriz,x,y):
        if self.modo == 1:
            matriz.insertar(x,y,self)
            matriz.insertar(sumar(x,1),y,self)
            matriz.insertar(restar(x,1),y,self)
            matriz.insertar(x,y+1,self)
        elif self.modo == 2:
            matriz.insertar(x,y-1,self)
            matriz.insertar(x,y,self)
            matriz.insertar(sumar(x,1),y,self)
            matriz.insertar(restar(x,1),y,self)
            matriz.insertar(x,y+1,self)
            matriz.insertar(x,y+2,self)
             #colocar aviones

class Submarino(nave):
    def __init__(self,modo,direccion):
        self.tipo='submarino'
        self.modo=modo
        self.direccion = direccion
        if modo == 1:
            self.casillas = 1
        elif modo == 2:
            self.casillas = 2
        elif modo == 3:
            self.casillas = 3
    def colocar(self,matriz,x,y):
        if self.modo == 1:
            matriz.insertar(x,y,self)
        elif self.modo == 2:
            if self.direccion == 1:
                matriz.insertar(x,y,self)
                matriz.insertar(sumar(x,1),y,self)
            else:
                matriz.insertar(x,y,self)
                matriz.insertar(x,(y+1),self)
        elif self.modo == 3:
            if self.direccion == 1:
                matriz.insertar(x,y,self)
                matriz.insertar(sumar(x,1),y,self)
                matriz.insertar(sumar(x,2),y,self)
            else:
                matriz.insertar(x,y,self)
                matriz.insertar(x,(y+1),self)
                matriz.insertar(x,(y+2),self)

class Satelite(nave):
    def __init__(self,x=0,y=0):
        self.tipo='satelite'
        self.x=x
        self.y=y
        self.casillas=1
    def colocar(self,matriz,x,y):
        matriz.insertar(x,y,self)

class Usuario(object):
    def __init__(self,nombre=None,contrasena=None,conectado=None):
        self.nombre=nombre
        self.contrasena=contrasena
        self.conectado=conectado
        self.lista = ListaDoble()
        #self.cubo = Cubo()
        #self.acertados = Cubo()
        #self.fallados = Cubo()
        self.ganadas = 0
        self.contactos = AVL()
    def __lt__(self,other):
        return (self.nombre.upper() < other.nombre.upper())
    def __eq__(self,other):
        return(self.nombre.upper() == other.nombre.upper())
    def __gt__(self,other):
        return(self.nombre.upper() > other.nombre.upper())
    def __str__(self):
        return self.nombre
    def __repr__(self):
        return (self.nombre + ' ' + str(self.lista))

class Cubo(object):
    def __init__(self):
        self.submarinos = MatrizDispersa()
        self.barcos = MatrizDispersa()
        self.aviones = MatrizDispersa()
        self.satelites = MatrizDispersa()
    def colocar(self,nivel,columna,fila):
        if nivel == 1:
            self.satelites.insertar(columna,fila)
        elif nivel == 2:
            self.aviones.insertar(columna,fila)
        elif nivel == 3:
            self.barcos.insertar(columna,fila)
        elif nivel == 4:
            self.submarinos.insertar(columna,fila)


class partida(object):
    contador=0
    def __init__(self,oponente=None,tiros=0,acertados=0,fallados=0,resultado=None,danio=0):
        self.oponente=oponente
        self.tiros=tiros
        self.acertados=acertados
        self.fallados=fallados
        self.resultado=resultado
        self.danio=danio
        self.eliminadas=0
        self.numero= partida.contador
        partida.contador+=1
    def __str__(self):
        if self.resultado == 0:
            res = 'perdida'
        else:
            res = 'ganada'
        cadena = str(self.oponente) + ' ' + str(self.tiros) + ' ' + res
        return cadena
    def json(self):
        data={}
        data['oponente'] = self.oponente
        data['tiros'] = self.tiros
        data['acertados'] = self.acertados
        data['fallados'] = self.fallados
        if self.resultado == 0:
            data['resultado'] = 'perdida'
        else:
            data['resultado'] = 'ganada'
        data['damage'] = self.danio
        json_data = json.dumps(data)
        return json_data
    def __repr__(self):
        return str(self.numero)
    def __lt__(self,other):
        return self.tiros < other.tiros
    def __gt__(self,other):
        return self.tiros > other.tiros

class NodoDoble(object):
    def __init__(self,dato=None):
        self.dato=dato
        self.derecha=None
        self.izquierda=None

class ListaDoble(object):
    def __init__(self,inicio=None):
        self.inicio=inicio
        self.tama=0
    def insertar(self,dato):
        self.tama+=1
        nuevo = NodoDoble(dato)
        nuevo.derecha = self.inicio
        if(self.inicio is not None):
            self.inicio.izquierda = nuevo
        self.inicio = nuevo
    def graficar(self):
        graf = Digraph(comment='ListaDoble')
        nodo = self.inicio
        while nodo.derecha is not None:
            graf.node(str(nodo.dato))
            print(nodo.dato)
            graf.node(str(nodo.derecha.dato))
            graf.edge(str(nodo.dato),str(nodo.derecha.dato))
            graf.edge(str(nodo.derecha.dato),str(nodo.dato))
            nodo = nodo.derecha
        #graf.render('doble.gv',cleanup=True)
        #graf.save('doble',"C:\\Users\\Abraham Jelkmann\\Desktop")
        return graf
    def imprimir(self):
        nodo = self.inicio
        cad=''
        while nodo.derecha is not None:
            cad += str(nodo.dato) +  ','
            #print(nodo.dato)
            nodo = nodo.derecha
        cad+=str(nodo.dato)
        print(cad)
        return cad
    def buscarnumero(self,dato):
        nodo=self.inicio
        encontrada=False
        while not encontrada:
            if nodo.dato.numero == dato:
                encontrada = True
                return nodo.dato.json()
            else:
                if nodo.derecha is not None:
                    nodo = nodo.derecha
                else:
                    return None

    def mostrarnumeros(self):
        nodo = self.inicio
        cad=''
        while nodo.derecha is not None:
            cad += str(nodo.dato.numero) +  ','
            #print(nodo.dato)
            nodo = nodo.derecha
        cad+=str(nodo.dato.numero)
        print(cad)
        return cad
    def insertarfinal(self,dato):
        self.tama+=1
        nuevo = NodoDoble(dato)
        if self.inicio is not None:
            inicial = self.inicio
            while inicial.derecha is not None:
                inicial = inicial.derecha
            inicial.derecha = nuevo
            nuevo.izquierda = inicial
        else:
            self.inicio=nuevo
    def ordenamiento(self):
        inicial = self.inicio
        for x in range(2,self.tama):
            inicial=self.inicio
            while inicial.derecha is not None:
                if inicial.dato > inicial.derecha.dato:
                    aux = inicial.dato
                    inicial.dato = inicial.derecha.dato
                    inicial.derecha.dato = aux
                inicial = inicial.derecha

class Listaconsulta(object):
    def __init__(self,inicio=None):
        self.inicio=inicio
        self.tama=0
    def insertar(self,dato):
        self.tama+=1
        nuevo = NodoDoble(dato)
        nuevo.derecha = self.inicio
        if(self.inicio is not None):
            self.inicio.izquierda = nuevo
        self.inicio = nuevo
    def graficar(self):
        graf = Digraph(comment='ListaDoble')
        nodo = self.inicio
        while nodo.derecha is not None:
            graf.node(str(nodo.dato))
            print(nodo.dato)
            graf.node(str(nodo.derecha.dato))
            graf.edge(str(nodo.dato),str(nodo.derecha.dato))
            graf.edge(str(nodo.derecha.dato),str(nodo.dato))
            nodo = nodo.derecha
        #graf.render('doble.gv',cleanup=True)
        #graf.save('doble',"C:\\Users\\Abraham Jelkmann\\Desktop")
        return graf
    def imprimir(self):
        nodo = self.inicio
        cad=''
        while nodo.derecha is not None:
            cad += str(nodo.dato) +  ','
            #print(nodo.dato)
            nodo = nodo.derecha
        cad+=str(nodo.dato)
        print(cad)
        return cad
    def buscarnumero(self,dato):
        nodo=self.inicio
        encontrada=False
        while not encontrada:
            if nodo.dato.numero == dato:
                encontrada = True
                return nodo.dato.json()
            else:
                if nodo.derecha is not None:
                    nodo = nodo.derecha
                else:
                    return None

    def mostrarnumeros(self):
        nodo = self.inicio
        cad=''
        while nodo.derecha is not None:
            cad += str(nodo.dato.numero) +  ','
            #print(nodo.dato)
            nodo = nodo.derecha
        cad+=str(nodo.dato.numero)
        print(cad)
        return cad
    def insertarfinal(self,dato):
        self.tama+=1
        nuevo = NodoDoble(dato)
        if self.inicio is not None:
            inicial = self.inicio
            while inicial.derecha is not None:
                inicial = inicial.derecha
            inicial.derecha = nuevo
            nuevo.izquierda = inicial
        else:
            self.inicio=nuevo
    def ordenamiento(self):
        inicial = self.inicio
        for x in range(2,self.tama):
            inicial=self.inicio
            while inicial.derecha is not None:
                if inicial.dato.contactos.datos > inicial.derecha.dato.contactos.datos:
                    aux = inicial.dato
                    inicial.dato = inicial.derecha.dato
                    inicial.derecha.dato = aux
                inicial = inicial.derecha

def Reprint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Tempo(object):
    def __init__(self,minutos=0,segundos=0):
        self.segundos = segundos
        self.minutos = minutos
        self.segundostr = 0
        self.minutostr = 0
        self.inicio = 0
        self.final = 0
    def contar(self):
        self.segundostr = self.segundostr + 1
        if self.segundostr == 60:
            self.minutostr == self.minutostr + 1
            self.segundostr == 0
        if self.minutostr == self.minutos:
            if self.segundostr == self.segundos:
                return 1
        return 0

class Contacto(object):
    def __init__(self,nombre,contra):
        self.nombre=nombre
        self.contra=contra
        self.existe='No existe'
    def __str__(self):
        cad = self.nombre + '\\n' + self.contra + '\\n' + self.existe
        return cad
    def __lt__(self,other):
        return self.nombre < other.nombre
    def __gt__(self,other):
        return self.nombre > other.nombre
    def __eq__(self,other):
        return (self.nombre == other.nombre)
    def __ge__(self,other):
        return (self.nombre >= other.nombre)
    def __le__(self,other):
        return self.nombre <= other.nombre

class Disparo(object):
    parametro='x'
    def __init__(self,x='A',y=0,nave=1,tipo=1,resultado=1,emisor='',receptor='',fecha='',numero=0,tiempo=''):
        self.x = x
        self.y = y
        self.nave = nave
        self.tipo = tipo
        self.resultado = resultado
        self.tiponave=''
        self.emisor = emisor
        self.receptor = receptor
        self.fecha = fecha
        self.tiempo = tiempo
        self.numero = numero
        self.parametro=Disparo.parametro
        self.res=''
    def __str__(self):
        if self.parametro == 'x':
            cadena = 'posx: ' + str(self.x) + "\\n" + 'posy: ' + str(self.y) + "\\n" +  'nivel: ' + str(self.nave) + "\\n" +  'tipo: ' + str(self.tipo)
            cadena+= "\\n" + 'res: ' + str(self.res) + "\\n" + 'emisor: ' + str(self.emisor) + "\\n" + 'receptor: ' + str(self.receptor)  + "\\n" + 'fecha: ' + str(self.fecha)
            cadena+=  "\\n" + 'tiempo: ' + str(self.tiempo) + "\\n" + 'numero: ' + str(self.numero)
            return cadena
        if self.parametro == 'y':
            cadena = 'posy: ' + str(self.y) + "\\n" + 'posx: ' + str(self.x) + "\\n" +  'nivel: ' + str(self.nave)  + "\\n" +  'tipo: ' + str(self.tipo)
            cadena+= "\\n" + 'res: ' + str(self.res) + "\\n" + 'emisor: ' + str(self.emisor) + "\\n" + 'receptor: ' + str(self.receptor)  + "\\n" + 'fecha: ' + str(self.fecha)
            cadena+=  "\\n" + 'tiempo: ' + str(self.tiempo) + "\\n" + 'numero: ' + str(self.numero)
            return cadena
        else:
            cadena =  'numero: '   + str(self.numero) + "\\n" + 'posx: ' + str(self.x) + "\\n" + 'posy: ' + str(self.y) + "\\n" +  'nivel: ' + str(self.nave) + "\\n" +  'tipo: ' + str(self.tipo)
            cadena+= "\\n" + 'res: ' + str(self.res) + "\\n" + 'emisor: ' + str(self.emisor) + "\\n" + 'receptor: ' + str(self.receptor)  + "\\n" + 'fecha: ' + str(self.fecha)
            cadena+=  "\\n" + 'tiempo: ' + str(self.tiempo) + "\\n"
            return cadena
    def __lt__(self,other):
        if self.parametro == 'x':
            if self.x != other.x:
                return self.x < other.x
            else:
                return self.numero < other.numero
        elif self.parametro == 'y':
            if self.y != other.y:
                return self.y < other.y
            else:
                return self.numero < other.numero
        else:
            return self.numero < other.numero

    def __gt__(self,other):
        if self.parametro == 'x':
            if self.x != other.x:
                return self.x > other.x
            else:
                return self.numero > other.numero
        elif self.parametro == 'y':
            if self.y != other.y:
                return self.y > other.y
            else:
                return self.numero > other.numero
        else:
            return self.numero > other.numero

    def __eq__(self,other):
        return self.numero == other.numero

    def cambiar(self,x,y):
        print('cambiando a: ' + str(x) + ' ' +str(y))
        self.x=x
        self.y=int(y)


listaconsulta=Listaconsulta()
tem = Tempo()
historial = ArbolB()
ha = Hash(47,60,30)
ar = ArbolBinario()
disparos = ListaDoble()
juegos = ListaDoble()
juegoactual = juego()
ar.insertar(Usuario('chuz','chuz',0))


def tiromasivo(jugador,nivel,posx,posy):
    if jugador == juegoactual.jugador1:
        if True:
            #dis = ar.buscar(ar.raiz,juegoactual.jugador2)
            if nivel == '1':
                nod = juegoactual.cubo2.satelites.buscar(posx,int(posy))
                #print('satelites: ' + posx + " , " +  posy)
                if nod is not None:
                    if not nod.hundido:
                        juegoactual.acertados1.satelites.insertar(posx,int(posy))
                        juegoactual.cubodisparos1.satelites.insertar(posx,int(posy),hundido=True)
                        juegoactual.tirosa1+=1
                        res=nod.nave.contar()
                        disparo(posx,int(posy),1,juegoactual.tipo_disparo,1,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res=res)
                        nod.hundido = True
                        #Agregar código para ráfaga

                        return 'exito'
                    else:
                        return 'nodo ya hundido'
                else:
                    juegoactual.fallados1.satelites.insertar(posx,int(posy))
                    juegoactual.cubodisparos1.satelites.insertar(posx,int(posy))
                    juegoactual.tirosf1+=1
                    disparo(posx,int(posy),1,juegoactual.tipo_disparo,0,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res='fallo')
                    #Agregar código para ráfaga

                    return 'fallo'
            elif nivel == '2':
                nod = juegoactual.cubo2.aviones.buscar(posx,int(posy))
                if nod is not None:
                    if not nod.hundido:
                        res=nod.nave.contar()
                        disparo(posx,int(posy),2,juegoactual.tipo_disparo,1,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res=res)
                        juegoactual.acertados1.aviones.insertar(posx,int(posy))
                        juegoactual.tirosa1+=1
                        juegoactual.cubodisparos1.aviones.insertar(posx,int(posy),hundido=True)
                        nod.hundido = True
                        #ráfaga

                        return 'exito'
                    else:
                        return 'nodo ya hundido'
                else:
                    juegoactual.fallados1.aviones.insertar(posx,int(posy))
                    juegoactual.cubodisparos1.aviones.insertar(posx,int(posy))
                    juegoactual.tirosf1+=1
                    disparo(posx,int(posy),2,juegoactual.tipo_disparo,0,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res='fallo')
                    #ráfaga

                    return 'fallo'
            elif nivel == '3':
                nod = juegoactual.cubo2.barcos.buscar(posx,int(posy))
                if nod is not None:
                    if not nod.hundido:
                        res=nod.nave.contar()
                        disparo(posx,int(posy),3,juegoactual.tipo_disparo,1,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res=res)
                        juegoactual.acertados1.barcos.insertar(posx,int(posy))
                        juegoactual.tirosa1+=1
                        juegoactual.cubodisparos1.barcos.insertar(posx,int(posy),hundido=True)
                        nod.hundido = True

                        return 'exito'
                    else:
                        return 'nodo ya hundido'
                else:
                    disparo(posx,int(posy),3,juegoactual.tipo_disparo,0,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res='fallo')
                    juegoactual.fallados1.barcos.insertar(posx,int(posy))
                    juegoactual.tirosf1+=1
                    juegoactual.cubodisparos1.barcos.insertar(posx,int(posy))

                    return 'fallo'
            elif nivel == '4':
                nod = juegoactual.cubo2.submarinos.buscar(posx,int(posy))
                if nod is not None:
                    if not nod.hundido:
                        res=nod.nave.contar()
                        disparo(posx,int(posy),4,juegoactual.tipo_disparo,1,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res=res)
                        juegoactual.acertados1.submarinos.insertar(posx,int(posy))
                        juegoactual.tirosa1+=1
                        juegoactual.cubodisparos1.submarinos.insertar(posx,int(posy),hundido=True)
                        nod.hundido = True

                        return 'exito'
                    else:
                        return 'nodo ya hundido'
                else:
                    disparo(posx,int(posy),4,juegoactual.tipo_disparo,0,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res='fallo')
                    juegoactual.fallados1.submarinos.insertar(posx,int(posy))
                    juegoactual.tirosf1+=1
                    juegoactual.cubodisparos1.submarinos.insertar(posx,int(posy))

                    return 'fallo'
            else:
                return 'nivel incorrecto'
        else:
            return 'no es el turno del jugador'
    elif jugador == juegoactual.jugador2:
        if True:
            #dis = ar.buscar(ar.raiz,juegoactual.jugador1)
            if nivel == '1':
                nod = juegoactual.cubo1.satelites.buscar(posx,int(posy))
                if nod is not None:
                    if not nod.hundido:
                        res=nod.nave.contar()
                        disparo(posx,int(posy),1,juegoactual.tipo_disparo,1,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res=res)
                        juegoactual.acertados2.satelites.insertar(posx,int(posy))
                        juegoactual.tirosa2+=1
                        juegoactual.cubodisparos2.satelites.insertar(posx,int(posy),hundido=True)
                        nod.hundido = True
                        return 'exito'
                    else:
                        return 'nodo ya hundido'
                else:
                    disparo(posx,int(posy),1,juegoactual.tipo_disparo,0,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res='fallo')
                    juegoactual.fallados2.satelites.insertar(posx,int(posy))
                    juegoactual.tirosf2+=1
                    juegoactual.cubodisparos2.satelites.insertar(posx,int(posy))

                    return 'fallo'
            elif nivel == '2':
                nod = juegoactual.cubo1.aviones.buscar(posx,int(posy))
                if nod is not None:
                    if not nod.hundido:
                        res=nod.nave.contar()
                        disparo(posx,int(posy),2,juegoactual.tipo_disparo,1,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res=res)
                        juegoactual.acertados2.aviones.insertar(posx,int(posy))
                        juegoactual.tirosa2+=1
                        juegoactual.cubodisparos2.aviones.insertar(posx,int(posy),hundido=True)
                        nod.hundido = True

                        return 'exito'
                    else:
                        return 'nodo ya hundido'
                else:
                    disparo(posx,int(posy),2,juegoactual.tipo_disparo,0,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res='fallo')
                    juegoactual.fallados2.satelites.insertar(posx,int(posy))
                    juegoactual.tirosf2+=1
                    juegoactual.cubodisparos2.satelites.insertar(posx,int(posy))

                    return 'fallo'
            elif nivel == '3':
                nod = juegoactual.cubo1.barcos.buscar(posx,int(posy))
                if nod is not None:
                    if not nod.hundido:
                        res=nod.nave.contar()
                        disparo(posx,int(posy),3,juegoactual.tipo_disparo,1,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res=res)
                        juegoactual.acertados2.barcos.insertar(posx,int(posy))
                        juegoactual.tirosa2+=1
                        juegoactual.cubodisparos2.barcos.insertar(posx,int(posy),hundido=True)
                        nod.hundido = True

                        return 'exito'
                    else:
                        return 'nodo ya hundido'
                else:
                    disparo(posx,int(posy),3,juegoactual.tipo_disparo,0,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res='fallo')
                    juegoactual.fallados2.barcos.insertar(posx,int(posy))
                    juegoactual.tirosf2+=1
                    juegoactual.cubodisparos2.barcos.insertar(posx,int(posy))

                    return 'fallo'
            elif nivel == '4':
                nod = juegoactual.cubo1.submarinos.buscar(posx,int(posy))
                if nod is not None:
                    if not nod.hundido:
                        res=nod.nave.contar()
                        disparo(posx,int(posy),4,juegoactual.tipo_disparo,1,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res=res)
                        juegoactual.acertados2.submarinos.insertar(posx,int(posy))
                        juegoactual.tirosa2+=1
                        juegoactual.cubodisparos2.submarinos.insertar(posx,int(posy),hundido=True)
                        nod.hundido = True

                        return 'exito'
                    else:
                        return 'nodo ya hundido'
                else:
                    disparo(posx,int(posy),4,juegoactual.tipo_disparo,0,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res='fallo')
                    juegoactual.fallados2.submarinos.insertar(posx,int(posy))
                    juegoactual.tirosf2+=1
                    juegoactual.cubodisparos2.submarinos.insertar(posx,int(posy))

                    return 'fallo'
            else:
                return 'nivel incorrecto'
        else:
            return 'No es el turno del jugador'
    else:
        return 'El jugador no esta en la partida'


def revisarsegundos():
    tiempo = tem.final - time.time()
    revisar()
    return (tiempo)

def contar(tiempo):
    #tiempo = str(request.form['tiempo'])
    tem.inicio = time.time()
    tem.final = time.time() + int(tiempo)
    return 'iniciado'

def guardar():
    jugador1 = ar.buscar(ar.raiz,juegoactual.jugador1)
    jugador2 = ar.buscar(ar.raiz,juegoactual.jugador2)
    if juegoactual.acertados1 > juegoactual.acertados2:
        par1 = partida(oponente=juegoactual.jugador2,tiros=juegoactual.disparos,acertados=juegoactual.acertados1,fallados=juegoactual.fallados1,resultado=1,danio=juegoactual.acertados2,eliminadas=0) #arreglar esto
        jugador1.lista.insertar(par1)
        par2 = partida(oponente=juegoactual.jugador1,tiros=juegoactual.disparos,acertados=juegoactual.acertados2,fallados=juegoactual.fallados2,resultado=0,danio=juegoactual.acertados1,eliminadas=0)
        jugador2.lista.insertar(par2)
    else:
        par1 = partida(oponente=juegoactual.jugador2,tiros=juegoactual.disparos,acertados=juegoactual.acertados1,fallados=juegoactual.fallados1,resultado=0,danio=juegoactual.acertados2,eliminadas=0) #arreglar esto
        jugador1.lista.insertar(par1)
        par2 = partida(oponente=juegoactual.jugador1,tiros=juegoactual.disparos,acertados=juegoactual.acertados2,fallados=juegoactual.fallados2,resultado=1,danio=juegoactual.acertados1,eliminadas=0)
        jugador2.lista.insertar(par2)
    #terminar código partida

def disparo(x,y,nivel,tipo,resultado,emisor,receptor,fecha,tiempo=0,res=''):
    if juegoactual.variante == 2:
        if juegoactual.disparos == 0:
            contar(juegoactual.tiempo)
    juegoactual.disparos += 1
    ti=revisar()
    dis = Disparo(x,y,nivel,tipo,resultado,emisor,receptor,fecha,juegoactual.disparos,ti)
    dis.res = res

    juegoactual.historial.insertar(juegoactual.historial.raiz,dis)


@app.route('/consultausuarios',methods=['POST'])
def conusaruios():
    par = str(request.form['jugador'])
    #juegos.imprimir()
    listaconsulta.ordenamiento()
    cadena = listaconsulta.imprimir()
    return cadena

@app.route('/consultajuegos',methods=['POST'])
def conjuegos():
    par = str(request.form['jugador'])
    #juegos.imprimir()
    juegos.ordenamiento()
    cadena = juegos.imprimir()
    return cadena

@app.route('/disparar',methods=['POST'])
def disparar():
    if juegoactual.disparos > 0:
        if revisarsegundos() > 0:
            print("Juego en curso")
        else:
            print("El juego ha acabado")
            return('El juego ha acabado')
    jugador = str(request.form['jugador'])
    nivel = str(request.form['nivel'])
    posx = str(request.form['posx'])
    posy = str(request.form['posy'])
    us = ar.buscar(ar.raiz,jugador)
    print('disparo')
    if not Reprint(posy):
        return 'Valores incorrectos'
    else:
        pass
    if not posx.isalpha():
        return 'Valores incorrectos'
    else:
        pass
    if us is not None:
        if jugador == juegoactual.jugador1:
            if jugador == juegoactual.turno:
                #dis = ar.buscar(ar.raiz,juegoactual.jugador2)
                if nivel == '1':
                    nod = juegoactual.cubo2.satelites.buscar(posx,int(posy))
                    print('satelites: ' + posx + " , " +  posy)
                    if nod is not None:
                        if not nod.hundido:
                            juegoactual.acertados1.satelites.insertar(posx,int(posy))
                            juegoactual.cubodisparos1.satelites.insertar(posx,int(posy),hundido=True)
                            juegoactual.tirosa1+=1
                            res=nod.nave.contar()
                            disparo(posx,int(posy),1,juegoactual.tipo_disparo,1,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res=res)
                            nod.hundido = True
                            #Agregar código para ráfaga
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        juegoactual.fallados1.satelites.insertar(posx,int(posy))
                        juegoactual.cubodisparos1.satelites.insertar(posx,int(posy))
                        juegoactual.tirosf1+=1
                        disparo(posx,int(posy),1,juegoactual.tipo_disparo,0,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res='fallo')
                        #Agregar código para ráfaga
                        juegoactual.cambiarturno()
                        return 'fallo'
                elif nivel == '2':
                    nod = juegoactual.cubo2.aviones.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            res=nod.nave.contar()
                            disparo(posx,int(posy),2,juegoactual.tipo_disparo,1,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res=res)
                            juegoactual.acertados1.aviones.insertar(posx,int(posy))
                            juegoactual.tirosa1+=1
                            juegoactual.cubodisparos1.aviones.insertar(posx,int(posy),hundido=True)
                            nod.hundido = True
                            #ráfaga
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        juegoactual.fallados1.aviones.insertar(posx,int(posy))
                        juegoactual.cubodisparos1.aviones.insertar(posx,int(posy))
                        juegoactual.tirosf1+=1
                        disparo(posx,int(posy),2,juegoactual.tipo_disparo,0,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res='fallo')
                        #ráfaga
                        juegoactual.cambiarturno()
                        return 'fallo'
                elif nivel == '3':
                    nod = juegoactual.cubo2.barcos.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            res=nod.nave.contar()
                            disparo(posx,int(posy),3,juegoactual.tipo_disparo,1,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res=res)
                            juegoactual.acertados1.barcos.insertar(posx,int(posy))
                            juegoactual.tirosa1+=1
                            juegoactual.cubodisparos1.barcos.insertar(posx,int(posy),hundido=True)
                            nod.hundido = True
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        disparo(posx,int(posy),3,juegoactual.tipo_disparo,0,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res='fallo')
                        juegoactual.fallados1.barcos.insertar(posx,int(posy))
                        juegoactual.tirosf1+=1
                        juegoactual.cubodisparos1.barcos.insertar(posx,int(posy))
                        juegoactual.cambiarturno()
                        return 'fallo'
                elif nivel == '4':
                    nod = juegoactual.cubo2.submarinos.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            res=nod.nave.contar()
                            disparo(posx,int(posy),4,juegoactual.tipo_disparo,1,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res=res)
                            juegoactual.acertados1.submarinos.insertar(posx,int(posy))
                            juegoactual.tirosa1+=1
                            juegoactual.cubodisparos1.submarinos.insertar(posx,int(posy),hundido=True)
                            nod.hundido = True
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        disparo(posx,int(posy),4,juegoactual.tipo_disparo,0,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today(),tiempo=revisar(),res='fallo')
                        juegoactual.fallados1.submarinos.insertar(posx,int(posy))
                        juegoactual.tirosf1+=1
                        juegoactual.cubodisparos1.submarinos.insertar(posx,int(posy))
                        juegoactual.cambiarturno()
                        return 'fallo'
                else:
                    return 'nivel incorrecto'
            else:
                return 'no es el turno del jugador'
        elif jugador == juegoactual.jugador2:
            if jugador == juegoactual.turno:
                #dis = ar.buscar(ar.raiz,juegoactual.jugador1)
                if nivel == '1':
                    nod = juegoactual.cubo1.satelites.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            res=nod.nave.contar()
                            disparo(posx,int(posy),1,juegoactual.tipo_disparo,1,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res=res)
                            juegoactual.acertados2.satelites.insertar(posx,int(posy))
                            juegoactual.tirosa2+=1
                            juegoactual.cubodisparos2.satelites.insertar(posx,int(posy),hundido=True)
                            nod.hundido = True
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        disparo(posx,int(posy),1,juegoactual.tipo_disparo,0,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res='fallo')
                        juegoactual.fallados2.satelites.insertar(posx,int(posy))
                        juegoactual.tirosf2+=1
                        juegoactual.cubodisparos2.satelites.insertar(posx,int(posy))
                        juegoactual.cambiarturno()
                        return 'fallo'
                elif nivel == '2':
                    nod = juegoactual.cubo1.aviones.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            res=nod.nave.contar()
                            disparo(posx,int(posy),2,juegoactual.tipo_disparo,1,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res=res)
                            juegoactual.acertados2.aviones.insertar(posx,int(posy))
                            juegoactual.tirosa2+=1
                            juegoactual.cubodisparos2.aviones.insertar(posx,int(posy),hundido=True)
                            nod.hundido = True
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        disparo(posx,int(posy),2,juegoactual.tipo_disparo,0,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res='fallo')
                        juegoactual.fallados2.satelites.insertar(posx,int(posy))
                        juegoactual.tirosf2+=1
                        juegoactual.cubodisparos2.satelites.insertar(posx,int(posy))
                        juegoactual.cambiarturno()
                        return 'fallo'
                elif nivel == '3':
                    nod = juegoactual.cubo1.barcos.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            res=nod.nave.contar()
                            disparo(posx,int(posy),3,juegoactual.tipo_disparo,1,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res=res)
                            juegoactual.acertados2.barcos.insertar(posx,int(posy))
                            juegoactual.tirosa2+=1
                            juegoactual.cubodisparos2.barcos.insertar(posx,int(posy),hundido=True)
                            nod.hundido = True
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        disparo(posx,int(posy),3,juegoactual.tipo_disparo,0,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res='fallo')
                        juegoactual.fallados2.barcos.insertar(posx,int(posy))
                        juegoactual.tirosf2+=1
                        juegoactual.cubodisparos2.barcos.insertar(posx,int(posy))
                        juegoactual.cambiarturno()
                        return 'fallo'
                elif nivel == '4':
                    nod = juegoactual.cubo1.submarinos.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            res=nod.nave.contar()
                            disparo(posx,int(posy),4,juegoactual.tipo_disparo,1,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res=res)
                            juegoactual.acertados2.submarinos.insertar(posx,int(posy))
                            juegoactual.tirosa2+=1
                            juegoactual.cubodisparos2.submarinos.insertar(posx,int(posy),hundido=True)
                            nod.hundido = True
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        disparo(posx,int(posy),4,juegoactual.tipo_disparo,0,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today(),tiempo=revisar(),res='fallo')
                        juegoactual.fallados2.submarinos.insertar(posx,int(posy))
                        juegoactual.tirosf2+=1
                        juegoactual.cubodisparos2.submarinos.insertar(posx,int(posy))
                        juegoactual.cambiarturno()
                        return 'fallo'
                else:
                    return 'nivel incorrecto'
            else:
                return 'No es el turno del jugador'
        else:
            return 'El jugador no esta en la partida'
    else:
        return'error'


@app.route('/revisar',methods=['POST'])
def revisar():
    tiempo = tem.final - time.time()
    t = divmod(tiempo,60)
    dec, segundos = math.modf(t[1])
    print ('minutos: ' + str(t[0]) + ' segundos: ' + str(segundos))
    cad = 'minutos: ' + str(t[0]) + ' segundos: ' + str(segundos)
    return (cad)

@app.route('/parametros',methods=['POST'])
def parametros():
    x = juegoactual.x
    y = juegoactual.y
    cadena = str(x) + "," + str(y)
    return (cadena)

@app.route('/jugadores',methods=['POST'])
def enemigo():
    jugador=str(request.form['jugador'])
    if jugador == juegoactual.jugador1:
        return juegoactual.jugador2
    elif jugador == juegoactual.jugador2:
        return juegoactual.jugador1
    else:
        return "no está en la partida"

@app.route('/tableros',methods=['POST'])
def tableros():
    nivel = str(request.form['nivel'])
    jugador = str(request.form['usuario'])

    #u = ar.buscar(ar.raiz,jugador)
    if jugador is not None:
        if nivel == '1':
            if jugador == juegoactual.jugador1:
                return juegoactual.cubo1.satelites.recorreref()
            elif jugador == juegoactual.jugador2:
                return juegoactual.cubo2.satelites.recorreref()
            else:
                return "error"
        elif nivel == '2':
            if jugador == juegoactual.jugador1:
                return juegoactual.cubo1.aviones.recorreref()
            elif jugador == juegoactual.jugador2:
                return juegoactual.cubo2.aviones.recorreref()
            else:
                return "error"
        elif nivel == '3':
            if jugador == juegoactual.jugador1:
                return juegoactual.cubo1.barcos.recorreref()
            elif jugador == juegoactual.jugador2:
                return juegoactual.cubo2.barcos.recorreref()
            else:
                return "error"
        elif nivel == '4':
            if jugador == juegoactual.jugador1:
                return juegoactual.cubo1.submarinos.recorreref()
            elif jugador == juegoactual.jugador2:
                return juegoactual.cubo2.submarinos.recorreref()
            else:
                return "error"
    else:
        return 'Error'

@app.route('/tablerosen',methods=['POST'])
def tablerosen():
    nivel = str(request.form['nivel'])
    jugador = str(request.form['usuario'])

    #u = ar.buscar(ar.raiz,jugador)
    if jugador is not None:
        if nivel == '1':
            if jugador == juegoactual.jugador1:
                return juegoactual.cubodisparos2.satelites.recorreref()
            elif jugador == juegoactual.jugador2:
                return juegoactual.cubodisparos1.satelites.recorreref()
            else:
                return "error"
        elif nivel == '2':
            if jugador == juegoactual.jugador1:
                return juegoactual.cubodisparos2.aviones.recorreref()
            elif jugador == juegoactual.jugador2:
                return juegoactual.cubodisparos1.aviones.recorreref()
            else:
                return "error"
        elif nivel == '3':
            if jugador == juegoactual.jugador1:
                return juegoactual.cubodisparos2.barcos.recorreref()
            elif jugador == juegoactual.jugador2:
                return juegoactual.cubodisparos1.barcos.recorreref()
            else:
                return "error"
        elif nivel == '4':
            if jugador == juegoactual.jugador1:
                return juegoactual.cubodisparos2.submarinos.recorreref()
            elif jugador == juegoactual.jugador2:
                return juegoactual.cubodisparos1.submarinos.recorreref()
            else:
                return "error"
    else:
        return 'Error'

@app.route('/registrar',methods=['POST'])
def registrar():
    nombre = str(request.form['nombre'])
    contra = str(request.form['contra'])
    usuario = Usuario(nombre.strip(),contra.strip(),0)
    ar.insertar(usuario)
    ha.insertar(usuario)
    return "True"

@app.route('/iniciar',methods=['POST'])
def iniciar():
    nombre = str(request.form['nombre'])
    contra = str(request.form['contra'])
    dato = ar.buscar(ar.raiz,nombre)
    print(nombre + ' ' + contra)
    if dato is not None:
        print(dato.contrasena.strip() + " = " + contra)
        if dato.contrasena == contra:
            return "True"
        else:
            return "False"
    else:
        return "False"

@app.route('/partidas',methods=['POST'])
def partidas():
    nombre = str(request.form['nombre'])
    dato = ar.buscar(ar.raiz,nombre)
    return dato.lista.mostrarnumeros()
    #agregar partidas

@app.route('/codigoq',methods=['POST'])
def codigoq():
    nombre = str(request.form['nombre'])
    dato = str(request.form['dato'])
    usuario = ar.buscar(ar.raiz,nombre)
    js = usuario.lista.buscarnumero(int(dato))
    img = qrcode.make(js)
    img.save("C:\\Users\\Abraham Jelkmann\\Desktop\\qr.bmp")
    with open("C:\\Users\\Abraham Jelkmann\\Desktop\\qr.bmp",'rb') as imageFile:
        cadena = base64.b64encode(imageFile.read())
    return cadena
    #agregar partidas

@app.route('/carga',methods=['POST'])
def cargar():
    tipo = str(request.form['tipo'])
    print(tipo)
    if tipo == 'usuarios':
        nombre = str(request.form['nombre'])
        contra = str(request.form['contra'])
        conectado = str(request.form['conectado'])
        u = Usuario(nombre.strip(),contra.strip(),int(conectado))
        ar.insertar(u)
        ha.insertar(u)
        listaconsulta.insertar(u)
        print(nombre,contra,conectado)
        return "True"

    elif tipo == 'naves':
        jugador = str(request.form['jugador'])
        columna = str(request.form['columna'])
        fila = str(request.form['fila'])
        nivel = str(request.form['nivel'])
        modo = str(request.form['modo'])
        direccion = str(request.form['direccion'])

        #usuario = ar.buscar(ar.raiz,jugador)

        if nivel == '1':
            s = Satelite()
            if jugador == juegoactual.jugador1:
                s.colocar(juegoactual.cuboinicial1.satelites,columna,int(fila))
                s.colocar(juegoactual.cubo1.satelites,columna,int(fila))
            elif jugador == juegoactual.jugador2:
                s.colocar(juegoactual.cuboinicial2.satelites,columna,int(fila))
                s.colocar(juegoactual.cubo2.satelites,columna,int(fila))
            else:
                print("el jugador no está en la partida")
            print('Satelite')
            return 'satelite'

        elif nivel == '2':
            a = Avion(int(modo))
            if jugador == juegoactual.jugador1:
                a.colocar(juegoactual.cuboinicial1.aviones,columna,int(fila))
                a.colocar(juegoactual.cubo1.aviones,columna,int(fila))
            elif jugador == juegoactual.jugador2:
                a.colocar(juegoactual.cuboinicial2.aviones,columna,int(fila))
                a.colocar(juegoactual.cubo2.aviones,columna,int(fila))
            else:
                print("el jugador no está en la partida")
            print('Avion')
            return 'Avion'

        elif nivel == '3':
            b = Barco(int(modo),int(direccion))
            if jugador == juegoactual.jugador1:
                b.colocar(juegoactual.cuboinicial1.barcos,columna,int(fila))
                b.colocar(juegoactual.cubo1.barcos,columna,int(fila))
            elif jugador == juegoactual.jugador2:
                b.colocar(juegoactual.cuboinicial2.barcos,columna,int(fila))
                b.colocar(juegoactual.cubo2.barcos,columna,int(fila))
            else:
                print("el jugador no está en la partida")
            print('Barco')
            return 'Barco'

        elif nivel == '4':
            sub = Submarino(int(modo),int(direccion))
            if jugador == juegoactual.jugador1:
                sub.colocar(juegoactual.cuboinicial1.submarinos,columna,int(fila))
                sub.colocar(juegoactual.cubo1.submarinos,columna,int(fila))
            elif jugador == juegoactual.jugador2:
                sub.colocar(juegoactual.cuboinicial2.submarinos,columna,int(fila))
                sub.colocar(juegoactual.cubo2.submarinos,columna,int(fila))
            else:
                print("el jugador no está en la partida")
            print('submarino')
            return 'submarino'

    elif tipo == 'partidas':
        usuario = str(request.form['usuario'])
        oponente = str(request.form['oponente'])
        tiros = str(request.form['tiros'])
        acertados = str(request.form['acertados'])
        fallados = str(request.form['fallados'])
        ganada = str(request.form['ganada'])
        danio = str(request.form['danio'])

        p = partida(oponente,int(tiros),int(acertados),int(fallados),int(ganada),int(danio))
        juegos.insertar(p)
        usuario = ar.buscar(ar.raiz,usuario)
        usuario.lista.insertar(p)
        print('agregando partida a: ' + str(usuario))
        return 'partida agregada'
    elif tipo == 'juego':
        usuario1 = str(request.form['usuario1'])
        usuario2 = str(request.form['usuario2'])
        tamx = str(request.form['tamx'])
        tamy = str(request.form['tamy'])
        variante = str(request.form['variante'])
        tiempo = str(request.form['tiempo'])
        tipodisparo = str(request.form['tipodisparo'])
        numerodisparos = str(request.form['numerodisparos'])
        juegoactual.turno = usuario1
        juegoactual.jugador1 = usuario1
        juegoactual.jugador2 = usuario2
        juegoactual.x = int(tamx)
        juegoactual.y = int(tamy)
        juegoactual.variante = int(variante)
        juegoactual.tiempo = tiempo
        juegoactual.tipo_disparo = tipodisparo
        juegoactual.numerodisparos = int(numerodisparos)
        juegoactual.disparos =0
        t = Timer(tiempo,guardar)
        print('tiempo de juego: ' + tiempo + ' segundos')
        return 'juego creado'
    elif tipo == 'tiros':
        jugador = str(request.form['usuario'])
        posx = str(request.form['columna'])
        posy = str(request.form['fila'])
        print(jugador + " " + posx + " " + posy)
        print(tiromasivo(jugador,"1",posx,int(posy)))
        return "tiro"
    elif tipo == 'contactos':
        usuario = str(request.form['usuario'])
        nickname = str(request.form['nickname'])
        contra = str(request.form['contra'])
        u = ar.buscar(ar.raiz,usuario)
        con = Contacto(nickname,contra)
        if ar.buscar(ar.raiz,nickname) is not None:
            con.existe='existe'
        if u is not None:
            u.contactos.insertar(con)
        return 'ingresado'
    elif tipo == 'historial':
        posx = str(request.form['posx'])
        posy = str(request.form['posy'])
        tipo = str(request.form['tipod'])
        resultado = str(request.form['resultado'])
        nave = str(request.form['nave'])
        emi = str(request.form['emisor'])
        rece = str(request.form['receptor'])
        fecha = str(request.form['fecha'])
        tiempo = str(request.form['tiempo'])
        numero = str(request.form['numero'])
        dat = Disparo(x=posx,y=int(posy),nave=int(nave),tipo=int(tipo),resultado=int(resultado),emisor=emi,receptor=rece,fecha=fecha,numero=int(numero),tiempo=tiempo)
        historial.insertar(historial.raiz,dat)
        return 'ingresado'

@app.route('/limpiar',methods=['POST'])
def limpiar():
    historial.limpiar()
    return 'limpio'

@app.route('/errores',methods=['POST'])
def errores():
    error = str(request.form['error'])
    print(error)
    return 'impre'

@app.route('/graficar',methods=['POST'])
def graf():
    nombre = str(request.form['nombre'])
    nick = str(request.form['nickname'])
    imagen = str(request.form['imagen'])
    if nombre == 'matriz':
        if imagen == 'satelites':
            #us = ar.buscar(ar.raiz,nick)
            if nick == juegoactual.jugador1:
                juegoactual.cubo1.satelites.graficar(imagen)
            else:
                juegoactual.cubo2.satelites.graficar(imagen)
            print('graficando satelites')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'barcos':
            us = ar.buscar(ar.raiz,nick)
            #print('graficando barcos')
            if nick == juegoactual.jugador1:
                juegoactual.cubo1.barcos.graficar(imagen)
            else:
                juegoactual.cubo2.barcos.graficar(imagen)
            #us.cubo.barcos.graficar(imagen)
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'aviones':
            #us = ar.buscar(ar.raiz,nick)
            if nick == juegoactual.jugador1:
                juegoactual.cubo1.aviones.graficar(imagen)
            else:
                juegoactual.cubo2.aviones.graficar(imagen)
            #us.cubo.aviones.graficar(imagen)
            print('graficando aviones')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'submarinos':
            #us = ar.buscar(ar.raiz,nick)
            if nick == juegoactual.jugador1:
                juegoactual.cubo1.submarinos.graficar(imagen)
            else:
                juegoactual.cubo2.submarinos.graficar(imagen)
            #us.cubo.submarinos.graficar(imagen)
            print('graficando submarinos')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        return cadena
    elif nombre == 'arbol':
        dot = Digraph(comment='Arbol',format='png')
        dot = ar.graficar(ar.raiz,0,dot)
        dot.render("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen,cleanup=True)
        dot.save(imagen,r"C:\\Users\\Abraham Jelkmann\\Desktop")
        with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
            cadena = base64.b64encode(imageFile.read())
        return cadena
    elif nombre == 'arbolconlistas':
        dot = Digraph(comment='arbolconlistas',format='png')
        dot = ar.graficarconlista(ar.raiz,0,dot)
        dot.render("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen,cleanup=True)
        dot.save(imagen,r"C:\\Users\\Abraham Jelkmann\\Desktop")
        with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
            cadena = base64.b64encode(imageFile.read())
        return cadena
    elif nombre == 'acertados':
        if imagen == 'satelites':
            #us = ar.buscar(ar.raiz,nick)
            if nick == juegoactual.jugador1:
                juegoactual.acertados1.satelites.graficar(imagen)
            else:
                juegoactual.acertados2.satelites.graficar(imagen)
            #us.acertados.satelites.graficar(imagen)
            print('graficando satelites')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'barcos':
            if nick == juegoactual.jugador1:
                juegoactual.acertados1.barcos.graficar(imagen)
            else:
                juegoactual.acertados2.barcos.graficar(imagen)
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'aviones':
            if nick == juegoactual.jugador1:
                juegoactual.acertados1.aviones.graficar(imagen)
            else:
                juegoactual.acertados2.aviones.graficar(imagen)
            print('graficando aviones')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'submarinos':
            if nick == juegoactual.jugador1:
                juegoactual.acertados1.submarinos.graficar(imagen)
            else:
                juegoactual.acertados2.submarinos.graficar(imagen)
            print('graficando submarinos')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        return cadena
    elif nombre == 'fallados':
        if imagen == 'satelites':
            if nick == juegoactual.jugador1:
                juegoactual.fallados1.satelites.graficar(imagen)
            else:
                juegoactual.fallados2.satelites.graficar(imagen)
            print('graficando satelites')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'barcos':
            if nick == juegoactual.jugador1:
                juegoactual.fallados1.barcos.graficar(imagen)
            else:
                juegoactual.fallados2.barcos.graficar(imagen)
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'aviones':
            if nick == juegoactual.jugador1:
                juegoactual.fallados1.aviones.graficar(imagen)
            else:
                juegoactual.fallados2.aviones.graficar(imagen)
            print('graficando aviones')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'submarinos':
            if nick == juegoactual.jugador1:
                juegoactual.fallados1.submarinos.graficar(imagen)
            else:
                juegoactual.fallados2.submarinos.graficar(imagen)
            print('graficando submarinos')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        return cadena
    elif nombre == 'arbolb':
        juegoactual.historial.graf('arbolbjuego')
        print('graficando arbol b')
        with open("C:\\Users\\Abraham Jelkmann\\Desktop\\arbolbjuego.png",'rb') as imageFile:
            cadena = base64.b64encode(imageFile.read())
        return cadena
    elif nombre == 'historial':
        historial.graf('historial')
        with open("C:\\Users\\Abraham Jelkmann\\Desktop\\historial.png",'rb') as imageFile:
            cadena = base64.b64encode(imageFile.read())
        return cadena
    elif nombre == 'contactos':
        us = ar.buscar(ar.raiz,nick)
        us.contactos.graficar('avl')
        with open("C:\\Users\\Abraham Jelkmann\\Desktop\\avl.png",'rb') as imageFile:
            cadena = base64.b64encode(imageFile.read())
        return cadena
    elif nombre == 'hash':
        ha.graficar('thash')
        with open("C:\\Users\\Abraham Jelkmann\\Desktop\\thash.png",'rb') as imageFile:
            cadena = base64.b64encode(imageFile.read())
        return cadena
    else:
        return 'error'

@app.route('/android',methods=['POST'])
def android():
    nombre = str(request.form['p'])
    print(nombre + ' desde android')
    return 'hola'

@app.route('/paramb',methods=['POST'])
def paramb():
    param = str(request.form['param'])
    Disparo.parametro=param.lower()
    print('parametro: ' + param)
    return 'establecido'

@app.route('/eliminarcontacto',methods=['POST'])
def eliminarc():
    nombre = str(request.form['nombre'])
    nick = str(request.form['nickname'])
    u = ar.buscar(ar.raiz,nombre)
    u.contactos.eliminar(Contacto(nick,''))
    return 'eliminado'

@app.route('/editarcontacto',methods=['POST'])
def editarc():
    nombre = str(request.form['nombre'])
    nick = str(request.form['nickname'])
    nuevo=str(request.form['nuevo'])
    u = ar.buscar(ar.raiz,nombre)
    u.contactos.editar(Contacto(nick,''),nuevo)
    return 'editado'

@app.route('/editarb',methods=['POST'])
def editarb():
    tiro = str(request.form['numero'])
    x = str(request.form['x'])
    y = str(request.form['y'])
    xx = str(request.form['xx'])
    yy = str(request.form['yy'])
    d = Disparo(x=xx,y=int(yy),numero=int(tiro))
    d.parametro=Disparo.parametro
    print(str(d))
    nod = juegoactual.historial.editar(d,x,int(y))
    return 'editado'


#@app.route('/')


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

"""
par = partida('chuz',10,2,3,0,15)
par1=partida('asdf',2,4,5,1,2)
print(par.numero)
print(par1.numero)
"""

"""
li = ListaDoble()
li.insertar(4)
li.insertar(10)
li.insertar(2)
li.insertar(14)
li.insertar(11)
li.insertar(1)
li.ordenamiento()
li.imprimir()
#li.graficar()
"""

"""
sat = Satelite()
bar = Barco(2,1)

mat = MatrizDispersa()
mat.insertar('A',2)
mat.insertar('B',5)
mat.insertar('A',10)
mat.insertar('A',5)
mat.insertar('C',7)
mat.insertar('G',15)
mat.insertar('C',8)
sat.colocar(mat,'G',5)
bar.colocar(mat,'H',10)
mat.recorreref()
mat.recorrer()
mat.graficar('asdf')
numval('a')
numval('B')
"""
#p=partida('chuz',32,2,30,1,3)
#img = qrcode.make(p.json())
#img.save("C:\\Users\\Abraham Jelkmann\\Desktop\\qr.bmp")
