from flask import Flask, request, Response
from graphviz import Digraph
import base64
import threading
import time
import datetime
from threading import Timer
import math
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
    def __init__(self,espacios=0):
        self.espacios=espacios

class juego(object):
    def __init__(self,naves=0,tipo_disparo=None,x=0,y=0,variante=None):
        self.tipo_disparo=tipo_disparo
        self.x=x
        self.y=y
        self.variante=variante
        self.tiempo=0
        self.jugador1=None
        self.jugador2=None
        self.turno=None
        self.numerodisparos = 0
        self.disparos=0
    def cambiarturno(self):
        if self.jugador1.upper() == self.turno.upper():
            self.turno = self.jugador2
            print('Turno de: ' + self.jugador2)
        elif self.jugador2.upper() == self.turno.upper():
            self.turno = self.jugador1
            print('Turno de: ' + self.jugador1)
        else:
            print('Error')

class Barco(object):
    def __init__(self,modo=None,direccion=None):
        self.modo=modo
        self.direccion=direccion
    def colocar(self,matriz,x,y):
        if self.modo == 1:
            matriz.insertar(x,y)
        elif self.modo == 2:
            if self.direccion == 1:
                matriz.insertar(x,y)
                matriz.insertar(sumar(x,1),y)
            else:
                matriz.insertar(x,y)
                matriz.insertar(x,(y+1))
        elif self.modo == 3:
            if self.direccion == 1:
                matriz.insertar(x,y)
                matriz.insertar(sumar(x,1),y)
                matriz.insertar(sumar(x,2),y)
            else:
                matriz.insertar(x,y)
                matriz.insertar(x,(y+1))
                matriz.insertar(x,(y+2))

class Avion(object):
    def __init__(self,modo=None):
        self.modo=modo
    def colocar(self,matriz,x,y):
        if self.modo == 1:
            matriz.insertar(x,y)
            matriz.insertar(sumar(x,1),y)
            matriz.insertar(restar(x,1),y)
            matriz.insertar(x,y+1)
        elif self.modo == 2:
            matriz.insertar(x,y-1)
            matriz.insertar(x,y)
            matriz.insertar(sumar(x,1),y)
            matriz.insertar(restar(x,1),y)
            matriz.insertar(x,y+1)
            matriz.insertar(x,y+2)
             #colocar aviones

class Submarino(object):
    def __init__(self,modo,direccion):
        self.modo=modo
        self.direccion = direccion
    def colocar(self,matriz,x,y):
        if self.modo == 1:
            matriz.insertar(x,y)
        elif self.modo == 2:
            if self.direccion == 1:
                matriz.insertar(x,y)
                matriz.insertar(sumar(x,1),y)
            else:
                matriz.insertar(x,y)
                matriz.insertar(x,(y+1))
        elif self.modo == 3:
            if self.direccion == 1:
                matriz.insertar(x,y)
                matriz.insertar(sumar(x,1),y)
                matriz.insertar(sumar(x,2),y)
            else:
                matriz.insertar(x,y)
                matriz.insertar(x,(y+1))
                matriz.insertar(x,(y+2))

