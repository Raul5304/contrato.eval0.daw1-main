#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

from canonic import canonic

class monton():

    __stuff = ""
    
    def __init__(self, *args):
        self.__stuff = ",".join(args)

    def __str__(self)-> str:
        return f"<<{self.__stuff}>>"
    
    def amontona(self, algo):
        if isinstance(algo, monton):
           if self.__stuff:
               self.__stuff += "," + algo.__stuff
            #    print(algo)
           else:
               self.__stuff = algo.__stuff
        else:
            palabra = canonic(str(algo))
            if self.__stuff:
                self.__stuff += "," + palabra
                # print(palabra)
            else:
                self.__stuff = palabra
           
    def contiene(self, algo) -> bool:
        palabra = str(algo)
        numero_perlas = self.__stuff.count(palabra)
        if numero_perlas >=1:
            # print(numero_perlas)
            return True
        else:
            print("Sin perlas")
            return False

    def copiar(self, algo) -> object:
        """doc..."""
        palabra = str(algo)
        num_perlas = 0
        if palabra in self.__stuff:
            num_perlas = self.__stuff.count(palabra)
            print(num_perlas)
            return palabra
        else:
            print("No hay perlas, no se ha devuelto ningún dato.")
            return None

    def tomar(self, algo) -> object:
        """doc..."""
        palabra = str(algo)
        num_perlas = 0
        if palabra in self.__stuff:
            num_perlas = self.__stuff.count(palabra)
            self.__stuff = self.__stuff.replace(palabra,'',num_perlas)
            self.__stuff = self.__stuff.replace(',,',',',num_perlas)
            print(num_perlas)
            return palabra
        else:
            print("No hay perlas, no se ha devuelto ningún dato.")
            return None

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

    # puedo amontonar -todo lo que haya- en un monton 
    # en otro moton.
    # Esto no vacia el monton argumentado (m1 aqui)
    # Esto no vacia previamente el monton invocado (m0 aqui)
    # no ~ m0 = m1
    m0.amontona(m1)

    predicado = m0.contiene("perla") # predicado == True
    print(m0)
    
    copia = m0.copiar("perla") # copia == "perla"
    print(m0)
    
    tesoro = m0.tomar("perla") # tesoro == "perla" ; en m0 DESAPARECE la "perla"
    print(m0)
    
    
    