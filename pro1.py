from flask import Flask, request, Response
from graphviz import Digraph
import base64
import threading
import time
from threading import Timer
import math
app = Flask("Proyecto")


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

class tablero(object):
    def __init__(self,niveles=0,tiros=None):
        self.niveles=niveles
        self.tiros=tiros

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
    def __lt__(self,other):
        return (self.nombre.lower() < other.nombre.lower())
    def __eq__(self,other):
        return(self.nombre.lower() == other.nombre.lower())
    def __gt__(self,other):
        return(self.nombre.lower() > other.nombre.lower())
    def __str__(self):
        return self.nombre

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
    def __init__(self,object,oponente=None,tiros=0,acertados=0,fallados=0,resultado=None,danio=0):
        self.oponente=oponente
        self.tiros=tiros
        self.acertados=acertados
        self.fallados=fallados
        self.resultado=resultado
        self.danio=danio

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
        matriz.render(imagen,cleanup=True)
        matriz.save(imagen,"C:\\Users\\Oscar\\Desktop")

    def buscar(self,x,y):
        horizontal = False
        vertical = False
        actual = self.cabeza
        if self.cabeza is not None:
            while actual.derecha is not None:
                print(actual.derecha.x + " = " + x)
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
                print(str(actual.derecha.y) + " = " + str(y))
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
            print(nodo.dato)
            graf.node(str(nodo.derecha.dato))
            graf.edge(str(nodo.dato),str(nodo.derecha.dato))
            graf.edge(str(nodo.derecha.dato),str(nodo.dato))
            nodo = nodo.derecha
        #graf.render('doble.gv',cleanup=True)
        #graf.save('doble',"C:\\Users\\Oscar\\Desktop")
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
            if valor == raiz.dato.nombre:
                print(str(raiz.dato) + ' existe')
                return raiz.dato
            elif valor < raiz.dato.nombre:
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
        print (raiz.dato)
        if (raiz.izquierda is not None):
            dot.node(str(raiz.dato))
            dot.node(str(raiz.izquierda.dato))
            dot.edge(str(raiz.dato),str(raiz.izquierda.dato))
        if(raiz.derecha is not None):
            dot.node(str(raiz.dato))
            dot.node(str(raiz.derecha.dato))
            dot.edge(str(raiz.dato),str(raiz.derecha.dato))
        contador+=1
        self.graficar(raiz.izquierda,contador,dot)
        self.graficar(raiz.derecha,contador,dot)
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

tem = Tempo()

ar = ArbolBinario()

juegoactual = juego()

@app.route('/disparar',methods=['POST'])
def disparar():
    jugador = str(request.form['jugador'])
    nivel = str(request.form['nivel'])
    posx = str(request.form['posx'])
    posy = str(request.form['posy'])
    us = ar.buscar(ar.raiz,jugador)
    print('entro')
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
                            nod.hundido = True
                            return 'exito'
                        else:
                            return 'nodo ya hunido'
                    else:
                        return 'fallo'
                elif nivel == '2':
                    nod = dis.cubo.aviones.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            nod.hundido = True
                            return 'exito'
                        else:
                            return 'nodo ya hunido'
                    else:
                        return 'fallo'
                elif nivel == '3':
                    nod = dis.cubo.barcos.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            nod.hundido = True
                            return 'exito'
                        else:
                            return 'nodo ya hunido'
                    else:
                        return 'fallo'
                elif nivel == '4':
                    nod = dis.cubo.submarinos.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            nod.hundido = True
                            return 'exito'
                        else:
                            return 'nodo ya hunido'
                    else:
                        return 'fallo'
                else:
                    return 'nivel incorrecto'
            else:
                return 'no es el turno del jugador'
        elif us.nombre == juegoactual.jugador2:
            if us.nombre == juegoactual.turno:
                dis = ar.buscar(ar.raiz,juegoactual.jugador1)
                if nivel == '1':
                    nod = dis.satelites.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            nod.hundido = True
                            return 'exito'
                        else:
                            return 'nodo ya hunido'
                    else:
                        return 'fallo'
                elif nivel == '2':
                    nod = dis.cubo.aviones.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            nod.hundido = True
                            return 'exito'
                        else:
                            return 'nodo ya hunido'
                    else:
                        return 'fallo'
                elif nivel == '3':
                    nod = dis.cubo.barcos.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            nod.hundido = True
                            return 'exito'
                        else:
                            return 'nodo ya hunido'
                    else:
                        return 'fallo'
                elif nivel == '4':
                    nod = dis.cubo.submarinos.buscar(posx,int(posy))
                    if nod is not None:
                        if not nod.hundido:
                            nod.hundido = True
                            return 'exito'
                        else:
                            return 'nodo ya hunido'
                    else:
                        return 'fallo'
                else:
                    return 'nivel incorrecto'
            else:
                return 'No es el turno del jugador'
        else:
            return 'El jugador no esta en la partida'
    else:
        return'error'

