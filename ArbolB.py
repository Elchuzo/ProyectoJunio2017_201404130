from graphviz import Digraph

#clase para pruebas
class Dato(object):
    def __init__(self,numero,x):
        self.x=x
        self.numero=numero
    def __str__(self):
        a = '  x:  ' + str(self.x)
        b = '  n:  ' + str(self.numero)
        cadena = a + " \n " + b
        return cadena
    def __eq__(self,other):
        return (self.x == other.x)
    def __lt__(self,other):
        return(self.x < other.x)
    def __gt__(self,other):
        return(self.x > other.x)

class ArbolB(object):
    def __init__(self):
        self.raiz = VectorB()

    def insertar(self,raiz,dato):
        #print('Insertando: ' + str(dato))
        if raiz.tiene_hijos():
            actual = raiz.p0
            while dato > actual.dato and actual.siguiente.dato is not None:
                actual = actual.siguiente
            if dato < actual.dato:
                self.insertar(actual.izquierda,dato)
            else:
                self.insertar(actual.derecha,dato)
            pass
        else:
            raiz.insertar(dato)
            if raiz.cantidad_datos() == 5: # El vector ya está lleno, se debe separar
                if raiz.padre is not None: # Si tiene padre, se debe insertar el valor medio al padre

                    self.insertararriba(raiz,raiz.padre.vector,raiz.p2.dato)

                else:                       # Si no tiene padre, se crea una nueva raiz
                    vraiz = VectorB()               # Inicializar vraiz
                    vraiz.insertar(raiz.p2.dato) # Insertar el dato medio(p2) en la nueva raiz

                    vizquierda = VectorB()            # Crear el hijo izquierdo de la nueva raiz
                    vizquierda.insertar(raiz.p0.dato) # Ingresar los valores del vector izquierdo
                    vizquierda.insertar(raiz.p1.dato)

                    vderecha = VectorB()               # Crear el hijo derecho de la nueva raiz
                    vderecha.insertar(raiz.p3.dato)   # Ingresar los valores del vector derecho
                    vderecha.insertar(raiz.p4.dato)

                    raiz.cambiar(vraiz)              # Asignar la nueva raiz
                    raiz.p0.setIzquierda(vizquierda) # Asignar hijos derechos e izquierdos
                    raiz.p0.setDerecha(vderecha)
                    # Asignar padres a los hijos creados
                    vizquierda.padre = raiz.p0
                    vderecha.padre = raiz.p0
                    # Pruebas, eliminar después
                    #raiz.imprimir()
                    #vizquierda.imprimir()
                    #vderecha.imprimir()
                    print("La raiz se ha separado") # raiz es un VectorB

    def insertararriba(self,raiz,padre,dato): # raiz es un VectorB

        padre.insertar(dato) # Agregar el dato al padre

        vizquierda = VectorB() # Crear el vector que será agregado a la izquierda del dato ingresado al padre
        vizquierda.insertar(raiz.p0.dato)
        vizquierda.insertar(raiz.p1.dato)

        vderecha = VectorB() # Crear el vector que será agregado a la derecha del dato ingresado al padre
        vderecha.insertar(raiz.p3.dato)
        vderecha.insertar(raiz.p4.dato)

        vizquierda.p0.setIzquierda(raiz.p0.izquierda)
        vizquierda.p1.setIzquierda(raiz.p1.izquierda)
        vizquierda.p1.setDerecha(raiz.p1.derecha)

        vderecha.p0.setIzquierda(raiz.p3.izquierda)
        vderecha.p1.setIzquierda(raiz.p4.izquierda)
        vderecha.p1.setDerecha(raiz.p4.derecha)

        nod = padre.buscar(dato) # nod es el nodo que contiene el dato que ingresamos al inicio al padre

        nod.setIzquierda(vizquierda) # Asignar hijos al dato ingresado
        nod.setDerecha(vderecha)

        vizquierda.padre = nod
        vderecha.padre = nod

        if padre.cantidad_datos() == 5:
            if padre.padre is not None:
                self.insertararriba(padre,padre.padre.vector,padre.p2.dato)
            else:
                vraiz = VectorB()
                vraiz.insertar(padre.p2.dato)

                vizquierda = VectorB()
                vizquierda.insertar(padre.p0.dato)
                vizquierda.insertar(padre.p1.dato)

                vderecha = VectorB()
                vderecha.insertar(padre.p3.dato)
                vderecha.insertar(padre.p4.dato)

                vizquierda.p0.setIzquierda(padre.p0.izquierda)
                vizquierda.p1.setIzquierda(padre.p1.izquierda)
                vizquierda.p1.setDerecha(padre.p1.derecha)

                vderecha.p0.setIzquierda(padre.p3.izquierda)
                vderecha.p1.setIzquierda(padre.p4.izquierda)
                vderecha.p1.setDerecha(padre.p4.derecha)

                padre.p0.izquierda.padre = vizquierda.p0
                padre.p1.izquierda.padre = vizquierda.p1
                padre.p2.izquierda.padre = vizquierda.p1

                padre.p3.izquierda.padre = vderecha.p0
                padre.p4.izquierda.padre = vderecha.p1
                padre.p4.derecha.padre = vderecha.p1

                #asignar de nuevo los padres de los hijos de los nuevos vectores creados (vizquierda y vderecha)

                padre.cambiar(vraiz)

                padre.p0.setIzquierda(vizquierda)
                padre.p0.setDerecha(vderecha)

                vizquierda.padre = padre.p0
                vderecha.padre = padre.p0

    def recorrer(self,raiz,dot,contador):
        raiz.imprimir()

        if raiz.cantidad_datos() == 1:
            dot.body.append('node'+str(contador)+'[label = "<f0>|'+str(raiz.p0.dato)+'|<f1>"];')
        elif raiz.cantidad_datos() == 2:
            dot.body.append('node'+str(contador)+'[label = "<f0> |' + str(raiz.p0.dato) + '|<f1> |' + str(raiz.p1.dato) + '|<f2>"];')
        elif raiz.cantidad_datos() == 3:
            dot.body.append('node'+str(contador)+'[label = "<f0> |' + str(raiz.p0.dato) + '|<f1> |' + str(raiz.p1.dato) + '|<f2> |' + str(raiz.p2.dato) + '|<f3>"];')
        elif raiz.cantidad_datos() == 4:
            dot.body.append('node'+str(contador)+'[label = "<f0> |' + str(raiz.p0.dato) + '|<f1> |' + str(raiz.p1.dato) + '|<f2> |' + str(raiz.p2.dato) + '|<f3>|' + str(raiz.p3.dato) + '|<f4>"];')
        #print(str(contador))
        contador+=1
        #if raiz.padre is not None: # Pruebas para verificar que el padre es el correcto
            #print('padre: ')
            #raiz.padre.vector.imprimir()
        if raiz.tiene_hijos():
            if raiz.cantidad_datos() == 1:

                n=self.recorrer(raiz.p0.izquierda,dot,contador)
                #print(n)
                dot.body.append('"node'+str(contador-1)+'":f0 -> "node'+str(contador)+'"')
                self.recorrer(raiz.p0.derecha,dot,n)
                #print(contador)
                dot.body.append('"node'+str(contador-1)+'":f1 -> "node'+str(n)+'"')

            elif raiz.cantidad_datos() == 2:
                print(contador)
                if contador == 1: # reorganizar los parametros para que la raiz no se arruine
                    n=self.recorrer(raiz.p0.izquierda,dot,contador)
                    dot.body.append('"node'+str(contador-1)+'":f0 -> "node'+str(contador)+'"')
                    m=self.recorrer(raiz.p0.derecha,dot,n)
                    dot.body.append('"node'+str(contador-1)+'":f1 -> "node'+str(n)+'"')
                    self.recorrer(raiz.p1.derecha,dot,m)
                    dot.body.append('"node'+str(contador-1)+'":f2 -> "node'+str(m)+'"')
                else:
                    n=self.recorrer(raiz.p0.izquierda,dot,contador)
                    dot.body.append('"node'+str(contador-1)+'":f0 -> "node'+str(contador)+'"')
                    n=self.recorrer(raiz.p0.derecha,dot,n)
                    dot.body.append('"node'+str(contador-1)+'":f1 -> "node'+str(n-1)+'"')
                    n=self.recorrer(raiz.p1.derecha,dot,n)
                    dot.body.append('"node'+str(contador-1)+'":f2 -> "node'+str(n-1)+'"')

            elif raiz.cantidad_datos() == 3:
                n=self.recorrer(raiz.p0.izquierda,dot,contador)
                dot.body.append('"node'+str(contador-1)+'":f0 -> "node'+str(contador)+'"')
                n=self.recorrer(raiz.p0.derecha,dot,n)
                dot.body.append('"node'+str(contador-1)+'":f1 -> "node'+str(n-1)+'"')
                n=self.recorrer(raiz.p1.derecha,dot,n)
                dot.body.append('"node'+str(contador-1)+'":f2 -> "node'+str(n-1)+'"')
                n=self.recorrer(raiz.p2.derecha,dot,n)
                dot.body.append('"node'+str(contador-1)+'":f3 -> "node'+str(n-1)+'"')
            elif raiz.cantidad_datos() == 4:
                n=self.recorrer(raiz.p0.izquierda,dot,contador)
                dot.body.append('"node'+str(contador-1)+'":f0 -> "node'+str(contador)+'"')
                n=self.recorrer(raiz.p0.derecha,dot,n)
                dot.body.append('"node'+str(contador-1)+'":f1 -> "node'+str(n-1)+'"')
                n=self.recorrer(raiz.p1.derecha,dot,n)
                dot.body.append('"node'+str(contador-1)+'":f2 -> "node'+str(n-1)+'"')
                n=self.recorrer(raiz.p2.derecha,dot,n)
                dot.body.append('"node'+str(contador-1)+'":f3 -> "node'+str(n-1)+'"')
                n=self.recorrer(raiz.p3.derecha,dot,n)
                dot.body.append('"node'+str(contador-1)+'":f4 -> "node'+str(n-1)+'"')
            return n
        else:
            return contador

    def buscar(self):
        pass #implementar busqueda

    def eliminar(self):
        pass # (algún día)

    def graf(self,imagen):
        dot = Digraph(comment='ArbolB',format='png')
        dot.body.append('node [shape = record,height=.1];')
        self.recorrer(self.raiz,dot,0)
        dot.render("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen,cleanup=True)
        dot.save(imagen,r"C:\\Users\\Abraham Jelkmann\\Desktop")


class VectorB(object):

    def __init__(self,size=4):
        self.size = size
        #Definir todos los nodos del vector al ser iniciado
        self.p4 = NodoVector('p4')
        self.p3 = NodoVector('p3',self.p4,self)
        self.p2 = NodoVector('p2',self.p3,self)
        self.p1 =  NodoVector('p1',self.p2,self)
        self.p0 = NodoVector('p0',self.p1,self)
        self.p4.vector = self
        #Asignar punteros a los nodos anteriores para simular una lista doble
        #(facilita las inserciones)
        self.p1.anterior = self.p0
        self.p2.anterior = self.p1
        self.p3.anterior = self.p2
        self.p4.anterior = self.p3
        self.padre=None

    def insertar(self,dato):
        insertado = False
        if self.cantidad_datos() == 0:
            self.p0.dato = dato
            insertado = True
            #return print((str(dato) + ' ha sido ingresado'))
        if self.cantidad_datos() < 5: # Al tener 5 datos se debe separar el vector
            actual = self.p0
            while not insertado:

                if dato < actual.dato:
                    self.corrernodos(actual)
                    actual.dato = dato
                    insertado = True
            #        return print((str(dato) + ' ha sido ingresado'))
                while (dato > actual.dato):
                    if actual.siguiente.dato is not None:
                        actual = actual.siguiente
                    else:
                        actual.siguiente.dato = dato
                        insertado = True
                        #return print((str(dato) + ' ha sido ingresado'))

    #que no quede huella que no y que no

    def corrernodos(self,actual=None): #Metodo para desplazar los nodos
        final = self.p4
        while final.dato is None:
            final = final.anterior
        while final != actual:
            final.siguiente.dato = final.dato # Correr el dato del nodo una posición a la izquierda
            final.siguiente.izquierda = final.izquierda # Asignar los hijos derechos e izquierdos del nodo una posición a la izquierda
            final.siguiente.derecha = final.derecha
            if final.izquierda is not None:
                final.izquierda.padre = final.siguiente # Cambiar los padres de los hijos
                final.derecha.padre = final.siguiente

            final.dato = final.anterior.dato # Correr el dato anterior al nodo actual a la posición del nodo actual
            final.izquierda = final.anterior.izquierda # Asignar los hijos derechos e izquierdos a la posicion del nodo actual
            final.derecha = final.anterior.derecha

            if final.anterior.izquierda is not None:
                final.anterior.izquierda.padre = final
                final.anterior.derecha.padre = final

            final = final.anterior
        # El código se debe ejecutar una vez más (se puede optimizar pero no quiero pensar)
        final.siguiente.dato = final.dato
        final.siguiente.izquierda = final.izquierda
        final.siguiente.derecha = final.derecha
        if final.izquierda is not None:
            final.izquierda.padre = final.siguiente # Cambiar los padres de los hijos
            final.derecha.padre = final.siguiente
        if final.anterior is not None:
            final.dato = final.anterior.dato
            final.izquierda = final.anterior.izquierda # (Optimizable)
            final.derecha = final.anterior.derecha
            if final.anterior.izquierda is not None:
                final.anterior.izquierda.padre = final
                final.anterior.derecha.padre = final

    def cantidad_datos(self): #Retorna la cantidad de datos no nulos en el vector
        cantidad = 0
        if self.p0.dato is not None:
            cantidad += 1
        if self.p1.dato is not None:
            cantidad += 1
        if self.p2.dato is not None:
            cantidad += 1
        if self.p3.dato is not None:
            cantidad += 1
        if self.p4.dato is not None:
            cantidad += 1
        return cantidad
        #que no quede huella de ti

    def imprimir(self):
        #print('voy a imprimir')
        actual = self.p0
        cadena = '| '
        if actual.dato is not None:
        #    print(actual.dato)
            cadena = cadena + str(actual.dato)
        while(actual.siguiente.dato is not None):
            actual = actual.siguiente
        #    print(actual.dato)
            cadena = cadena + " | " + str(actual.dato)
            if actual.siguiente is None:
                break
        print('el vector es: ' + cadena + ' |')

    def tiene_hijos(self):
        if self.p0.izquierda is not None or self.p0.derecha is not None:
            return True
        else:
            return False

    def cambiar(self,vector): #Metodo para cambiar los datos de un vector
        self.p4.dato=None
        self.p3.dato=None
        self.p2.dato=None
        self.p1.dato=None
        self.p0.dato = vector.p0.dato
        #codigo

    def buscar(self,valor):
        actual = self.p0
        if actual.dato == valor:
            return actual
        while actual.dato != valor and actual.siguiente is not None:
            actual = actual.siguiente
            if actual.dato == valor:
                return actual
        print('No se econtró el dato')
        return ('No se encontró el dato')



class NodoVector(object):
    def __init__(self,nombre=None,siguiente=None,vector=None,anterior=None,dato=None,derecha=None,izquierda=None):
        self.siguiente=siguiente
        self.anterior=anterior
        self.derecha=derecha
        self.izquierda=izquierda
        self.dato=dato
        self.vector=vector
        self.nombre=nombre

    def setIzquierda(self,valor):
        self.izquierda = valor
        if self.anterior is not None:
            self.anterior.derecha = valor

    def setDerecha(self,valor):
        self.derecha = valor
        if self.siguiente is not None:
            self.siguiente.izquierda = valor

""" #pruebas para los vectores
prueba = VectorB()
prueba.insertar(50)
prueba.imprimir()
prueba.insertar(4)
prueba.imprimir()
prueba.insertar(10)
prueba.imprimir()
prueba.insertar(15)
prueba.imprimir()
prueba.insertar(30)
prueba.imprimir()
prueba.buscar(15)
"""

# pruebas arbol B
arbol = ArbolB()

arbol.insertar(arbol.raiz,50)
arbol.insertar(arbol.raiz,5)
arbol.insertar(arbol.raiz,32)
arbol.insertar(arbol.raiz,10)
arbol.insertar(arbol.raiz,33)
arbol.insertar(arbol.raiz,3)
arbol.insertar(arbol.raiz,25)
arbol.insertar(arbol.raiz,45)
arbol.insertar(arbol.raiz,8)
arbol.insertar(arbol.raiz,4)
arbol.insertar(arbol.raiz,15)


arbol.insertar(arbol.raiz,46)
arbol.insertar(arbol.raiz,47)
arbol.insertar(arbol.raiz,22)
arbol.insertar(arbol.raiz,17)
arbol.insertar(arbol.raiz,66)
arbol.insertar(arbol.raiz,70)
arbol.insertar(arbol.raiz,80)

arbol.insertar(arbol.raiz,7)
arbol.insertar(arbol.raiz,6)



arbol.insertar(arbol.raiz,30)
arbol.insertar(arbol.raiz,27)
arbol.insertar(arbol.raiz,26)
arbol.insertar(arbol.raiz,11)
arbol.insertar(arbol.raiz,12)
arbol.insertar(arbol.raiz,13)

"""
arbol.insertar(arbol.raiz,Dato(1,5))
arbol.insertar(arbol.raiz,Dato(2,25))
arbol.insertar(arbol.raiz,Dato(3,6))
arbol.insertar(arbol.raiz,Dato(4,15))
arbol.insertar(arbol.raiz,Dato(5,31))
arbol.insertar(arbol.raiz,Dato(6,15))
arbol.insertar(arbol.raiz,Dato(7,12))
arbol.insertar(arbol.raiz,Dato(8,44))
arbol.insertar(arbol.raiz,Dato(9,9))
"""
#arbol.recorrer(arbol.raiz)
arbol.graf('arbol')
