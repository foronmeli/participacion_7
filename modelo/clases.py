from dataclasses import dataclass

class Conjunto:
    contador=0
    def __init__(self,nombre):
        self.elemento=[]
        self.nombre=nombre
        Conjunto.contador+=1
        
@property
def id(self):
        self.asigna=Conjunto.contador.value()
        return self.asigna
    
def contiene(self,elemento)->bool:
        if elemento in self.elemento:
            return "El nombre ya existe"
        else:
            self.elemento.append(elemento)
    
def agregar_elemento(self,conjunto1):
        elemento=conjunto1
        self.contiene(elemento)

def unir(self, conjunto2):
        conjunto=Conjunto(f"{self.nombre} UNION {conjunto2.nombre}")
        for elemento in self.elemento:
            conjunto.agregar_elemento(elemento)
        return conjunto

def __add__(self, conjunto2):
        return self.unir(conjunto2) 

def intersectar(self, conjunton1, conjunton2):
        interseccion = [i for i in conjunton1.elemento if i in conjunton2.elemento]
        nombre_resultante = f"{conjunton1.nombre} INTERSECTADO {conjunton2.nombre}"
        conjunto = Conjunto(nombre_resultante)
        for elemento in interseccion:
            conjunto.agregar_elemento(elemento)
        return conjunto

def __str__(self):
        elementos = ', '.join(elemento.nombre for elemento in self.elemento)
        return f"Conjunto {self.nombre}: ({elementos})"
    
@dataclass
class Elemento:
    nombre:str
    def __eq__(self,nombre):
        if self.nombren==nombre:
            return True
        else:
            return False
        