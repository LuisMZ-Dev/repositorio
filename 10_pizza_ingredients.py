PREFERENCE = int(input("Seleccione opcion: \n 1 para pizza vegetariana \n 2 para pizza normal: "))

def pizza_ingredients(PREFERENCE: int) -> str:
    all_ingredient = 'Mozarella, tomate'
    
    if PREFERENCE == 1:
        res_selection= 'tu Pizza es vegetariana'
        print("Selecciona ingredientes:\n 1-Pimiento \n 2-tofu")
        selection = int(input("seleccioan tu ingrediente: "))
        if selection == 1:
            ingredient = "Pimiento"
        else:
            ingredient = "Tofu"
    else:
        print("selecciona ingredientes: \n 1-Peperoni \n 2-Jamon \n 3-Salmon")
        res_selection= 'tu Pizza no es vegetariana'
        selection = int(input("seleccioan tu ingrediente: "))
        if selection == 1:
            ingredient = "Peperoni"
        elif selection == 2:
            ingredient = "Jamon"
        else:
            ingredient = "Salmon"
    return print(f'{res_selection} sus ingredientes: \n {all_ingredient} y {ingredient}')

if __name__ =='__main__':
    pizza_ingredients(PREFERENCE)

    #Agregando comentario para probar este archivo