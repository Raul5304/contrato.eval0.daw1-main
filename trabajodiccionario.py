#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

from canonic import canonic

class Monton:
    
    __stuff = {}  # Usamos un diccionario vacío en lugar de una lista.

    def __init__(self, *args: ...):
        self.__stuff = {}
        for item in args:
            self.amontona(item)
    
    def __str__(self) -> str:
        answ = "<<"
        for key, value in self.__stuff.items():
            answ += f"({key}: {value}), "
        answ += ">>"
        return answ
    
    def amontona(self, algo):
        if isinstance(algo, Monton):
            self.__stuff.update(algo.__stuff)
        elif isinstance(algo, dict):
            self.__stuff.update(algo)
        else:
            raise ValueError("Solo se puede agregar un objeto tipo Monton o diccionario.")
    
    def contiene(self, key) -> bool:
        """Verifica si una clave está en el diccionario."""
        return key in self.__stuff

    def copiar(self, key) -> object:
        """Devuelve el valor de la clave si existe."""
        if key in self.__stuff:
            return self.__stuff[key]
        else:
            raise ValueError(f"No hay clave '{key}' en el diccionario")

    def tomar(self, key) -> object:
        """Elimina una clave y devuelve su valor."""
        if key in self.__stuff:
            return self.__stuff.pop(key)
        else:
            raise ValueError(f"No hay clave '{key}' en el diccionario")


if __name__ == "__main__":
    
    m0 = Monton()  # m0 es un nuevo Monton vacío
    print(m0)
    
    m1 = Monton({"clave1": "algo"})  # m1 es un nuevo Monton con la clave "clave1" y valor "algo"
    m1.amontona({"clave2": "algo mas"})  # Se añade un nuevo par clave-valor
    print(m1)

    m1.amontona({"clave3": "perla"})  # Se añade otro par clave-valor
    print(m1)

    m1.amontona({"clave4": "y mas mierdas"})  # Se añade otro par clave-valor
    print(m1)
    
    m0.amontona(m1)  # Se amontonan los elementos de m1 en m0

    predicado = m0.contiene("clave3")  # Verifica si "clave3" está en m0
    print(f"¿Contiene 'clave3'? {predicado}")
    print(m0)
    
    copia = m0.copiar("clave3")  # Copia el valor de la clave "clave3"
    print(f"Copia de 'clave3': {copia}")
    
    tesoro = m0.tomar("clave3")  # Toma (elimina) el par clave-valor "clave3"
    print(f"Eliminada la 'clave3': {tesoro}")
    print(m0)