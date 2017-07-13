from graphviz import Digraph

class NodoAvl(object):
    def __init__(self,dato=None,padre=None):
        self.dato=dato
        self.balance=0
        self.altura=0
        self.derecha=None
        self.izquierda=None
        self.padre=padre

class AVL(object):
    def __init__(self,raiz=None):
        self.raiz=raiz

    def insertar(self,dato):
        if self.raiz is None:
            self.raiz = NodoAvl(dato)
        else:
            n = self.raiz
            padre = NodoAvl()
            while(True):
                if(n.dato==dato):
                    return False
                padre = n
                izquierda = n.dato > dato
                n = n.izquierda if izquierda else n.derecha
                if n is None:
                    if izquierda:
                        padre.izquierda = NodoAvl(dato,padre)
                    else:
                        padre.derecha = NodoAvl(dato,padre)
                    self.rebalancear(padre)
                    break
        return True

    def eliminarnodo(self,nodo):
        if(nodo.izquierda is None and nodo.derecha is None):
            if(nodo.padre is None): self.raiz=None
            else:
                padre = nodo.padre
                if(padre.izquierda == nodo):
                    padre.izquierda = None
                else:
                    padre.derecha = None
                self.rebalancear(padre)
            return
        if nodo.izquierda is not None:
            hijo = nodo.izquierda
            while(hijo.derecha is not None): hijo = hijo.derecha
            nodo.dato = hijo.dato
            self.eliminar(hijo)
        else:
            hijo = nodo.derecha
            while(hijo.izquierda is not None): hijo = hijo.izquierda
            nodo.dato = hijo.dato
            self.eliminar(hijo)

    def eliminar(self,dato):
        if self.raiz is None:
            return
        nodo = self.raiz
        hijo = self.raiz
        while(hijo is not None):
            nodo = hijo
            hijo =  nodo.derecha if dato >= nodo.dato else nodo.izquierda
            if(dato == nodo.dato):
                self.eliminar(nodo)
                return

    def rebalancear(self,nodo):
        self.estbalance(nodo)
        if nodo.balance == -2:
            if(self.altura(nodo.izquierda.izquierda) >= self.altura(nodo.izquierda.derecha)):
                nodo = self.rotDer(nodo)
            else:
                nodo = self.rotIzDer(nodo)
        elif nodo.balance == 2:
            if(self.altura(nodo.derecha.derecha) >= self.altura(nodo.derecha.izquierda)):
                nodo = self.rotIz(nodo)
            else:
                nodo = self.rotDerIz(nodo)

        if nodo.padre is not None:
            self.rebalancear(nodo.padre)
        else:
            self.raiz = nodo

    def rotIz(self,nodo):
        b = nodo.derecha
        b.padre = nodo.padre
        nodo.derecha = b.izquierda
        if nodo.derecha is not None:
            nodo.derecha.padre = nodo
        b.izquierda = nodo
        nodo.padre = b
        if b.padre is not None:
            if b.padre.derecha == nodo:
                b.padre.derecha = b
            else:
                b.padre.izquierda = b
        self.estbalance(nodo,b)
        return b

    def rotDer(self,nodo):
        b = nodo.izquierda
        b.padre = nodo.padre
        nodo.izquierda = b.derecha
        if nodo.izquierda is not None:
            nodo.izquierda.padre = nodo
        b.derecha = nodo
        nodo.padre = b
        if b.padre is not None:
            if b.padre.derecha == nodo:
                b.padre.derecha = b
            else:
                b.padre.izquierda = b
        self.estbalance(nodo,b)
        return b

    def rotIzDer(self,nodo):
        nodo.izquierda = self.rotIz(nodo.izquierda)
        return rotDer(nodo)

    def rotDerIz(self,nodo):
        nodo.derecha = rotDer(nodo.derecha)
        return rotIz(nodo)

    def altura(self,nodo):
        if nodo is None:
            return -1
        return nodo.altura

    def estbalance(self,*nodos):
        for n in nodos:
            self.realt(n)
            n.balance = self.altura(n.derecha) - self.altura(n.izquierda)

    def realt(self,nodo):
        if nodo is not None:
            nodo.altura = 1 + max(self.altura(nodo.izquierda),self.altura(nodo.derecha))

    def graf(self,raiz,dot):
        if raiz is None:
            return
        dot.node(str(raiz.dato))
        if (raiz.izquierda is not None):
            dot.node(str(raiz.izquierda.dato))
            dot.edge(str(raiz.dato),str(raiz.izquierda.dato))
        if(raiz.derecha is not None):
            dot.node(str(raiz.derecha.dato))
            dot.edge(str(raiz.dato),str(raiz.derecha.dato))
        #contador+=1
        self.graf(raiz.izquierda,dot)
        self.graf(raiz.derecha,dot)
        return dot

    def graficar(self,imagen):
        dot = Digraph(comment='AVL',format='png')
        self.graf(self.raiz,dot)
        dot.render("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen,cleanup=True)
        dot.save(imagen,r"C:\\Users\\Abraham Jelkmann\\Desktop")
    #arreglar y agregar metodo para editar
    def buscar(self,raiz,valor):
        if raiz is None:
            print('No existe')
            return None
        else:
            if valor == raiz.dato:
                print(str(raiz.dato) + ' existe')
                return raiz
            elif valor < raiz.dato:
                return self.buscar(raiz.izquierda,valor)
            else:
                return self.buscar(raiz.derecha,valor)
    def editar(self,valor,nuevo):
        dat = self.buscar(self.raiz,valor)
        if dat is not None:
            dat.dato = nuevo
            print("el dato ha sido cambiado")
            return "el dato ha sido cambiado"
        else:
            print("el dato no existe")
            return "el dato no existe"


arbol = AVL()
arbol.insertar(1)
arbol.insertar(2)
arbol.insertar(3)
arbol.insertar(4)
arbol.insertar(5)
arbol.insertar(6)
arbol.insertar(7)
arbol.insertar(8)
arbol.insertar(9)
arbol.buscar(arbol.raiz,9)
arbol.buscar(arbol.raiz,1)
arbol.buscar(arbol.raiz,4)
arbol.buscar(arbol.raiz,6)
arbol.buscar(arbol.raiz,15)
arbol.graficar('avl')
