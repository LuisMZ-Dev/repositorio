AGE= int(input("Cual es tu edad: "))

def calculate_price(AGE: int) -> str:   

    if AGE > 0:
        if AGE < 4:
            msg = 0
        elif AGE <= 18:
            msg = 5
        else:
            msg= 10
    else:
        msg = 'La edad debe se mayor a 0'
    return print(f'el precio de la entrada es {msg}€')
    
if __name__ == '__main__':
    calculate_price(AGE)