
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
        

        
        