NAMEUSER = input("Escribe tu nombre: ")
GENDER = int(input("Escriba 1 para Masculino o 2 para Femenino: "))
NAME = NAMEUSER.strip().lower()

def indicate_group(NAME = str, GENDER = int) -> str:
    MAN = 1
    WOMAN = 2
    GROUP_A = "Perteneces al grupo A"
    GROUP_B = "Perteneces al grupo B"    
    if GENDER == WOMAN and NAME < 'm':
        msg = GROUP_A
    elif GENDER == MAN and NAME < 'n':
        msg = GROUP_A
    else:
        msg = GROUP_B
    return print(msg)

if __name__ == '__main__':
    indicate_group(NAME, GENDER)