NUMBER = int(input("Escribe un numero entero: "))

def validate(NUMBER=int) -> str:
    EVEN_NUMBER = "Es un numero Par"
    ODD_NUMBER = "Es un numero Impar"

    if NUMBER % 2 == 0:
        message = EVEN_NUMBER
    else:
        message = ODD_NUMBER
    return print(message)

if __name__ == '__main__':
        validate(NUMBER)