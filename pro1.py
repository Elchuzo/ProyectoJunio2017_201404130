from flask import Flask, request, Response
from graphviz import Digraph
app = Flask("Proyecto")


class nave(object):
    def __init__(self,espacios=0):
        self.espacios=espacios

class tablero(object):
    def __init__(self,niveles=0,tiros=None):
        self.niveles=niveles
        self.tiros=tiros

class juego(object):
    def __init__(self,naves=0,tipo_disparo=None,dimension=None,variante=None):
        self.naves=naves
        self.tipo_disparo=tipo_disparo
        self.dimension=dimension
        self.variante=variante

class usuario(object):
    def __init__(object,nombre=None,contrasena=None,conectado=False,lista_juegos=None):
        self.nombre=nombre
        self.contrasena=contrasena
        self.conectado=conectado
        self.lista_juegos=lista_juegos

class partida(object):
    def __init__(object,oponente=None,tiros=0,acertados=0,fallados=0,resultado=None,danio=0):
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
        self.x=0
        self.y=0

class MatrizDispersa(object):
    def __init__(self):
        self.cabeza=NodoMatriz()
    def insertar(self,dato,x,y):
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
                    horizontal = true
                    break
                elif actual.derecha.x < x:
                    actual = actual.derecha
        if not horizontal:
            #print('añadiendo nodo derecha')
            if actual.derecha is not None:
                actual.derecha.izquierda = nodox
                nodox.derecha = actual.derecha
            nodox.izquierda = actual
            actual.derecha = nodox
            horizontal=True
        else:
            #print('añadiendo primer nodo arriba')
            self.cabeza.derecha = nodox
            nodox.izquierda = self.cabeza
        actual = self.cabeza
        if self.cabeza.abajo is not None:
            while actual.abajo is not None:
                if actual.abajo.y == y:
                    vertical = true
                    break
                elif actual.abajo.y < y:
                    actual = actual.abajo
        if  not vertical:
            #print('añadiendo nodo abajo')
            if actual.abajo is not None:
                actual.abajo.arriba = nodoy
                nodoy.abajo = actual.abajo
            nodoy.arriba = actual
            actual.abajo = nodoy
            vertical=True
        else:
            print('añadiendo primer nodo abajo')
            self.cabeza.abajo = nodoy
            nodoy.arriba = self.cabeza
        actual = self.cabeza
        #print('nodo actual: ' + str(actual.x) + str(actual.y))
        #print('nodo a ingresar: ' + str(nodoin.x) + str(nodoin.y))
        while actual.x != nodoin.x:
            if actual.derecha is not None:
                actual = actual.derecha
                print(str(actual.x)+ ' = ' + str(nodoin.x))
            else:
                break
        if actual.abajo is not None:
            if actual.abajo.y < nodoin.y:
                while actual.abajo.y < nodoin.y:
                    actual = actual.abajo
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
        actual = self.cabeza

        while actual.y != nodoin.y:
            if actual.abajo is not None:
                actual = actual.abajo
            else:
                break
        if actual.derecha is not None:
            while actual.derecha.x < nodoin.x:
                actual = actual.derecha
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

    def graficar(self):
        actual = self.cabeza
        matriz = Digraph(comment='Matriz')
        contador = 0
        terminado = False
        matriz.attr('node',shape='box')
        matriz.attr('graph',rankdir='LR')
        matriz.node(str(actual.dato))
        while (not terminado):
            nodo = actual
            print('dato actual: '+str(nodo.dato))
            while nodo.derecha is not None:
                print('graficando derecha')
                matriz.node(str(nodo.derecha.dato))
                matriz.edge(str(nodo.dato),str(nodo.derecha.dato))
                matriz.edge(str(nodo.derecha.dato),str(nodo.dato))
                if nodo.arriba is not None:
                    print('graficando abajo')
                #    matriz.node(str(nodo.dato))
                    matriz.edge(str(nodo.dato),str(nodo.arriba.dato), constraint='false')
                    matriz.body.append('\t\t{rank=same;"' + str(nodo.arriba.dato) + '" -> "' + str(nodo.dato) + '";}')
                nodo = nodo.derecha

            if nodo.arriba is not None:
                print('graficando abajo')
            #    matriz.node(str(nodo.dato))
                matriz.edge(str(nodo.dato),str(nodo.arriba.dato), constraint='false')
                matriz.body.append('\t\t{rank=same;"' + str(nodo.arriba.dato) + '" -> "' + str(nodo.dato) + '";}')


            if actual.abajo is not None:
                    actual = actual.abajo
            else:
                terminado = True
        print(matriz.source)
        matriz.render('matriz.gv',cleanup=True)
        matriz.save('matriz.gv',"C:\\Users\\Oscar\\Desktop")



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
        graf.render('doble.gv',cleanup=True)
        graf.save('doble.gv',"C:\\Users\\Oscar\\Desktop")



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
    def buscar(self,raiz,dato):
        if raiz is None:
            print('No existe')
        else:
            if dato == raiz.dato:
                print(dato + 'existe')
                return dato
            elif clave <raiz.dato:
                return buscar(raiz.izquierda,dato)
            else:
                return buscar(raiz.derecha,dato)

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



def prebinario(raiz,contador):
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
    prebinario(raiz.izquierda,contador)
    prebinario(raiz.derecha,contador)

@app.route('/parametros',methods=['POST'])
def parametros():
    return ('10,6')


#if __name__ == "__main__":
#  app.run(debug=True, host='0.0.0.0')

"""
lista = ListaDoble()
lista.insertar(5)
lista.insertar(10)
lista.insertar(8)
lista.graficar()
"""

dot = Digraph(comment='Prueba')

ar = ArbolBinario()
"""
ar.insertar(10)
ar.insertar(20)
ar.insertar(5)
ar.insertar(4)
ar.insertar(8)
ar.insertar(15)
ar.insertar(11)
ar.insertar(6)
ar.insertar(32)
ar.insertar(7)
ar.insertar(9)
"""
"""
ar.insertar('Oscar')
ar.insertar('Alejandro')
ar.insertar('Andrea')
ar.insertar('Nicte')
ar.insertar('Alma')
ar.insertar('Pablo')
"""

mat = MatrizDispersa()
mat.insertar(5,2,2)
mat.insertar(8,3,5)
mat.graficar()

print('preorder')
prebinario(ar.raiz,0)
print('')

dot.render('prueba.gv',cleanup=True)
dot.save('prueba.gv',"C:\\Users\\Oscar\\Desktop")
