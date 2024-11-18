#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

def canonic(s):
    return s.lower().strip()

if __name__ == "__main__":
    
    dicc = {}
    print(dicc)

    # Uso el diccionario como conjunto
    dicc["Nombre"] = ""
    dicc["Apellido1"] = ""

    # Una forma canonica de una cadena
    # 1- No tiene espacios en blanco ni en cabeza ni en cola
    # 2- Todo minúsculas

    s= [
        "ramon",
        " Ramon",
        "Ramon  ",
        "ramON",
        "rAMon",
        "",
    ]


    for item in s:
        print(item.lower().strip())
        print(canonic(item))

