
class ArbolB(object):
    def __init__(self):
        self.raiz = VectorB()
    def insertar(self,raiz,dato):
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
                    if raiz.padre.izquierda = raiz:
                        print("El padre tiene este hijo a la izquierda")
                    elif raiz.padre.derecha = raiz:
                        print("El padre tiene este hijo a la derecha")
                    else:
                        print("Mi código no está en nada")
                    raiz.padre.insertar(raiz.p2.dato)
                    nod = raiz.padre.buscar(raiz.p2.dato)

                    pass
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
                    raiz.p0.izquierda = vizquierda # Asignar hijos derechos e izquierdos
                    raiz.p0.derecha = vderecha
                    vizquierda.padre = raiz.p0 # Asignar padres a los hijos creados
                    vderecha.padre = raiz.p0
                    # Pruebas, eliminar después
                    raiz.imprimir()
                    vizquierda.imprimir()
                    vderecha.imprimir()
                    print("La raiz se ha separado")


class VectorB(object):
        def __init__(self,size=4):
        self.size = size
        #Definir todos los nodos del vector al ser iniciado
        self.p4 = NodoVector()
        self.p3 = NodoVector(self.p4)
        self.p2 = NodoVector(self.p3)
        self.p1 =  NodoVector(self.p2)
        self.p0 = NodoVector(self.p1)
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
            return print((str(dato) + ' ha sido ingresado'))
        if self.cantidad_datos() < 5: # Al tener 5 datos se debe separar el vector
            actual = self.p0
            while not insertado:

                if dato < actual.dato:
                    self.corrernodos(actual)
                    actual.dato = dato
                    insertado = True
                    return print((str(dato) + ' ha sido ingresado'))
                while (dato > actual.dato):
                    if actual.siguiente.dato is not None:
                        actual = actual.siguiente
                    else:
                        actual.siguiente.dato = dato
                        insertado = True
                        return print((str(dato) + ' ha sido ingresado'))
#que no quede huella que no y que no

    def corrernodos(self,actual=None):
        final = self.p4
        while final.dato is None:
            final = final.anterior
        while final != actual:
            final.siguiente.dato = final.dato # Correr el dato del nodo una posición a la izquierda
            final.siguiente.izquierda = final.izquierda # Asignar los hijos derechos e izquierdos del nodo una posición a la izquierda
            final.siguiente.derecha = final.derecha
            final.dato = final.anterior.dato # Correr el dato anterior al nodo actual a la posición del nodo actual
            final.izquierda = final.anterior.izquierda # Asignar los hijos derechos e izquierdos a la posicion del nodo actual
            final.derecha = final.anterior.derecha
            final = final.anterior
        # El código se debe ejecutar una vez más (se puede optimizar pero no quiero pensar)
        final.siguiente.dato = final.dato
        final.siguiente.izquierda = final.izquierda
        final.siguiente.derecha = final.derecha
        if final.anterior is not None:
            final.dato = final.anterior.dato
            final.izquierda = final.anterior.izquierda # (Optimizable)
            final.derecha = final.anterior.derecha #Metodo para desplazar los nodos

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
        actual = self.p0
        cadena = ''
        if actual.dato is not None:
            cadena = cadena + str(actual.dato)
        while(actual.siguiente.dato is not None):
            actual = actual.siguiente
            cadena = cadena + " _ " + str(actual.dato)
            if actual.siguiente is None:
                break
        print(cadena)

    def tiene_hijos(self):
        if self.p0.izquierda is not None or self.p0.derecha is not None:
            return True
        else:
            return False

    def cambiar(self,vector):
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
    def __init__(self,siguiente=None,anterior=None,dato=None,derecha=None,izquierda=None):
        self.siguiente=siguiente
        self.anterior=anterior
        self.derecha=derecha
        self.izquierda=izquierda
        self.dato=dato

    def setIzquierda(self,valor):
        self.izquierda = valor
    def setDerecha(self,valor):
        self.derecha = valor
"""
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
arbol = ArbolB()
arbol.insertar(arbol.raiz,50)
arbol.insertar(arbol.raiz,5)
arbol.insertar(arbol.raiz,32)
arbol.insertar(arbol.raiz,10)
arbol.insertar(arbol.raiz,33)
arbol.insertar(arbol.raiz,3)
arbol.insertar(arbol.raiz,25)
arbol.insertar(arbol.raiz,45)
arbol.raiz.imprimir()
arbol.raiz.p0.izquierda.imprimir()
arbol.raiz.p0.derecha.imprimir()
