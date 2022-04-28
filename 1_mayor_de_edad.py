AGE= int(input("Escribe tu edad:  "))

def mayor_edad(edad=int) -> str:
   
    ADULT = 'Eres mayor de edad'
    YOUNGER = 'Eres menor de edad'
       
    if edad >= 18:
        you_are = ADULT
    else:
        you_are = YOUNGER    
    return print(you_are)
    
    
if __name__== '__main__':
    mayor_edad(AGE)





    