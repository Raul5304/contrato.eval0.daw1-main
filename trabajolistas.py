#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

from canonic import canonic

class monton():
    
    __stuff = []    

    def __init__(self, *args: ...):
        self.__stuff = []
        for item in args:
            self.amontona(item)
            self.__stuff.append(item)

    def __str__(self)-> str:
        answ = "<<"
        for item in self.__stuff:
            answ += f"{str(item)}, "
        answ += ">>"
        return answ
    
    def amontona(self, algo):
        if isinstance(algo, monton):
            self.__stuff.extend(algo.__stuff)
        else:
            self.__stuff.append(algo)
           
    def contiene(self, algo) -> bool:
        return algo in self.__stuff

    def copiar(self, algo) -> object:
        if algo in self.__stuff:
            return algo
        else:
            raise ValueError(f"No hay item en la lista")

    def tomar(self, algo) -> object:
        if algo in self.__stuff:
            self.__stuff.remove(algo)
            return algo
        else:
            raise ValueError(f"No hay item en la lista")

if __name__ == "__main__":
    
    m0 = monton()        # m0 es un nuevo monton vacio
    print(m0)
    

    m1 = monton("algo")  # m0 es un nuevo monton con "algo"
    m1.amontona("algo mas")
    # assert: en m1 hay "algo" y "algo mas" y NADA MAS.
    print(m1)

    m1.amontona("perla")
    # assert: en m1 hay "algo" y "algo mas" y "perla" y NADA MAS.
    print(m1)

    m1.amontona("y mas mierdas")
    # assert: en m1 hay ...
    print(m1)
    
    m0.amontona(m1)

    predicado = m0.contiene("perla") # predicado == True
    print(m0)
    
    copia = m0.copiar("perla") # copia == "perla"
    print(m0)
    
    tesoro = m0.tomar("perla") # tesoro == "perla" ; en m0 DESAPARECE la "perla"
    print(m0)