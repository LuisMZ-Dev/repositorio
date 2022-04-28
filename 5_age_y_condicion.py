AGE = int(input("Ingrese la edad: "))
EARNINGS = int(input("Cuales son sus ingresos mensuales: "))

def pay_tribute(AGE = int, EARNINS = int) -> str:
    MUST_PAY = "Tiene que tributar"
    DONT_PAY = "No tienes que pgar"

    if AGE > 16 and EARNINGS >= 1000:
        msg = MUST_PAY
    else:
        msg = DONT_PAY
    return print(msg)

if __name__ == '__main__':
    pay_tribute(AGE, EARNINGS)