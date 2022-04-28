POINT_USER = float(input("Escribe tu puntuacion: "))

def employee_score(POINT_USER = float) -> str :  
        MONEY = 2400
        POINTS = [0, 0.4, 0.6]
        LEVEL = ['INACEPTABLE','ACEPTABLE','MERITORIO']
        if POINT_USER in POINTS:
            if POINT_USER == POINTS[0]:
                level_user = LEVEL[0]
                money_user = MONEY * POINTS[0]
            elif POINT_USER == POINTS[1]:
                level_user = LEVEL[1]
                money_user = MONEY * POINTS[1]
            else:
                level_user = LEVEL[2]
                money_user = MONEY * POINTS[2]        
            return print(f'Tu nivel de rendimiento es {level_user}, obtienes {money_user} €')
        else:
            print(f"ERROR: Debe escribir la puntacion exacta: {POINTS}")          

if __name__ == '__main__':
    employee_score(POINT_USER)
