from graphviz import Digraph

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