@app.route('/contar',methods=['POST'])
def contar():
    tiempo = str(request.form['tiempo'])
    tem.inicio = time.time()
    tem.final = time.time() + int(tiempo)
    inicio = time.time()
    fin = inicio + int(tiempo)
    return 'iniciado'

@app.route('/revisar',methods=['POST'])
def revisar():
    tiempo = tem.final - time.time()
    t = divmod(tiempo,60)
    dec, segundos = math.modf(t[1])
    print ('minutos: ' + str(t[0]) + ' segundos: ' + str(segundos))
    return ('hola')

@app.route('/parametros',methods=['POST'])
def parametros():
    x = juegoactual.x
    y = juegoactual.y
    cadena = str(x) + "," + str(y)
    return (cadena)

@app.route('/registrar',methods=['POST'])
def registrar():
    nombre = str(request.form['nombre'])
    contra = str(request.form['contra'])
    usuario = Usuario(nombre,contra,0)
    ar.insertar(usuario)
    return "True"

@app.route('/iniciar',methods=['POST'])
def iniciar():
    nombre = str(request.form['nombre'])
    contra = str(request.form['contra'])
    dato = ar.buscar(ar.raiz,nombre)
    if dato is not None:
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
        u = Usuario(nombre,contra,int(conectado))
        ar.insertar(u)
        print(nombre,contra,conectado)
        return nombre
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
        return 'juego creado'

@app.route('/jugar',methods=['POST'])

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
            with open("C:\\Users\\Oscar\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'barcos':
            us = ar.buscar(ar.raiz,nick)
            print('graficando barcos')
            us.cubo.barcos.graficar(imagen)
            with open("C:\\Users\\Oscar\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'aviones':
            us = ar.buscar(ar.raiz,nick)
            us.cubo.aviones.graficar(imagen)
            print('graficando aviones')
            with open("C:\\Users\\Oscar\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
        elif imagen == 'submarinos':
            us = ar.buscar(ar.raiz,nick)
            us.cubo.submarinos.graficar(imagen)
            print('graficando submarinos')
            with open("C:\\Users\\Oscar\\Desktop\\"+imagen+".png",'rb') as imageFile:
                cadena = base64.b64encode(imageFile.read())
    elif nombre == 'arbol':
        dot = Digraph(comment='Prueba',format='png')
        dot = ar.graficar(ar.raiz,0,dot)
        dot.render('prueba',cleanup=True)
        dot.save('prueba',r"C:\\Users\\Oscar\\Desktop")
        with open("C:\\Users\\Oscar\\Desktop\\prueba.png",'rb') as imageFile:
            cadena = base64.b64encode(imageFile.read())
    return cadena

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
ar.insertar('Oscar')
ar.insertar('Alejandro')
ar.insertar('Alma')
ar.insertar('Pablo')
"""

sat = Satelite()
bar = Barco(2,1)
"""
mat = MatrizDispersa()
mat.insertar('A',2)
mat.insertar('B',5)
mat.insertar('C',8)
sat.colocar(mat,'G',5)
bar.colocar(mat,'H',10)
mat.graficar()
"""
