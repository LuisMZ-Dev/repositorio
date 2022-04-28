from unicodedata import name


PASSWORD = "contraseña"

def password(PASSWORD=str) -> str:
    SI="La contraseña coincide, fin del programa"
    NO="La contraseña NO coincide"    
    CONFIRM = input("escribe contraseña: ")

    if PASSWORD == CONFIRM:
        res=SI      
    else:
        res=NO        
    return print(res)

if __name__ == '__main__':
    password(PASSWORD)

