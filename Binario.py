

class NodoAbb(object):
    def __init__(self,dato=None):
        self.dato=dato
        self.izquierda=None
        self.derecha=None

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
    
