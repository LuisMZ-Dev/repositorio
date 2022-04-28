NUM_1= int(input("Ingrese primer numero: "))
NUM_2= int(input("Ingrese segundo numero: "))

def division_error(NUM_1 = int, NUM_2 = int) -> str:
    MSJ_ERROR="ERROR el divisor NO  pude ser 0"

    if NUM_2 == 0:         
        RES=MSJ_ERROR
    else:
        RESULT= NUM_1 / NUM_2
        RES= RESULT
    return print(RES)

if __name__ == '__main__':
    division_error(NUM_1, NUM_2)