class Satelite(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def colocar(self,matriz,x,y):
        matriz.insertar(x,y)

class Usuario(object):
    def __init__(self,nombre=None,contrasena=None,conectado=None):
        self.nombre=nombre
        self.contrasena=contrasena
        self.conectado=conectado
        self.lista = ListaDoble()
        self.cubo = Cubo()
        self.acertados = Cubo()
        self.fallados = Cubo()
        self.ganadas = 0
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
    def __init__(self,oponente=None,tiros=0,acertados=0,fallados=0,resultado=None,danio=0):
        self.oponente=oponente
        self.tiros=tiros
        self.acertados=acertados
        self.fallados=fallados
        self.resultado=resultado
        self.danio=danio
    def __str__(self):
        if self.resultado == 0:
            res = 'perdida'
        else:
            res = 'ganada'
        cadena = str(self.oponente) + ' ' + str(self.tiros) + ' ' + res
        return cadena

class NodoAbb(object):
    def __init__(self,dato=None):
        self.dato=dato
        self.izquierda=None
        self.derecha=None

class NodoMatriz(object):
    def __init__(self,dato=None):
        self.dato = 'X'
        self.arriba=None
        self.abajo=None
        self.derecha=None
        self.izquierda=None
        self.hundido=False
        self.disparado=False
        self.x=0
        self.y=0

class MatrizDispersa(object):
    def __init__(self):
        self.cabeza=NodoMatriz()
    def insertar(self,x,y):
        nodox = NodoMatriz()
        nodox.x = x
        nodox.dato = (str(x)+','+str(0))
        nodoy= NodoMatriz()
        nodoy.y = y
        nodoy.dato = (str(0)+','+str(y))
        nodoin=NodoMatriz()
        nodoin.x=x
        nodoin.y=y
        nodoin.dato = (str(x)+','+str(y))
        insertado=False
        horizontal=False
        vertical=False
        actual = self.cabeza
        if self.cabeza.derecha is not None:
            while actual.derecha is not None:
                if actual.derecha.x == x:
                    horizontal = True
                    break
                elif actual.derecha.x < x:
                    actual = actual.derecha
                else:
                    break
        if not horizontal:
            #print('añadiendo nodo derecha')
            if actual.derecha is not None:
                actual.derecha.izquierda = nodox
                nodox.derecha = actual.derecha
            nodox.izquierda = actual
            actual.derecha = nodox
            horizontal=True
        actual = self.cabeza
        if self.cabeza.abajo is not None:
            while actual.abajo is not None:
                if actual.abajo.y == y:
                    vertical = True
                    break
                elif actual.abajo.y < y:
                    actual = actual.abajo
                else:
                    break
        if  not vertical:
            #print('añadiendo nodo abajo')
            if actual.abajo is not None:
                actual.abajo.arriba = nodoy
                nodoy.abajo = actual.abajo
            nodoy.arriba = actual
            actual.abajo = nodoy
            vertical=True
        actual = self.cabeza
        #print('nodo actual: ' + str(actual.x) + str(actual.y))
        #print('nodo a ingresar: ' + str(nodoin.x) + str(nodoin.y))
        while actual.x != nodoin.x:
            if actual.derecha is not None:
                actual = actual.derecha
                #print(str(actual.x)+ ' = ' + str(nodoin.x))
            else:
                break
        if actual.abajo is not None:
            if actual.abajo.y < nodoin.y:
                while actual.abajo.y < nodoin.y:
                    actual = actual.abajo
                    if actual.abajo is None:
                        break
            if actual.abajo is not None:
                if actual.abajo.y > nodoin.y:
                    nodoin.abajo = actual.abajo
                    nodoin.arriba = actual
                    actual.abajo.arriba = nodoin
                    actual.abajo = nodoin
                else:
                    print("Error")
            else:
                actual.abajo = nodoin
                nodoin.arriba = actual
        else:
            actual.abajo = nodoin
            nodoin.arriba = actual
        actual = self.cabeza

        while actual.y != nodoin.y:
            if actual.abajo is not None:
                actual = actual.abajo
            else:
                break
        if actual.derecha is not None:
            if actual.derecha.x < nodoin.x:
                while actual.derecha.x < nodoin.x:
                    actual = actual.derecha
                    if actual.derecha is None:
                        break
            if actual.derecha is not None:
                if actual.derecha.x > nodoin.x:
                    nodoin.derecha = actual.derecha
                    nodoin.izquierda = actual
                    actual.derecha.izquierda = nodoin
                    actual.derecha = nodoin
                    insertado = True
                else:
                    print("Error")
            else:
                actual.derecha = nodoin
                nodoin.izquierda = actual
        else:
            actual.derecha = nodoin
            nodoin.izquierda = actual

    def graficar(self,imagen):
        actual = self.cabeza
        matriz = Digraph(comment='Matriz',format='png')
        contador = 0
        terminado = False
        matriz.attr('node',shape='box')
        matriz.attr('graph',rankdir='LR')
        matriz.node(str(actual.dato))
        while (not terminado):
            nodo = actual
            # print('dato actual: '+str(nodo.dato))
            while nodo.derecha is not None:
            #    print('graficando derecha')
                matriz.node(str(nodo.derecha.dato))
                matriz.edge(str(nodo.dato),str(nodo.derecha.dato))
                matriz.edge(str(nodo.derecha.dato),str(nodo.dato))
                if nodo.arriba is not None:
                #    print('graficando abajo')
                # no    matriz.node(str(nodo.dato))
                    matriz.edge(str(nodo.dato),str(nodo.arriba.dato), constraint='false')
                    matriz.body.append('\t\t{rank=same;"' + str(nodo.arriba.dato) + '" -> "' + str(nodo.dato) + '";}')
                nodo = nodo.derecha

            if nodo.arriba is not None:
            #    print('graficando abajo')
            #    matriz.node(str(nodo.dato))
                matriz.edge(str(nodo.dato),str(nodo.arriba.dato), constraint='false')
                matriz.body.append('\t\t{rank=same;"' + str(nodo.arriba.dato) + '" -> "' + str(nodo.dato) + '";}')

            if actual.abajo is not None:
                actual = actual.abajo
            else:
                terminado = True
        #print(matriz.source)
        matriz.render("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen,cleanup=True)
        #matriz.save(imagen,"C:\\Users\\Abraham Jelkmann\\Desktop")

    def buscar(self,x,y):
        horizontal = False
        vertical = False
        actual = self.cabeza
        if self.cabeza is not None:
            while actual.derecha is not None:
                #print(actual.derecha.x + " = " + x)
                if actual.derecha.x == x:
                    actual = actual.derecha
                    horizontal = True
                    break
                elif actual.derecha.x < x:
                    actual = actual.derecha
                else:
                    break
        if horizontal:
            while actual.abajo is not None:
                #print(str(actual.derecha.y) + " = " + str(y))
                if actual.abajo.y == y:
                    actual = actual.derecha
                    vertical = True
                    break
                elif actual.abajo.y < y:
                    actual = actual.abajo
                else:
                    break
        if horizontal and vertical:
            return actual
        else:
            return None

    def recorrer(self):
        cadena = ''
        actual = self.cabeza
        if self.cabeza is not None:
            while actual.derecha is not None:
                actual = actual.derecha
                #print('la cabeza no esta vacia')
                if actual.abajo is not None:
                    #print('hay nodos abajo')
                    aux = actual
                    while aux.abajo is not None:
                        if aux.abajo.hundido:
                            hu = '1'
                        else:
                            hu = '0'
                        cadena = cadena + numval(aux.abajo.x) + ',' + str(aux.abajo.y) + ',' + hu + "\n"
                        aux = aux.abajo
        #print ('recorrido matriz: ' + cadena)
        return cadena
    def recorreref(self):
        cadena = ''
        actual = self.cabeza
        if self.cabeza is not None:
            while actual.abajo is not None:
                actual = actual.abajo
                if actual.derecha is not None:
                    aux = actual
                    while aux.derecha is not None:
                        if aux.derecha.hundido:
                            hu='1'
                        else:
                            hu='0'
                        cadena = cadena + numval(aux.derecha.x) + ',' + str(aux.derecha.y) + ',' + hu + "\n"
                        aux = aux.derecha
        #print('recorrido en y: ' + cadena)
        return cadena

class NodoDoble(object):
    def __init__(self,dato=None):
        self.dato=dato
        self.derecha=None
        self.izquierda=None

class ListaDoble(object):
    def __init__(self,inicio=None):
        self.inicio=inicio
    def insertar(self,dato):
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
            #print(nodo.dato)
            graf.node(str(nodo.derecha.dato))
            graf.edge(str(nodo.dato),str(nodo.derecha.dato))
            graf.edge(str(nodo.derecha.dato),str(nodo.dato))
            nodo = nodo.derecha
        #graf.render('doble.gv',cleanup=True)
        #graf.save('doble',"C:\\Users\\Abraham Jelkmann\\Desktop")
        return graf


class ArbolBinario(object):
    def __init__(self,raiz=None):
        self.raiz=raiz
    def insertar(self,dato=None):
        if self.raiz is None:
            self.raiz = NodoAbb(dato)
        else:
            self.insertarnodo(self.raiz,dato)
    def insertarnodo(self,nodo=None,dato=None):
        if nodo.izquierda is None and nodo.derecha is None:
            nod = NodoAbb(dato)
            if dato < nodo.dato:
                nodo.izquierda = nod
            else:
                nodo.derecha = nod
        else:
            if dato > nodo.dato:
                if nodo.derecha is not None:
                    self.insertarnodo(nodo.derecha,dato)
                else:
                    nod = NodoAbb(dato)
                    nodo.derecha = nod
            else:
                if nodo.izquierda is not None:
                    self.insertarnodo(nodo.izquierda,dato)
                else:
                    nod = NodoAbb(dato)
                    nodo.izquierda = nod
    def buscar(self,raiz,valor):
        if raiz is None:
            print('No existe')
            return None
        else:
            if valor.upper() == raiz.dato.nombre.upper():
                #print(str(raiz.dato) + ' existe')
                return raiz.dato
            elif valor.upper() < raiz.dato.nombre.upper():
                return self.buscar(raiz.izquierda,valor)
            else:
                return self.buscar(raiz.derecha,valor)

    def eliminar(self,raiz=None,valor=None):
        if(raiz is None):
            raise ValueError('No se ha encontrado el nodo')
        elif(valor < raiz.dato):
            iz = self.eliminar(raiz.izquierda,valor)
            raiz.izquierda = iz
        elif(valor > raiz.dato):
            der = self.eliminar(raiz.derecha,valor)
            raiz.derecha = der
        else:
            q = NodoAbb()
            q = raiz
            if(q.izquierda is None):
                raiz = q.derecha
            elif(q.derecha is None):
                raiz = q.izquierda
            else:
                q = self.reemplazar(q)
            q = None
        return raiz

    def reemplazar(self,act=None):
        p = act
        a = act.izquierda
        while(a.izquierda is not None):
            p = a
            a = a.derecha
        act.dato = a.dato
        if(p == act):
            p.izquierda = a.izquierda
        else:
            p.derecha = a.izquierda
        return a
    def graficar(self,raiz,contador,dot):
        if raiz is None:
            return
        #print (raiz.dato)
        dot.node(str(raiz.dato))
        #listas
        if (raiz.izquierda is not None):
            dot.node(str(raiz.izquierda.dato))
            dot.edge(str(raiz.dato),str(raiz.izquierda.dato))
        if(raiz.derecha is not None):
            dot.node(str(raiz.derecha.dato))
            dot.edge(str(raiz.dato),str(raiz.derecha.dato))
        contador+=1
        self.graficar(raiz.izquierda,contador,dot)
        self.graficar(raiz.derecha,contador,dot)
        return dot
    def graficarconlista(self,raiz,contador,dot):
        if raiz is None:
            return
        print (str(raiz.dato) + ' arbolconlista')
        dot.node(str(raiz.dato))
        if raiz.dato.lista is not None:
            li = raiz.dato.lista
            if li.inicio is not None:
                actual = li.inicio
                while actual.derecha is not None:
                    dot.node(str(actual.dato),shape='box')
                    #print(nodo.dato)
                    dot.node(str(actual.derecha.dato),shape='box')
                    dot.body.append('\t\t{rank=same;"' + str(actual.dato) + '" -> "' + str(actual.derecha.dato) + '";}')
                    dot.body.append('\t\t{rank=same;"' + str(actual.derecha.dato) + '" -> "' + str(actual.dato) + '";}')
                    actual = actual.derecha
                dot.body.append('\t\t{rank=same;"' + str(raiz.dato) + '" -> "' + str(li.inicio.dato) + '";}')
        if (raiz.izquierda is not None):
            #print (repr(raiz.izquierda.dato) + ' izquierda')
                #dot.body.append('\t\t{rank=same;"' + str(nodo.arriba.dato) + '" -> "' + str(nodo.dato) + '";}')
            dot.node(str(raiz.izquierda.dato))
            dot.edge(str(raiz.dato),str(raiz.izquierda.dato))
        if(raiz.derecha is not None):
            #print (repr(raiz.derecha.dato) + ' izquierda')
            dot.node(str(raiz.derecha.dato))
            dot.edge(str(raiz.dato),str(raiz.derecha.dato))
        contador+=1
        self.graficarconlista(raiz.izquierda,contador,dot)
        self.graficarconlista(raiz.derecha,contador,dot)
        return dot


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

class Disparo(object):
    def __init__(self,x,y,nivel,tipo,resultado,emisor,receptor,fecha,numero,tiempo=0):
        self.x = x
        self.y = y
        self.nivel = nivel
        self.tipo = tipo
        self.resultado = resultado
        self.emisor = emisor
        self.receptor = receptor
        self.fecha = fecha
        self.tiempo = tiempo
        self.numero = numero

tem = Tempo()

ar = ArbolBinario()
disparos = ListaDoble()
juegoactual = juego()

def revisarsegundos():
    tiempo = tem.final - time.time()
    revisar()
    return (tiempo)

def contar(tiempo):
    #tiempo = str(request.form['tiempo'])
    tem.inicio = time.time()
    tem.final = time.time() + int(tiempo)
    return 'iniciado'

def disparo(x,y,nivel,tipo,resultado,emisor,receptor,fecha,tiempo=0):
    if juegoactual.variante == 2:
        if juegoactual.disparos == 0:
            contar(juegoactual.tiempo)
    juegoactual.disparos += 1
    dis = Disparo(x,y,nivel,tipo,resultado,emisor,receptor,fecha,juegoactual.disparos,tiempo)
    disparos.insertar(dis)

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
        if us.nombre == juegoactual.jugador1:
            if us.nombre == juegoactual.turno:
                dis = ar.buscar(ar.raiz,juegoactual.jugador2)
                if nivel == '1':
                    nod = dis.cubo.satelites.buscar(posx,int(posy))
                    print('satelites: ' + posx + " , " +  posy)
                    if nod is not None:
                        if not nod.hundido:
                            us.acertados.satelites.insertar(posx,int(posy))
                            disparo(posx,int(posy),juegoactual.tipo_disparo,1,1,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today())
                            nod.hundido = True
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        us.fallados.satelites.insertar(posx,int(posy))
                        disparo(posx,int(posy),juegoactual.tipo_disparo,0,1,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today())
                        juegoactual.cambiarturno()
                        return 'fallo'
                elif nivel == '2':
                    nod = dis.cubo.aviones.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            disparo(posx,int(posy),juegoactual.tipo_disparo,1,2,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today())
                            us.acertados.aviones.insertar(posx,int(posy))
                            nod.hundido = True
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        us.fallados.aviones.insertar(posx,int(posy))
                        disparo(posx,int(posy),juegoactual.tipo_disparo,0,2,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today())
                        juegoactual.cambiarturno()
                        return 'fallo'
                elif nivel == '3':
                    nod = dis.cubo.barcos.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            disparo(posx,int(posy),juegoactual.tipo_disparo,1,3,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today())
                            us.acertados.barcos.insertar(posx,int(posy))
                            nod.hundido = True
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        disparo(posx,int(posy),juegoactual.tipo_disparo,0,3,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today())
                        us.fallados.barcos.insertar(posx,int(posy))
                        juegoactual.cambiarturno()
                        return 'fallo'
                elif nivel == '4':
                    nod = dis.cubo.submarinos.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            disparo(posx,int(posy),juegoactual.tipo_disparo,1,4,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today())
                            us.acertados.subamrinos.insertar(posx,int(posy))
                            nod.hundido = True
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        disparo(posx,int(posy),juegoactual.tipo_disparo,0,4,juegoactual.jugador1,juegoactual.jugador2,datetime.date.today())
                        us.fallados.submarinos.insertar(posx,int(posy))
                        juegoactual.cambiarturno()
                        return 'fallo'
                else:
                    return 'nivel incorrecto'
            else:
                return 'no es el turno del jugador'
        elif us.nombre == juegoactual.jugador2:
            if us.nombre == juegoactual.turno:
                dis = ar.buscar(ar.raiz,juegoactual.jugador1)
                if nivel == '1':
                    nod = dis.cubo.satelites.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            disparo(posx,int(posy),juegoactual.tipo_disparo,1,1,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today())
                            us.acertados.satelites.insertar(posx,int(posy))
                            nod.hundido = True
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        disparo(posx,int(posy),juegoactual.tipo_disparo,0,1,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today())
                        us.fallados.satelites.insertar(posx,int(posy))
                        juegoactual.cambiarturno()
                        return 'fallo'
                elif nivel == '2':
                    nod = dis.cubo.aviones.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            disparo(posx,int(posy),juegoactual.tipo_disparo,1,2,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today())
                            us.acertados.aviones.insertar(posx,int(posy))
                            nod.hundido = True
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        disparo(posx,int(posy),juegoactual.tipo_disparo,0,2,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today())
                        us.fallados.aviones.insertar(posx,int(posy))
                        juegoactual.cambiarturno()
                        return 'fallo'
                elif nivel == '3':
                    nod = dis.cubo.barcos.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            disparo(posx,int(posy),juegoactual.tipo_disparo,1,3,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today())
                            us.acertados.barcos.insertar(posx,int(posy))
                            nod.hundido = True
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        disparo(posx,int(posy),juegoactual.tipo_disparo,0,3,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today())
                        us.fallados.barcos.insertar(posx,int(posy))
                        juegoactual.cambiarturno()
                        return 'fallo'
                elif nivel == '4':
                    nod = dis.cubo.submarinos.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            disparo(posx,int(posy),juegoactual.tipo_disparo,1,4,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today())
                            us.acertados.submarinos.insertar(posx,int(posy))
                            nod.hundido = True
                            juegoactual.cambiarturno()
                            return 'exito'
                        else:
                            return 'nodo ya hundido'
                    else:
                        disparo(posx,int(posy),juegoactual.tipo_disparo,0,4,juegoactual.jugador2,juegoactual.jugador1,datetime.date.today())
                        us.fallados.submarinos.insertar(posx,int(posy))
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

@app.route('/')

@app.route('/tableros',methods=['POST'])
def tableros():
    nivel = str(request.form['nivel'])
    jugador = str(request.form['usuario'])
    u = ar.buscar(ar.raiz,jugador)
    if u is not None:
        if nivel == '1':
            return u.cubo.satelites.recorreref()
        elif nivel == '2':
            return u.cubo.aviones.recorreref()
        elif nivel == '3':
            return u.cubo.barcos.recorreref()
        elif nivel == '4':
            return u.cubo.submarinos.recorreref()
    else:
        return 'Error'

@app.route('/registrar',methods=['POST'])
def registrar():
    nombre = str(request.form['nombre'])
    contra = str(request.form['contra'])
    usuario = Usuario(nombre.strip(),contra.strip(),0)
    ar.insertar(usuario)
    return "True"

@app.route('/iniciar',methods=['POST'])
def iniciar():
    nombre = str(request.form['nombre'])
    contra = str(request.form['contra'])
    dato = ar.buscar(ar.raiz,nombre)
    print(dato.contrasena)
    if dato is not None:
        print(dato.contrasena.strip() + " = " + contra)
        if dato.contrasena == contra:
            return "True"
        else:
            return "False"
    else:
        return "False"

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
        print(nombre,contra,conectado)
        return "True"

    elif tipo == 'naves':
        jugador = str(request.form['jugador'])
        columna = str(request.form['columna'])
        fila = str(request.form['fila'])
        nivel = str(request.form['nivel'])
        modo = str(request.form['modo'])
        direccion = str(request.form['direccion'])

        usuario = ar.buscar(ar.raiz,jugador)
        if nivel == '1':
            s = Satelite()
            s.colocar(usuario.cubo.satelites,columna,int(fila))
            print('Satelite')
            return 'satelite'

        elif nivel == '2':
            a = Avion(int(modo))
            a.colocar(usuario.cubo.aviones,columna,int(fila))
            print('Avion')
            return 'Avion'

        elif nivel == '3':
            b = Barco(int(modo),int(direccion))
            b.colocar(usuario.cubo.barcos,columna,int(fila))
            print('Barco')
            return 'Barco'

        elif nivel == '4':
            sub = Submarino(int(modo),int(direccion))
            sub.colocar(usuario.cubo.submarinos,columna,int(fila))
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
        juegoactual.numerodisparos = numerodisparos
        juegoactual.disparos =0
        print('tiempo de juego: ' + tiempo + ' segundos')
        return 'juego creado'

@app.route('/jugar',methods=['POST'])

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
            us = ar.buscar(ar.raiz,nick)
            us.cubo.satelites.graficar(imagen)
            print('graficando satelites')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'barcos':
            us = ar.buscar(ar.raiz,nick)
            print('graficando barcos')
            us.cubo.barcos.graficar(imagen)
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'aviones':
            us = ar.buscar(ar.raiz,nick)
            us.cubo.aviones.graficar(imagen)
            print('graficando aviones')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'submarinos':
            us = ar.buscar(ar.raiz,nick)
            us.cubo.submarinos.graficar(imagen)
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
            us = ar.buscar(ar.raiz,nick)
            us.acertados.satelites.graficar(imagen)
            print('graficando satelites')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'barcos':
            us = ar.buscar(ar.raiz,nick)
            print('graficando barcos')
            us.acertados.barcos.graficar(imagen)
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'aviones':
            us = ar.buscar(ar.raiz,nick)
            us.acertados.aviones.graficar(imagen)
            print('graficando aviones')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'submarinos':
            us = ar.buscar(ar.raiz,nick)
            us.acertados.submarinos.graficar(imagen)
            print('graficando submarinos')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        return cadena
    elif nombre == 'fallados':
        if imagen == 'satelites':
            us = ar.buscar(ar.raiz,nick)
            us.fallados.satelites.graficar(imagen)
            print('graficando satelites')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'barcos':
            us = ar.buscar(ar.raiz,nick)
            print('graficando barcos')
            us.fallados.barcos.graficar(imagen)
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'aviones':
            us = ar.buscar(ar.raiz,nick)
            us.fallados.aviones.graficar(imagen)
            print('graficando aviones')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'submarinos':
            us = ar.buscar(ar.raiz,nick)
            us.fallados.submarinos.graficar(imagen)
            print('graficando submarinos')
            with open("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        return cadena
    else:
        return 'error'

#@app.route('/')


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

"""
lista = ListaDoble()
lista.insertar(5)
lista.insertar(10)
lista.insertar(8)
lista.graficar()
"""

"""
ar.insertar('Abraham Jelkmann')
ar.insertar('Alejandro')
ar.insertar('Alma')
ar.insertar('Pablo')
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
