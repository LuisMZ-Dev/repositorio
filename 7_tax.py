ANNUAL_RENT = int(input("Escribe tu renta anual: "))

def tax(ANNUAL_RENT = int)-> str:
    TAX= [10000, 20000, 35000, 60000]
    PCT= [5, 15, 20, 30, 45] 
    
    if   ANNUAL_RENT < TAX[0]:
        percentage = PCT[0]
        tax_to_pay = int(ANNUAL_RENT / 100 * PCT[0])
    elif ANNUAL_RENT < TAX[1]:
        percentage = PCT[1]
        tax_to_pay = int(ANNUAL_RENT / 100 * PCT[1])
    elif ANNUAL_RENT < TAX[2]:
        percentage = PCT[2]
        tax_to_pay = int(ANNUAL_RENT / 100 * PCT[2])
    elif ANNUAL_RENT < TAX[3]:
        percentage = PCT[3]
        tax_to_pay = int(ANNUAL_RENT / 100 * PCT[3])
    else:
        percentage = PCT[4]
        tax_to_pay = int(ANNUAL_RENT / 100 * PCT[4])    

    return print(f"Tu impositivo es de {percentage}%, debe pagar {tax_to_pay} €")

if __name__ == '__main__':
    tax(ANNUAL_RENT)