#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

# from marvelous import rainbow

class monton():
 
    # __stuff = {} # bronce
    # __stuff = () # bronce
    __stuff = [] # plata
    # __stuff = "" # PARA MASOCAS
    # __stuff = ... import maravilla # GLORIA
    
    def __init__(self, algo = ""):
        """doc..."""
        self.__stuff = algo

    def __str__(self)-> str:
        """doc..."""
        answ = f"La lista es: {m0}"
        return answ
    
    def amontona(self, algo):
        """doc..."""
        self.__stuff = self.__stuff.append(algo)

    def contiene(self, algo) -> bool:
        """doc..."""
        if self.__stuff == self:
            pass
            
        return True # pass

    def copiar(self, algo) -> object:
        """doc..."""
        return "Foo" # pass

    def tomar(self, algo) -> object:
        """doc..."""
        return "Foo" # pass

if __name__ == "__main__":
    
    m0 = monton()        # m0 es un nuevo monton vacio
    print(m0)

    exit(0) # ==========================================

    m1 = monton("algo")  # m0 es un nuevo monton con "algo"
    m1.amontona("algo mas")
    # assert: en m1 hay "algo" y "algo mas" y NADA MAS.

    m1.amontona("perla")
    # assert: en m1 hay "algo" y "algo mas" y "perla" y NADA MAS.

    m1.amontona("y mas mierdas")
    # assert: en m1 hay ...

    # puedo amontonar -todo lo que haya- en un monton 
    # en otro moton.
    # Esto no vacia el monton argumentado (m1 aqui)
    # Esto no vacia previamente el monton invocado (m0 aqui)
    # no ~ m0 = m1
    m0.amontona(m1)

    predicado = m0.contiene("perla") # predicado == True
    copia = m0.copiar("perla") # copia == "perla"
    tesoro = m0.tomar("perla") # tesoro == "perla" ; en m0 DESAPARECE la "perla"
    