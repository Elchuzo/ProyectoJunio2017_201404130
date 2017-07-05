
class ArbolB(object):
    def __init__(self):
        self.raiz = VectorB()
    def insertar(self,dato):


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
            final.siguiente.dato = final.dato
            final.dato = final.anterior.dato
            final = final.anterior
        final.siguiente.dato = final.dato
        if final.anterior is not None:
            final.dato = final.anterior.dato

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

class NodoVector(object):
    def __init__(self,siguiente=None,anterior=None,dato=None,derecha=None,izquierda=None):
        self.siguiente=siguiente
        self.anterior=anterior
        self.derecha=derecha
        self.izquierda=izquierda
        self.dato=dato


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
