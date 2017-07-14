from graphviz import Digraph
class Hash(object):
    def __init__(self,tamanio,pmax,pmin):
        self.tamanio=tamanio
        self.pmax=pmax
        self.pmin=pmin
        self.dict={}
    def pasarascii(self,cadena):
        cad=''
        l = [ord(c) for c in cadena]
        for c in l:
            cad+=str(c)
        square = int(cad)**2
        #print(square)
        return str(square)

    def mitadcuadrado(self,cadena):
        t = len(cadena)
        pos = t//2
        a = cadena[pos] + cadena[pos+1]
        return int(a)

    def calcularpos(self,pos):
        if pos > self.tamanio:
            return pos % self.tamanio
        else:
            return pos

    def porcentaje(self):
        p = (len(self.dict) / self.tamanio)*100
        return p

    def insertar(self,dato):
        asc = self.pasarascii(dato.nombre)
        mitad = self.mitadcuadrado(asc)
        pos = self.calcularpos(mitad)
        ingresado = False
        while not ingresado:
            if pos in self.dict:
                pos+=1
            else:
                self.dict[pos] = dato
                ingresado = True
        if self.porcentaje() >= 60:
            print('el porcentaje ha llegado a 60')
            self.rehash() # rehash
        print('el usuario: ' + dato.nombre + ' ha sido ingresado en la posicion: ' + str(pos))

    def eliminar(self,dato):
        for codigo, nombre in self.dict.items():
            if nombre == dato:
                #print(str(codigo) + " : " + str(nombre) + "  " + str(dato))
                pos = codigo
        print( "codigo: " + str(pos))
        del self.dict[pos]
        if self.porcentaje() <= 30 and self.tamanio > 47:
            self.rehashm()
            di = {}
            lista = self.dict.items()
            for u in lista:
                asc = self.pasarascii(u[1].nombre)
                mitad = self.mitadcuadrado(asc)
                pos = self.calcularpos(mitad)
                ingresado = False
                while not ingresado:
                    if pos in di:
                        pos+=1
                    else:
                        di[pos] = u[1]
                        ingresado = True
            self.dict = None
            self.dict = di

    def rehash(self):
        tam = self.tamanio*2
        if self.esprimo(tam):
            self.tamanio = tam
        else:
            while not self.esprimo(tam):
                tam+=1
            self.tamanio=tam

    def rehashm(self):
        tam = self.tamanio//2
        if self.esprimo(tam):
            self.tamanio=tam
        else:
            while not self.esprimo(tam):
                tam-=1
            self.tamanio=tam

    def recorrer(self):
        lista = self.dict.items()
        for u in lista:
            print(u[0],u[1].nombre,sep=" ")
    def esprimo(self,n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i+2)==0:
                return False
            i = i+6
        return True
    def graf(self,dot):
        cadena = 'node0 [label = "<p0>'
        for x in range(0,self.tamanio):
            if x in self.dict:
                cadena+= ' |' + str(x) + '. ' + self.dict[x].nombre + '| h<p'+str(x+1)+'>'
            else:
                cadena+= ' |' + str(x) + '. | h<p'+str(x+1)+'>'
        cadena+='|",height=3];'
        dot.body.append(cadena)
        #print(cadena)

    def graficar(self,imagen):
        dot = Digraph(comment='Thash',format='png')
        dot.body.append(' rankdir = LR;')
        dot.body.append('node [shape=record, width=.1, height=.1];')
        #dot.body.append('rotate=90;')
        self.graf(dot)
        dot.render("C:\\Users\\Abraham Jelkmann\\Desktop\\"+imagen,cleanup=True)
        dot.save(imagen,r"C:\\Users\\Abraham Jelkmann\\Desktop")

class Usuario(object):
    def __init__(self,nombre=None,contrasena=None,conectado=None):
        self.nombre=nombre
        self.contrasena=contrasena
        self.conectado=conectado
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



#hs = Hash(47,60,30)
"""
hs.insertar(Usuario('chuz','chuz',0))
hs.insertar(Usuario('Tbone','chuz',0))
hs.insertar(Usuario('Mord85','chuz',0))
hs.insertar(Usuario('potter','chuz',0))
hs.insertar(Usuario('manchas','chuz',0))
hs.insertar(Usuario('so good','chuz',0))
hs.insertar(Usuario('the thing','chuz',0))
hs.insertar(Usuario('taon1','chuz',0))
hs.insertar(Usuario('taon2','chuz',0))
hs.insertar(Usuario('taon3','chuz',0))
hs.insertar(Usuario('taon4','chuz',0))
hs.insertar(Usuario('taon5','chuz',0))
hs.insertar(Usuario('taon6','chuz',0))
hs.insertar(Usuario('taon7','chuz',0))
hs.insertar(Usuario('taon8','chuz',0))
hs.insertar(Usuario('taon9','chuz',0))
hs.insertar(Usuario('taon10','chuz',0))
hs.insertar(Usuario('taon11','chuz',0))
hs.insertar(Usuario('taon12','chuz',0))
hs.insertar(Usuario('taon13','chuz',0))
hs.insertar(Usuario('taon14','chuz',0))
hs.insertar(Usuario('taon15','chuz',0))
hs.insertar(Usuario('taon16','chuz',0))
hs.insertar(Usuario('taon17','chuz',0))
hs.insertar(Usuario('taon18','chuz',0))
hs.insertar(Usuario('taon19','chuz',0))
hs.insertar(Usuario('taon20','chuz',0))
hs.insertar(Usuario('taon21','chuz',0))
hs.insertar(Usuario('taon22','chuz',0))
hs.insertar(Usuario('taon23','chuz',0))

hs.insertar(Usuario('sony','chuz',0))
hs.insertar(Usuario('aturner','chuz',0))
hs.insertar(Usuario('timmy','chuz',0))
hs.eliminar(Usuario('taon9','chuz',0))
hs.eliminar(Usuario('taon11','chuz',0))
hs.eliminar(Usuario('taon12','chuz',0))
hs.eliminar(Usuario('taon3','chuz',0))
hs.eliminar(Usuario('taon4','chuz',0))
"""

#hs.recorrer()
#hs.graficar('hash')
